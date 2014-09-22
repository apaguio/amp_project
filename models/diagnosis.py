from models import influxdb

def get_ekm_data_range(meter_id, start, end):
    """
    Gets EKM data in the given datetime range
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm start start UTC timestamp (in seconds)
    @parm end end UTC timestamp (in seconds)
    """
    query = 'select * from "%s" where time > %ss and time < %ss' % (meter_id, start, end)
    result = influxdb.query(query)
    if result:
        return result[0]
    return result
