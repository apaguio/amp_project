from datetime import datetime, time
from models import db
from pytz import timezone, utc

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
    customer.solar = solar_meters
    customer.save()

    summer = db.Season(name='Summer', start=utc.localize(datetime(2014, 5, 1)),
                       end=utc.localize(datetime(2014, 10, 31)))
    get_summer_peak_periods(summer)
    winter = db.Season(name='Winter', start=utc.localize(datetime(2013, 11, 1)),
                       end=utc.localize(datetime(2014, 4, 30)))
    get_winter_peak_periods(winter)
    customer.seasons = [winter, summer]
    customer.save()

def init_facility_meters():
    meter1 = db.EkmMeter(id='10054', api_key='MTAxMDoyMDIw')
    return [meter1,]

def init_solar_meters():
    meter1 = db.EkmMeter(id='10068', api_key='MTAxMDoyMDIw')
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
