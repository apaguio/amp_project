from datetime import datetime, time
from models import db, influxdb
from pytz import timezone, utc
from celerybeatmongo.models import PeriodicTask
from settings import EKM_READING_INTERVAL

def generate():
    customer = db.Customer(name='test', email='test@example.com', password='c3nergy')
    customer.holidays = [utc.localize(datetime(2014, 11, 11)),
                         utc.localize(datetime(2014, 11, 27)),
                         utc.localize(datetime(2014, 12, 25))]
    # all datetime data are set in UTC format
    billing_periods = init_billing_periods()
    facility_meters = init_facility_meters()
    solar_meters = init_solar_meters()
    read_cycle = db.ReadCycle(name='V', billing_periods=billing_periods, rate_tariff='AG-5E')
    customer.read_cycle = read_cycle
    customer.facility = facility_meters
    customer.facility_name = 'Cenergy'
    customer.solar = solar_meters
    customer.save()

    summer = db.Season(name='Summer', start=utc.localize(datetime(2014, 5, 1)),
                       end=utc.localize(datetime(2014, 11, 1)))
    get_summer_peak_periods(summer)
    winter = db.Season(name='Winter', start=utc.localize(datetime(2014, 11, 1)),
                       end=utc.localize(datetime(2015, 5, 1)))
    get_winter_peak_periods(winter)
    customer.seasons = [winter, summer]

    init_customer_tasks(customer)

    customer.save()

def init_customer_tasks(customer):
    user_id = customer.get_id()
    meters = customer.facility + customer.solar
    for meter in meters:
        meter_type = 'solar' if meter.solar else 'facility' 
        args1 = {'user_id': user_id, 'meter_id': meter.id, 'nr_readings': EKM_READING_INTERVAL,
                 'key': meter.api_key, 'endpoint': meter.url, 'simulate_solar': meter.solar}
        p1 = PeriodicTask(name='ekm.%s.%s.%s' % (user_id, meter_type, meter.id), task='tasks.ekm.collect', enabled=True,
                         interval={'every': EKM_READING_INTERVAL, 'period': 'seconds'}, kwargs=args1).save()
        args2 = {'user_id': user_id, 'meter_id': meter.id}
        p2 = PeriodicTask(name='ekm.%s.%s.%s.15mins.aggregator' % (user_id, meter_type, meter.id), task='tasks.ekm.facility.15mins.aggregator', enabled=True,
                         crontab={'minute': '0, 15, 30, 45'}, kwargs=args2).save()
        args3 = {'user_id': user_id, 'meter_id': meter.id}
        p3 = PeriodicTask(name='%s.%s.%s.energy.usage.aggregator' % (user_id, meter_type, meter.id), task='tasks.energy.1h.aggregator', enabled=True,
                         crontab={'minute': '0'}, kwargs=args3).save()
        resolutions = ('1m', '5m', '15m', '30m', '1h', '24h')
        for resolution in resolutions:
            args1['resolution'] = resolution
            meter_continuous_query = '''select mean(P) as P, mean(L1_PF) as L1_PF, mean(L1_V) as L1_V
                                        from "%(user_id)s_%(meter_id)s"
                                        group by time(%(resolution)s)
                                        into "%(user_id)s_%(meter_id)s_%(resolution)s"''' % args1
            influxdb.query(meter_continuous_query)

def init_facility_meters():
    meter1 = db.EkmMeter(id='10054', api_key='MTAxMDoyMDIw')
    return [meter1,]

def init_solar_meters():
    meter1 = db.EkmMeter(id='10068', api_key='MTAxMDoyMDIw', solar=True)
    return [meter1,]

