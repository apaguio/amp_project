import time
from datetime import datetime
from models import mongodb, influxdb

#@app.route('/ekm_data_one_second/<meter_id>/<int:duration_in_seconds>')
def get_ekm_data(meter_id, period):
    """
    Gets EKM Data
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm period    time window in appended by time letter ( s - seconds, m - minutes, h - hours, d - days)
    """
    query = 'select P from "%s" where time > now() - %s limit 1000;' % (meter_id, period)
    result = influxdb.query(query)
    if result:
        return result[0]
    return result

#@app.route('/current_demand/<meter_id>')
def get_current_demand(meter_id):
    utc_now = datetime.utcfromtimestamp(time.time()) # current request time
    # round to nearest 15-min interval, and calculate minutes difference
    number_of_miutes = utc_now.minute - ((utc_now.minute / 15) * 15)
    #utc_now.strftime('%Y-%m-%d %H:%M:%S')
    query = 'select mean(P) as current_demand from "%s" group by time(%sm) limit 1;' % (meter_id, number_of_miutes)
    result = influxdb.query(query)
    if result:
        return result[0]['points'][0][1]
    return result

#@app.route('/tarrif/<name>')
def get_tarrif_details(name):
    """
    Gets the Tarrif Details
    TODO: PLEASE ADD MORE INFORMATION
    """
    # later on, can be extended by periods
    result = mongodb.db.tarrif.find_one({'name': name}, fields={'_id': False}) or list()
    return result

