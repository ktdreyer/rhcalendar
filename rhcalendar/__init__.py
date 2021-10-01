from rhcalendar.locales import locales
import workdays

__version__ = '1.3.2'


def networkdays(from_date, to_date, locale='en-US'):
    """ Return the net work days according to RH's calendar. """
    holidays = locales[locale]
    return workdays.networkdays(from_date, to_date, holidays)
