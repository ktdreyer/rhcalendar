import datetime
from rhcalendar import networkdays


def test_en_us():
    from_date = datetime.date(2023, 12, 28)
    to_date = datetime.date(2023, 12, 29)
    result = networkdays(from_date, to_date, locale='en-US')
    assert result == 0
