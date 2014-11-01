from models import mongodb

class EkmMeter(mongodb.EmbeddedDocument):
    id = mongodb.StringField()
    api_key = mongodb.StringField()
    url = mongodb.StringField(default='io.ekmpush.com')
    solar = mongodb.BooleanField(default=False)

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

class Historical(mongodb.EmbeddedDocument):
    id = mongodb.StringField()
    name = mongodb.StringField()
    start = mongodb.DateTimeField()
    end = mongodb.DateTimeField()
    resolution = mongodb.StringField()
    graphs = mongodb.ListField(mongodb.StringField())
    maxDemandPeak = mongodb.StringField()

    def get_id(self):
        return str(self.id)

class Customer(mongodb.Document):
    name = mongodb.StringField()
    email = mongodb.EmailField()
    password = mongodb.StringField()
    facility_name = mongodb.StringField()
    timezone = mongodb.StringField(default='PST8PDT')
    read_cycle = mongodb.EmbeddedDocumentField(ReadCycle)
    seasons = mongodb.ListField(mongodb.EmbeddedDocumentField(Season))
    facility = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
    solar = mongodb.ListField(mongodb.EmbeddedDocumentField(EkmMeter))
    holidays = mongodb.ListField(mongodb.DateTimeField())
    historicals = mongodb.ListField(mongodb.EmbeddedDocumentField(Historical))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.pk)

