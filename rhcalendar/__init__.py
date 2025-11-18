from rhcalendar.locales import locales
import workdays

try:
    from rhcalendar._version import __version__
except ImportError:
    # Version file not generated yet (e.g., during development before build)
    __version__ = "0.0.0+unknown"


def networkdays(from_date, to_date, locale='en-US'):
    """ Return the net work days according to RH's calendar. """
    holidays = locales[locale]
    return workdays.networkdays(from_date, to_date, holidays)
