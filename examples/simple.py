import datetime
from rhcalendar import networkdays

today = datetime.date.today()
to_date = datetime.date(2026, 1, 1)  # something far away...

days = networkdays(from_date=today, to_date=to_date)

print(f'{to_date} is {days} Red Hat business days from now.')
