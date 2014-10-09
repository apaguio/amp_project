from models import mongodb
import uuid

class EkmMeter(mongodb.EmbeddedDocument):
    id = mongodb.StringField()
    api_key = mongodb.StringField()

class PeakPeriod(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    start = mongodb.StringField() # start_time in ISO format
    end = mongodb.StringField() # end_time in ISO format
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
    rate_tarrif = mongodb.StringField()
    billing_periods = mongodb.ListField(mongodb.EmbeddedDocumentField(BillingPeriod))

class Customer(mongodb.Document):
    uid = mongodb.UUIDField(default=uuid.uuid4())
    name = mongodb.StringField()
    email = mongodb.EmailField()
    timezone = mongodb.StringField(default='PST8PDT')
    read_cycle = mongodb.EmbeddedDocumentField(ReadCycle)
    seasons = mongodb.ListField(mongodb.EmbeddedDocumentField(Season))
    facility = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
    solar = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
