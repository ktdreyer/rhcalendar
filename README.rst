Red Hat business days calendar
==============================

.. image:: https://github.com/ktdreyer/rhcalendar/workflows/tests/badge.svg
             :target: https://github.com/ktdreyer/rhcalendar/actions

.. image:: https://badge.fury.io/py/rhcalendar.svg
             :target: https://badge.fury.io/py/rhcalendar


This module builds on `workdays <https://pypi.org/project/workdays/>`_ to
provide a ``networkdays()`` method that knows about the Red Hat business
holidays.

Example: determine number of business days from today
-----------------------------------------------------

.. code-block:: python

    import datetime
    from rhcalendar import networkdays

    today = datetime.date.today()
    to_date = datetime.date(2023, 1, 1)  # something far away...

    days = networkdays(from_date=today, to_date=to_date)

    print('%s is %d Red Hat business days from now.' % (to_date, days))
    # prints "2023-01-01 is 522 Red Hat business days from now."

Locales
-------

Currently this module has the Red Hat holiday calendars for the US and Quebec,
Canada. Contributions welcome for other locales.

.. code-block:: python

    # Locale option defaults to 'en-US':
    days = workdays(from_date, to_date)

    # Or use Quebec, Canada holidays:
    days = workdays(from_date, to_date, locale='qc-CA')

Packages that use this package
------------------------------

* `helga-productpages <https://pypi.org/project/helga-productpages/>`_
