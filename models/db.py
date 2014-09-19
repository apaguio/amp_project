from datetime import datetime
from models import mongodb

class PeakPeriod(mongodb.EmbeddedDocument):
    name = mongodb.StringField()
    start = mongodb.StringField() # start_time in ISO format
    end = mongodb.StringField() # end_time in ISO format
    energy_charge = mongodb.FloatField()
    demand_charge = mongodb.FloatField()

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
    billing_periods = mongodb.ListField(mongodb.EmbeddedDocumentField(BillingPeriod))

class Customer(mongodb.Document):
    name = mongodb.StringField()
    email = mongodb.EmailField()
    read_cycle = mongodb.EmbeddedDocumentField(ReadCycle)
    seasons = mongodb.ListField(mongodb.EmbeddedDocumentField(Season))