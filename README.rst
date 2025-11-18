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
    to_date = datetime.date(2026, 1, 1)  # something far away...

    days = networkdays(from_date=today, to_date=to_date)

    print(f'{to_date} is {days} Red Hat business days from now.')
    # prints "2026-01-01 is 209 Red Hat business days from now."

Locales
-------

Currently this module has the Red Hat holiday calendars for the US and Quebec,
Canada. Contributions welcome for other locales.

.. code-block:: python

    # Locale option defaults to 'en-US':
    days = workdays(from_date, to_date)

    # Or use Quebec, Canada holidays:
    days = workdays(from_date, to_date, locale='qc-CA')

Development
-----------

Building
~~~~~~~~

This project uses ``uv`` for modern Python packaging:

.. code-block:: bash

    # Build the package
    uv build

    # Install in development mode
    uv pip install -e .

Releasing
~~~~~~~~~

This project uses ``bump-my-version`` for version management and GitHub Actions
for automated releases to PyPI.

To create a new release:

.. code-block:: bash

    # Bump version and create tag
    bump-my-version bump patch  # or minor/major
    git push origin main --tags

    # Create GitHub Release (triggers automatic PyPI publish)
    gh release create v1.3.7 --generate-notes

The GitHub Actions workflow will automatically build and publish to PyPI using
trusted publishing.
