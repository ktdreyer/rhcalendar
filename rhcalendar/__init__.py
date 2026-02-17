import datetime

import workdays  # type: ignore[import-untyped]

from rhcalendar.locales import locales

__version__ = '1.3.6'


def networkdays(from_date: datetime.date, to_date: datetime.date,
                locale: str = 'en-US') -> int:
    """ Return the net work days according to RH's calendar. """
    holidays = locales[locale]
    return workdays.networkdays(from_date, to_date, holidays)
