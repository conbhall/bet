import datetime
import calendar

def load_dates(year, month):
    num_days = calendar.monthrange(year, month)[1]
    dates = [
        datetime.date(year, month, day).strftime('%Y-%m-%d')
        for day in range(1, num_days + 1)
    ]

    return dates

def load_dates_between_months(start_year, start_month, end_year, end_month):
    dates = []

    current_year = start_year
    current_month = start_month

    while (current_year, current_month) <= (end_year, end_month):
        dates.extend(load_dates(current_year, current_month))

        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
    
    return dates

def load_dates_between(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1)
    
    return dates