
import datetime

def calculate_due_date(start_date, duration):
    due_date = start_date + datetime.timedelta(days=duration)
    return due_date
