from flask import Blueprint, request
import xml.etree.ElementTree as ET
from models import db, influxdb
from datetime import datetime
from redis import Redis
from meter_settings import SOLAR_METER_ID, CONSUMPTION_METER_ID

PSUEDO_FEED = False

if PSUEDO_FEED:
    import pprint
    import time
    import random

redis = Redis()

consume_app = Blueprint('consume_app', __name__)

def log_data_received(xml_data):
    root = ET.fromstring(xml_data)
    a8810_serial_number = ''
    a8810_name = ''  
    for element in root:
        # EXTRACT a8810 information
        if element.tag == 'mode':
            if element.text != 'LOGFILEUPLOAD':
                # The a8810 is doing something this endpoint does
                # not support. Cease processing.
                break
        if element.tag == 'serial':
            a8810_serial_number = element.text
        if element.tag == 'name':
            a8810_name = element.text

    devices = root.findall('./devices/device')

    for device in devices:
        device_name = ''
        device_address = ''
        device_type = ''
        device_class = ''
        for element in device:
            if element.tag == 'name':
                device_name = element.text
            if element.tag == 'address':
                device_address = element.text
            if element.tag == 'type':
                device_type = element.text
            if element.tag == 'class':
                device_class = element.text
        
        if PSUEDO_FEED:
            # setup data structure for solar meter
            data1 = {'name': SOLAR_METER_ID, 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
            # setup data structure for consumption meter
            data2 = {'name': CONSUMPTION_METER_ID, 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
        else:
            data = {'name': device_name, 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
        
        # For each device node, scan for records
        records = device.findall('./records/record')
        for i, record in enumerate(records):
            timestamp = ''
            error = ''
            error_code = 0
            for element in record:
                if element.tag == 'time':
                    utc_reading = datetime.strptime(element.text, '%Y-%m-%d %H:%M:%S')
                    timestamp = int((utc_reading - datetime(1970, 1, 1)).total_seconds()) # save points in db with UTC timestamps                    
                if element.tag == 'error':
                    error = element.get('text')
                    error_code = int(element.text)
            
            # Finally extract all the data points
            data_points = record.findall('./point')
            power = 0
            power_factor = 0
            voltage = 0
            if PSUEDO_FEED:
                power2 = 0
                power_factor2 = 0
                voltage2 = 0
            
            for data_point in data_points:
                # extract power value
                if data_point.get('number') == '9' and data_point.get('name') == 'Watts, 3-Ph total':
                    if PSUEDO_FEED:
                        power = (long(float(data_point.get('value'))) * 1000) + time.localtime()[4] + random.randint(100, 200)
                        power2 = long(random.randint(500, 600))
                    else:
                        power = long(float(data_point.get('value'))) * 1000 # converted to watts like EKM meters provide
                # extract power factor value
                if data_point.get('number') == '12' and data_point.get('name') == 'Power Factor, 3-Ph total':
                    if PSUEDO_FEED:
                        power_factor = random.randint(90, 99)/100.0
                        power_factor2 = power_factor
                    else:
                        power_factor = float(data_point.get('value'))
                # extract voltage value
                if data_point.get('number') == '0' and data_point.get('name') == 'Volts A-N':
                    if PSUEDO_FEED:
                        voltage = int(float(data_point.get('value'))) + time.localtime()[4]
                        voltage2 = voltage
                    else:
                        voltage = int(float(data_point.get('value')))

            if PSUEDO_FEED:
                point1 = [timestamp, power, power_factor, voltage]
                data1['points'].append(point1)            
                point2 = [timestamp, power2, power_factor2, voltage2]
                data2['points'].append(point2)
            else:
                point = [timestamp, power, power_factor, voltage]
                data['points'].append(point)            
        
        # Publishing to pubsub when event occurs, to be sent by socket.io
        if PSUEDO_FEED:
            publish_msg = {'meter_id': CONSUMPTION_METER_ID, 'points': data1['points']}
            redis.publish('point', publish_msg)
            publish_msg = {'meter_id': SOLAR_METER_ID, 'points': data2['points']}
            redis.publish('point', publish_msg)
        else:
            publish_msg = {'meter_id': device_name, 'points': data['points']}
            redis.publish('point', publish_msg)
            
        ## Write to influxdb
        if PSUEDO_FEED:
            #f = open('a8810_data.txt', 'a')
            #pprint.pprint(data1, f)
            #pprint.pprint(data2, f)
            #f.close()

            # store solar data
            influxdb.write_points([data1])
            # store consumption data
            influxdb.write_points([data2])
        else:
            # store meter data
            influxdb.write_points([data])

@consume_app.route('/consume', methods=['GET', 'POST'])
def consume_a8810_data():
    if request.method == 'POST':
        #TODO: Write code to actually save the data to the database but for now try to capture
        #      the data upload via HTTP POST from the AcquiSuite
        try:
            if PSUEDO_FEED:
                import a8810_data
                log_data_received(a8810_data.get_data())
                return 'Success'
            else:
                data = request.get_data()
                form = request.form
                for field in form:
                    print 'The value of {field} is "{value}"'.format(field=field, value=form[field])
                log_data_received(data)
                return 'Success'
        except:
            return 'Bad'
    else:
        return 'Ok'

#if __name__ == '__main__':
#    pass
