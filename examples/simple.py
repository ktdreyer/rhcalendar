import datetime
from rhcalendar import networkdays

today = datetime.date.today()
to_date = datetime.date(2020, 1, 1)  # something far away...

days = networkdays(from_date=today, to_date=to_date)

print('%s is %d Red Hat business days from now.' % (to_date, days))
