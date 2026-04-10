import datetime

import workdays  # type: ignore[import-untyped]

from rhcalendar.locales import locales

try:
    from rhcalendar._version import __version__
except ImportError:
    __version__ = "0.0.0+unknown"


def networkdays(from_date: datetime.date, to_date: datetime.date,
                locale: str = 'en-US') -> int:
    """ Return the net work days according to RH's calendar. """
    holidays = locales[locale]
    return workdays.networkdays(from_date, to_date, holidays)
