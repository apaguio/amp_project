from flask import Blueprint, request
from flask import Response
import csv
from models import db, influxdb
from datetime import datetime
from redis import Redis
from meter_settings import SOLAR_METER_ID, CONSUMPTION_METER_ID
import pprint
import gzip, StringIO
import os

redis = Redis()

VALID_PASSWORDS = (u'', )

consume_app = Blueprint('consume_app', __name__)

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data.split('\n')),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        if len(line.strip()) == 0:
            continue
        yield line.encode('utf-8')

def log_data_received(request):
    if request.form['MODE'] != 'LOGFILEUPLOAD':
        if request.form['MODE'] == 'STATUS':
            return
        else:
            return
    # Get the FileStorage instance from request
    logfile = request.files['LOGFILE']
    device_address = os.path.basename(logfile.filename).split('.')[0][3:]
    compressed_data = StringIO.StringIO(logfile.read())
    uncompressed_data = gzip.GzipFile(fileobj=compressed_data, mode='rb')
    
    data = {'name': str(int(device_address)), 'columns': ['time', 'P', 'L1_PF', 'L1_V'], 'points': []}
    
    for row in unicode_csv_reader(uncompressed_data.read()):
        utc_reading = datetime.strptime(row[0].replace("'", ""), '%Y-%m-%d %H:%M:%S')
        timestamp = int((utc_reading - datetime(1970, 1, 1)).total_seconds()) # save points in db with UTC timestamps                    
        power = long(float(row[14])) * 1000 # converted data point "Total Net Instantaneous Real Power" to watts like EKM meters provide
        power_factor = float(row[17]) # data point "Total Power Factor"
        voltage = int(float(row[70])) # data point "Voltage, Phase A - N"
        point = [timestamp, power, power_factor, voltage]
        data['points'].append(point)            
    
    influxdb.write_points([data])

@consume_app.route('/consume', methods=['GET', 'POST'])
def consume_a8810_data():
    if request.method == 'POST':
        #TODO: Write code to actually save the data to the database but for now try to capture
        #      the data upload via HTTP POST from the AcquiSuite
        try:
            data = request.get_data()
            if request.form['PASSWORD'] in VALID_PASSWORDS:
                log_data_received(request)
                return 'SUCCESS'
            else:
                raise Exception('Password not found.')
        except Exception as ex:
            f = open('/tmp/a8810_error.txt', 'a')
            f.write(str(ex))
            f.close()
            return 'FAILURE'
    else:
        data = request.get_data()
        return 'SUCCESS'

#if __name__ == '__main__':
#    pass
