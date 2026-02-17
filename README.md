# Red Hat business days calendar

[![image](https://github.com/ktdreyer/rhcalendar/workflows/tests/badge.svg)](https://github.com/ktdreyer/rhcalendar/actions)

[![image](https://badge.fury.io/py/rhcalendar.svg)](https://badge.fury.io/py/rhcalendar)

This module builds on [workdays](https://pypi.org/project/workdays/) to
provide a `networkdays()` method that knows about the Red Hat business
holidays.

# Example: determine number of business days from today

```python
import datetime
from rhcalendar import networkdays

today = datetime.date.today()
to_date = datetime.date(2026, 1, 1)  # something far away...

days = networkdays(from_date=today, to_date=to_date)

print(f'{to_date} is {days} Red Hat business days from now.')
# prints "2026-01-01 is 209 Red Hat business days from now."
```

# Locales

Currently this module has the Red Hat holiday calendars for the US and
Quebec, Canada. Contributions welcome for other locales.

```python
# Locale option defaults to 'en-US':
days = workdays(from_date, to_date)

# Or use Quebec, Canada holidays:
days = workdays(from_date, to_date, locale='qc-CA')
```
