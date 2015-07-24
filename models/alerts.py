from flask_login import current_user

def update_customer_alerts(one_minute_netload_avg_threshold, power_factor_threshold, voltage_threshold):
    current_user.one_minute_netload_avg_threshold = one_minute_netload_avg_threshold
    current_user.power_factor_threshold = power_factor_threshold
    current_user.voltage_threshold = voltage_threshold
    current_user.save()

def update_customer_contacts(alerts_emails, alerts_phones):
    current_user.alerts_emails = alerts_emails
    current_user.alerts_phones = alerts_phones
    current_user.save()