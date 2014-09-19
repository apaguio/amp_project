from datetime import datetime, time
from models import db

def generate():
    customer = db.Customer(name='test', email='test@example.com')
    billing_periods = init_billing_periods()
    read_cycle = db.ReadCycle(name='V', billing_periods=billing_periods)
    customer.read_cycle = read_cycle
    customer.save()

    summer = db.Season(name='Summer', start=datetime(2014, 5, 1), end=datetime(2014, 10, 31))
    get_summer_peak_periods(summer)
    winter = db.Season(name='Winter', start=datetime(2013, 11, 1), end=datetime(2014, 4, 30))
    get_winter_peak_periods(winter)
    customer.seasons = [winter, summer]
    customer.save()

def get_summer_peak_periods(summer):
    onpeak_period = db.PeakPeriod(name='onpeak', start=time(12).isoformat(),
                                end=time(17, 59, 59).isoformat(), energy_charge=0.19, demand_charge=21.46)
    offpeak_period = db.PeakPeriod(name='offpeak', start=time(18).isoformat(),
                                end=time(11, 59, 59).isoformat(), energy_charge=0.08, demand_charge=12.74)
    summer.peak_periods = [onpeak_period, offpeak_period]

def get_winter_peak_periods(winter):
    partpeak_period = db.PeakPeriod(name='partpeak', start=time(8, 30).isoformat(),
                                end=time(21, 29, 59).isoformat(), energy_charge=0.1, demand_charge=4.58)
    offpeak_period = db.PeakPeriod(name='offpeak', start=time(21, 30).isoformat(),
                                end=time(8, 29, 59).isoformat(), energy_charge=0.07, demand_charge=4.58)
    winter.peak_periods = [partpeak_period, offpeak_period]

def init_billing_periods():
    b1 = db.BillingPeriod(name='JAN', start=datetime(2013, 12, 17), end=datetime(2014, 1, 15), number_of_days=30)
    b2 = db.BillingPeriod(name='FEB', start=datetime(2014, 1, 16), end=datetime(2014, 2, 17), number_of_days=33)
    b3 = db.BillingPeriod(name='MAR', start=datetime(2014, 2, 18), end=datetime(2014, 3, 18), number_of_days=29)
    b4 = db.BillingPeriod(name='APR', start=datetime(2014, 3, 19), end=datetime(2014, 4, 17), number_of_days=30)
    b5 = db.BillingPeriod(name='MAY', start=datetime(2014, 4, 18), end=datetime(2014, 5, 18), number_of_days=31)
    b6 = db.BillingPeriod(name='JUN', start=datetime(2014, 5, 19), end=datetime(2014, 6, 17), number_of_days=30)
    b7 = db.BillingPeriod(name='JUL', start=datetime(2014, 6, 18), end=datetime(2014, 7, 17), number_of_days=30)
    b8 = db.BillingPeriod(name='AUG', start=datetime(2014, 7, 18), end=datetime(2014, 8, 18), number_of_days=32)
    b9 = db.BillingPeriod(name='SEP', start=datetime(2014, 8, 19), end=datetime(2014, 9, 17), number_of_days=30)
    b10 = db.BillingPeriod(name='OCT', start=datetime(2014, 9, 18), end=datetime(2014, 10, 16), number_of_days=29)
    b11 = db.BillingPeriod(name='NOV', start=datetime(2014, 10, 17), end=datetime(2014, 11, 17), number_of_days=32)
    b12 = db.BillingPeriod(name='DEC', start=datetime(2014, 11, 18), end=datetime(2014, 12, 16), number_of_days=29)
    return [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]