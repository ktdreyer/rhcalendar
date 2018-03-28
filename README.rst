Red Hat business days calendar
==============================

This module builds on `workdays <https://pypi.python.org/pypi/workdays/>`_ to
provide a ``networkdays()`` method that knows about the Red Hat business
holidays.

Example: determine number of business days from today
-----------------------------------------------------

.. code-block:: python

    import datetime
    from rhcalendar import networkdays

    today = datetime.date.today()
    to_date = datetime.date(2020, 1, 1)  # something far away...

    days = networkdays(from_date=today, to_date=to_date)

    print('%s is %d Red Hat business days from now.' % (to_date, days))
    # prints "2020-01-01 is 435 Red Hat business days from now."

Locales
-------

Currently this module only has the Red Hat US holiday calendar. Contributions
welcome for other locales.

.. code-block:: python

    # Only locale option is 'en-US' (the default) for now.
    days = workdays(from_date, to_date, locale='en-US')
