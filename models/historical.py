from models import utils
from datetime import datetime

def get_ekm_data(meter_id, start, end, resolution=None):
    """
    Gets EKM data in the given datetime range
    @parm meter_id  currently ( 10068 - consumption, 10054 - solar )
    @parm start start UTC timestamp (in seconds)
    @parm end end UTC timestamp (in seconds)
    @parm resolution data resolution, i.e aggregation interval, same format as period, like: 1m, 5m, etc
          leave it None (default) to get 1s resolution, i.e all data available (large data sets)
    """
    acceptableResolution = utils.acceptableResolution(resolution)

    if not resolution or resolution == '1s':
        query = 'select P, L1_PF, L1_V from "%s" where time > %ss and time < %ss ;' % (meter_id, start, end)
    else:
        if acceptableResolution:
            query = 'select P, L1_PF, L1_V from "%s_%s" where time > %ss and time < %ss;' % (meter_id, acceptableResolution, start, end)
        else:
            query = '''select mean(P) as P, mean(L1_PF) as L1_PF, mean(L1_V) as L1_V
                    from "%s" where time > %ss and time < %ss group by time(%s);''' % (meter_id, start, end, resolution)

    print query
    return utils.collect_ekm_data(query)

