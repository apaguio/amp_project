from models import mongodb
from flask_login import AnonymousUserMixin

class EkmMeter(mongodb.EmbeddedDocument):
    id = mongodb.StringField()
    api_key = mongodb.StringField()

class PeakPeriodSchedule(mongodb.EmbeddedDocument):
    day_of_week = mongodb.IntField()
    start = mongodb.StringField() # start_time in ISO format
    end = mongodb.StringField() # end_time in ISO format

class PeakPeriod(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    schedule = mongodb.ListField(mongodb.EmbeddedDocumentField(PeakPeriodSchedule))
    energy_charge = mongodb.FloatField()
    demand_charge = mongodb.FloatField()
    peak_demand_charge = mongodb.FloatField()

class Season(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    start = mongodb.DateTimeField()
    end = mongodb.DateTimeField()
    peak_periods = mongodb.ListField(mongodb.EmbeddedDocumentField(PeakPeriod))

class BillingPeriod(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    start = mongodb.DateTimeField()
    end = mongodb.DateTimeField()
    number_of_days = mongodb.IntField()

class ReadCycle(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    rate_tariff = mongodb.StringField()
    billing_periods = mongodb.ListField(mongodb.EmbeddedDocumentField(BillingPeriod))

class Customer(mongodb.Document):
    name = mongodb.StringField()
    email = mongodb.EmailField()
    password = mongodb.StringField()
    timezone = mongodb.StringField(default='PST8PDT')
    read_cycle = mongodb.EmbeddedDocumentField(ReadCycle)
    seasons = mongodb.ListField(mongodb.EmbeddedDocumentField(Season))
    facility = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
    solar = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
    holidays = mongodb.ListField(mongodb.DateTimeField())
    one_minute_netload_avg_threshold = mongodb.FloatField()
    power_factor_threshold = mongodb.FloatField()
    voltage_threshold = mongodb.FloatField()
    alerts_emails = mongodb.ListField(mongodb.EmailField())
    alerts_phones = mongodb.ListField(mongodb.StringField())
    alert_frequency_in_minutes = mongodb.IntField(default=15)
    last_alerted = mongodb.IntField()

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        print "Getting customer ID : %s" % self.pk
        return str(self.pk)

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.name = 'Guest'