def get_summer_peak_periods(summer):
    onpeak_schedule = [db.PeakPeriodSchedule(day_of_week=0, start=time(12).isoformat(), end=time(17, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=1, start=time(12).isoformat(), end=time(17, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=2, start=time(12).isoformat(), end=time(17, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=3, start=time(12).isoformat(), end=time(17, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=4, start=time(12).isoformat(), end=time(17, 59, 59).isoformat())]
    onpeak_period = db.PeakPeriod(name='onpeak', schedule=onpeak_schedule, energy_charge=0.19, demand_charge=8.72, peak_demand_charge=21.46)

    offpeak_schedule = [db.PeakPeriodSchedule(day_of_week=0, start=time(18).isoformat(), end=time(11, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=1, start=time(18).isoformat(), end=time(11, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=2, start=time(18).isoformat(), end=time(11, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=3, start=time(18).isoformat(), end=time(11, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=4, start=time(18).isoformat(), end=time(11, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=5, start=time(0).isoformat(), end=time(23, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=6, start=time(0).isoformat(), end=time(23, 59, 59).isoformat())]
    offpeak_period = db.PeakPeriod(name='offpeak', schedule=offpeak_schedule, energy_charge=0.08, demand_charge=12.74)
    summer.peak_periods = [onpeak_period, offpeak_period]

def get_winter_peak_periods(winter):
    partpeak_schedule = [db.PeakPeriodSchedule(day_of_week=0, start=time(8, 30).isoformat(), end=time(21, 29, 59).isoformat()),
                         db.PeakPeriodSchedule(day_of_week=1, start=time(8, 30).isoformat(), end=time(21, 29, 59).isoformat()),
                         db.PeakPeriodSchedule(day_of_week=2, start=time(8, 30).isoformat(), end=time(21, 29, 59).isoformat()),
                         db.PeakPeriodSchedule(day_of_week=3, start=time(8, 30).isoformat(), end=time(21, 29, 59).isoformat()),
                         db.PeakPeriodSchedule(day_of_week=4, start=time(8, 30).isoformat(), end=time(21, 29, 59).isoformat())]
    partpeak_period = db.PeakPeriod(name='partpeak', schedule=partpeak_schedule, energy_charge=0.1, demand_charge=4.58)

    offpeak_schedule = [db.PeakPeriodSchedule(day_of_week=0, start=time(21, 30).isoformat(), end=time(8, 29, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=1, start=time(21, 30).isoformat(), end=time(8, 29, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=2, start=time(21, 30).isoformat(), end=time(8, 29, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=3, start=time(21, 30).isoformat(), end=time(8, 29, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=4, start=time(21, 30).isoformat(), end=time(8, 29, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=5, start=time(0).isoformat(), end=time(23, 59, 59).isoformat()),
                       db.PeakPeriodSchedule(day_of_week=6, start=time(0).isoformat(), end=time(23, 59, 59).isoformat())]
    offpeak_period = db.PeakPeriod(name='offpeak', schedule=offpeak_schedule, energy_charge=0.07, demand_charge=4.58)
    winter.peak_periods = [partpeak_period, offpeak_period]

def init_billing_periods():
    b1 = db.BillingPeriod(name='JAN', start=utc.localize(datetime(2013, 12, 17)), end=utc.localize(datetime(2014, 1, 16)), number_of_days=30)
    b2 = db.BillingPeriod(name='FEB', start=utc.localize(datetime(2014, 1, 16)), end=utc.localize(datetime(2014, 2, 18)), number_of_days=33)
    b3 = db.BillingPeriod(name='MAR', start=utc.localize(datetime(2014, 2, 18)), end=utc.localize(datetime(2014, 3, 19)), number_of_days=29)
    b4 = db.BillingPeriod(name='APR', start=utc.localize(datetime(2014, 3, 19)), end=utc.localize(datetime(2014, 4, 18)), number_of_days=30)
    b5 = db.BillingPeriod(name='MAY', start=utc.localize(datetime(2014, 4, 18)), end=utc.localize(datetime(2014, 5, 19)), number_of_days=31)
    b6 = db.BillingPeriod(name='JUN', start=utc.localize(datetime(2014, 5, 19)), end=utc.localize(datetime(2014, 6, 18)), number_of_days=30)
    b7 = db.BillingPeriod(name='JUL', start=utc.localize(datetime(2014, 6, 18)), end=utc.localize(datetime(2014, 7, 18)), number_of_days=30)
    b8 = db.BillingPeriod(name='AUG', start=utc.localize(datetime(2014, 7, 18)), end=utc.localize(datetime(2014, 8, 19)), number_of_days=32)
    b9 = db.BillingPeriod(name='SEP', start=utc.localize(datetime(2014, 8, 19)), end=utc.localize(datetime(2014, 9, 18)), number_of_days=30)
    b10 = db.BillingPeriod(name='OCT', start=utc.localize(datetime(2014, 9, 18)), end=utc.localize(datetime(2014, 10, 17)), number_of_days=29)
    b11 = db.BillingPeriod(name='NOV', start=utc.localize(datetime(2014, 10, 17)), end=utc.localize(datetime(2014, 11, 18)), number_of_days=32)
    b12 = db.BillingPeriod(name='DEC', start=utc.localize(datetime(2014, 11, 18)), end=utc.localize(datetime(2014, 12, 17)), number_of_days=29)
    return [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]
