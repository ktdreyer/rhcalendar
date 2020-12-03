import datetime
from rhcalendar import networkdays


def test_en_us():
    from_date = datetime.date(2021, 12, 30)
    to_date = datetime.date(2021, 12, 31)
    result = networkdays(from_date, to_date, locale='en-US')
    assert result == 0
