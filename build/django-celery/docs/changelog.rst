================
 Change history
================

.. contents::
    :local:

.. _version-3.0.23:

3.0.23
======
:release-date: 2013-09-03 02:00 P.M BST

- Now depends on celery 3.0.23

- ``djcelery.contrib.test_runner`` used naive datetimes
  resulting in ``RuntimeWarning`` (Issue #242).

- Cache backend now compatible with Django 1.5.

    Fix contributed by Weipin Xia.

- DatabaseScheduler: Periodic task admin form now validates args and kwargs.

    Contributed by Justin Quick

- DatabaseScheduler: IntervalSchedule and CrontabSchedule will now be ordered
  in a more natural way.

    Contributed by @anagorny.

- Django Admin monitor:  Worker and Task now supports ``extra_context`.

    Fix contributed by @realitycheck

- Django Admin monitor: Now properly formats task tracebacks.

    Fix contributed by Vladislav Poluhin.

.. _version-3.0.21:

3.0.21
======
:release-date: 2013-08-26 04:00 P.M BST

- Now depends on Celery 3.0.21

- Fixed problems with time zones.

    Fix contributed by Jeffrey Hu

- Now compatible with Django 2.5

    Fixes contributed by Jay States, AlexRiina

- Experimental support for Python 3 (using 2to3).

.. _version-3.0.17:

3.0.17
======
:release-date: 2013-03-28 05:00 P.M BST

- Now depends on celery 3.0.17

- Tests passing on Django 1.5

- Fixed problem with the deprecated ``celeryd_multi`` command
  when using the ``--workdir`` option.

- Fixed current date handling when used with Django 1.5
  and ``USE_TZ`` is disabled.

    Fix contributed by Theo Spears.

- Now makes sure to not attempt converting already
  aware datetimes.

    Fix contributed by Idan Zalzberg.

- Admin Monitor: Fixed timezone problem (Issue #183)

    Fix contributed by Scott Rubin.

- Admin Monitor: Better formatting for task tracebacks.

    Contributed by Vladislav Poluhin.

- DatabaseScheduler: Now logs if a periodic task is automatically
  disabled because of invalid JSON in args/kwargs.

    Contributed by Gnrhxni.

- celerycam: Do update and delete queries in the same transaction
  when expiring old items.

.. _version-3.0.11:

3.0.11
======
:release-date: 2012-10-10 02:30 P.M BST

- Now depends on celery 3.0.11.

- Now depends on :mod:`pytz`

- Fixed Django Admin monitor timezone problem.

    Events still use timestamps that converts to the timezone of the receiving
    node, but a proper fix is being worked on that will be part of Celery 3.1

- Fixed error in database close mechanism for Oracle.

    Fix contributed by Dan LaMotte.


3.0.10
======
:release-date: 2012-09-21 10:29 A.M BST

- Now depends on Celery 3.0.10

- Fixed timezone issues when using the Database periodic task scheduler.

- Admin: Periodic task form now adds tasks imported using ``CELERY_IMPORTS``,
  and ``CELERY_INCLUDE``.

- Memory leak warning is now only output once.

- Periodic task form in Admin no longer lists the celery built-in tasks.

.. _version-3.0.9:

3.0.9
=====
:release-date: 2012-08-31 06:00 P.M BST

Important note:

Celery 3.0.9 fixes an issue with periodic tasks and timezones.

If you are using the database periodic task scheduler
then you have to reset the `last_run_at` fields
to ensure that no invalid timezones are stored:

.. code-block:: bash

    $ python manage.py shell
    >>> from djcelery.models import PeriodicTask
    >>> PeriodicTask.objects.update(last_run_at=None)

- Now depends on Celery 3.0.9

    See the Celery changelog for more information:

        http://docs.celeryproject.org/en/latest/changelog.html

- Don't close fds for database connections without a fileno.

- Fixes Oracle compatibility issue for closing an already
  closed connection.

    Fix contributed by Dan LaMotte.

- New test suite runner that stores results in the database:
  :class:`djcelery.contrib.test_runner.CeleryTestSuiteRunnerStoringResult`.

    Contributed by Kirill Panshin.

.. _version-3.0.6:

3.0.6
=====
:release-date: 2012-08-17 11:00 P.M BST

- Now depends on celery 3.0.6

- Naive datetime's received by Celery are now assumed to be UTC.

- The example demoproject no longer used ``djcelery.setup_loader``.

- Fixed south migration warning (Issue #149).

    Fix contributed by Roman Imankulov.

- No longer uses deprecated urls module.

    Fix contributed by Simon Charette.

- Databases are no longer closed after fork, instead we close
  the underlying file descriptors, so parent process can continue
  to use the connection (Issue #161).

    Fix contributed by Alex Stapleton.

.. _version-3.0.4:

3.0.4
=====
:release-date: 2012-07-26 07:00 P.M BST
:by: Ask Solem

- Now depends on celery 3.0.4

- ``CELERY_ENABLE_UTC`` is now disabled for Django versions
  before 1.4 (Issue #158).

- celerycam: No longer overwrites name, args, kwargs and eta if the
  received event is missing (Issue #148 + Issue #155).

    Fix contributed by Kirill Panshin.

- Fixed problem with migrations when running the tests.

    Fix contributed by Roger Barnes.

- New utilities:

    - :func:`djcelery.common.respect_language`

        Context manager for the with statement that changes the language used.
        For example::

            from celery import task
            from djcelery.common import respect_language

            @task
            def my_task(language=None):
                with respect_language(language):
                    ...

    - :func:`djcelery.common.respects_language`

        Decorator version of the above that adds a ``language`` keyword
        argument to any function that it decorates::

            @task
            @respects_language
            def my_task():
                pass

            my_task.delay(language=translation.get_language())

    Contributed by @ramusus

.. _version-3.0.1:

3.0.1
=====
:release-date: 2012-07-10 06:00 P.M BST
:by: Ask Solem

Important Notes
---------------

The 3.0 changelog forgot to mention that two of the database
tables has been altered, so you must either use South to migrate
the tables or alter the tables manually::

        ALTER TABLE celery_taskmeta
            ADD meta TEXT NULL DEFAULT "";

        ALTER TABLE djcelery_crontabschedule
            ADD day_of_month VARCHAR(64) NOT NULL DEFAULT "*";

        ALTER TABLE djcelery_crontabschedule
            ADD month_of_year VARCHAR(64) NOT NULL DEFAULT "*";

Fixes
-----

- Now depends on Celery 3.0.1

- Fixes problems with South migrations (Issue #149)

    Fix contributed by Roman Imankulov.

- Task monitor must store task eta in UTC (Issue #139).

    Fix contributed by Mike Ivanov.

.. _version-3.0.0:

3.0.0
=====
:release-date: 2012-07-07 01:00 P.M BST
:by: Ask Solem

.. _v300-important:

Important Notes
---------------

- Now depends on Celery 3.0

    It is important that you read the What's New document for the 3.0 series:
    http://docs.celeryproject.org/en/latest/whatsnew-3.0.html

- No longer depends on :mod:`django-picklefield`

    And as such the result backend will no longer deepcopy return
    values or exceptions.

- Celery 3.0 is the last release to require django-celery

    Starting with Celery 3.1 the django-celery package will no longer be
    required and Celery will support Django out of the box.

    The django-celery package may still exist for some time to provide
    additional utilities like the django-admin monitor.

- django-celery 3.0 is the last series to support Python 2.5.

    Celery will no longer support Python 2.5 starting with version 3.1.

- New :program:`manage.py celery` umbrella command replaces older commands.

    All commands except for :program:`manage.py celeryevcam` can
    now be started using the new umbrella command::

        $ manage.py celery worker -l info           # <<< NEW
        $ manage.py celeryd -l info                 # <-- OLD

        $ manage.py celery status                   # <<< NEW
        $ manage.py celeryctl status                # <-- OLD

        $ manage.py celery beat -l info             # <<< NEW
        $ manage.py celerybeat -l info              # <-- OLD

        $ manage.py celery multi start ...          # <<< NEW
        $ manage.py celeryd_multi start ...         # <-- OLD

        $ manage.py celery amqp queue.delete celery # <<< NEW
        $ manage.py camqadm queue.delete celery     # <-- OLD

    See ``manage.py celery help`` for a complete list of supported commands.

    The old commands will still work, but you are encouraged to start
    using the new umbrella command.

- The distribution :file:`contrib/` directory is now renamed to
  :file:`extra/`.

- The django-celery source code repository has moved

    The new location is at http://github.com/celery/django-celery

.. _v260-news:

News
----

- New Spanish translation.

    Contributed by Diego Andres Sanabria Martin.

.. _v300-fixes:

Fixes
-----

- Fixes an UTC bug when ``CELERY_ENABLE_UTC`` was enabled (Issue #131).

- Database Periodic Task Scheduler: Disabling a periodic task now also
  resets its last_run_at field. So that the schedule will restart from
  scratch if re-enabled (Issue #370).

- Database Periodic Task Scheduler: Now retries the sync operation
  if database errors occur.

.. _version-2.5.5:

2.5.5
=====
:release-date: 2012-04-19 01:46 P.M BST

* Fixed bug where task modules were not imported.

.. _version-2.5.4:

2.5.4
=====
:release-date: 2012-04-16 06:31 P.M BST

* Compatibility with celery 2.5.3

* Database scheduler now imports ``exchange``, ``routing_key`` and ``queue``
  options from ``CELERYBEAT_SCHEDULE``.

.. _version-2.5.3:

2.5.3
=====
:release-date: 2012-04-13 06:16 P.M BST
:by: Ask Solem

* 2.5.2 release broke installation because of an import in the package.

    Fixed by not having setup.py import the djcelery module anymore,
    but rather parsing the package file for metadata.

.. _version-2.5.2:

2.5.2
=====
:release-date: 2012-04-13 05:00 P.M BST
:by: Ask Solem

.. _v252-news:

News
----

* PeriodicTask admin now lists the enabled field in the list view

    Contributed by Gabe Jackson.

.. _v252-fixes:

Fixes
-----

* Fixed a compatibility issue with Django < 1.3

    Fix contributed by Roman Barczyski

* Admin monitor now properly escapes args and kwargs.

    Fix contributed by Serj Zavadsky

* PeriodicTask admin now gives error if no schedule set (or both set)
  (Issue #126).

* examples/demoproject has been updated to use the Django 1.4 template.

* Database connection is no longer closed for eager tasks (Issue #116).

    Fix contributed by Mark Lavin.

* The first-steps document for django-celery has been moved to the main
  Celery documentation.

* djcelerymon command no longer worked properly, this has now been fixed
  (Issue #123).

.. _version-2.5.1:

2.5.1
=====
:release-date: 2012-03-01 01:00 P.M GMT
:by: Ask Solem

.. _v251-fixes:

Fixes
-----

* Now depends on Celery 2.5.1

* Fixed problem with recursive imports when USE_I18N was enabled
  (Issue #109).

* The ``CELERY_DB_REUSE_MAX`` setting was not honored.

* The djcelerymon command no longer runs with DEBUG.

    To enable debug you can set the :envvar:`DJCELERYMON_DEBUG`
    environment variable.

* Fixed eventlet/gevent compatability with Django 1.4's new thread
  sharing detection.

* Now depends on django-picklefield 0.2.0 or greater.

    Previous versions would not work correctly with Django 1.4.

.. _version-2.5.0:

2.5.0
=====
:release-date: 2012-02-24 02:00 P.M GMT
:by: Ask Solem

.. _v250-important:

Important Notes
---------------

* Now depends on Celery 2.5.

* Database schema has been updated.

    After upgrading you need migrate using South, or migrate manually
    as described below.

    These changes means that expiring results will be faster and
    take less memory than before.

    In addition a description field to the PeriodicTask model has
    been added so that the purpose of a periodic task
    in the database can be documented via the Admin interface.

    **South Migration**

    To migrate using South execute the following command::

        $ python manage.py migrate djcelery

    If this is a new project that is also using South then you need
    to fake the migration:

        $ python manage.y migrate djcelery --fake

    **Manual Migration**

    To manually add the new fields,

    using PostgreSQL:

    .. code-block: sql

        ALTER TABLE celery_taskmeta
            ADD hidden BOOLEAN NOT NULL DEFAULT FALSE;

        ALTER TABLE celery_tasksetmeta
            ADD hidden BOOLEAN NOT NULL DEFAULT FALSE;

        ALTER TABLE djcelery_periodictask
            ADD description TEXT NOT NULL DEFAULT ""

    using MySQL:

    .. code-block:: sql

        ALTER TABLE celery_taskmeta
            ADD hidden TINYINT NOT NULL DEFAULT 0;

        ALTER TABLE celery_tasksetmeta
            ADD hidden TINYINT NOT NULL DEFAULT 0;

        ALTER TABLE djcelery_periodictask
            ADD description TEXT NOT NULL DEFAULT "";

    using SQLite:

    .. code-block:: sql

        ALTER TABLE celery_taskmeta
            ADD hidden BOOL NOT NULL DEFAULT FALSE;
        ALTER TABLE celery_tasksetmeta
            ADD hidden BOOL NOT NULL DEFAULT FALSE;
        ALTER TABLE djcelery_periodictask
            ADD description VARCHAR(200) NOT NULL DEFAULT "";

.. _v250-news:

News
----

* Auto-discovered task modules now works with the new auto-reloader
  functionality.

* The database periodic task scheduler now tried to recover from
  operational database errors.

* The periodic task schedule entry now accepts both int and
  timedelta (Issue #100).

* 'Connection already closed' errors occurring while closing
  the database connection are now ignored (Issue #93).

* The ``djcelerymon`` command used to start a Django admin monitor
  instance outside of Django projects now starts without a celery
  config module.

* Should now work with Django 1.4's new timezone support.

   Contributed by Jannis Leidel and Donald Stufft.

* South migrations did not work properly.

    Fix contributed by Christopher Grebs.

* celeryd-multi now preserves django-related arguments,
  like ``--settings`` (Issue #94).


* Migrations now work with Django < 1.3 (Issue #92).

    Fix contributed by Jude Nagurney.

* The expiry of the database result backend can now be an int (Issue #84).


.. _version-2.4.2:

2.4.2
=====
:release-date: 2011-11-14 12:00 P.M GMT

* Fixed syntax error in South migrations code (Issue #88).

    Fix contributed by Olivier Tabone.

.. _version-2.4.1:

2.4.1
=====
:release-date: 2011-11-07 06:00 P.M GMT
:by: Ask Solem

* Management commands was missing command line arguments because of recent
  changes to Celery.

* Management commands now supports the ``--broker|-b`` option.

* South migrations now ignores errors when tables already exist.

.. _version-2.4.0:

2.4.0
=====
:release-date: 2011-11-04 04:00 P.M GMT
:by: Ask Solem

.. _240-important:

Important Notes
---------------

This release adds `South`_ migrations, which well assist users in automatically
updating their database schemas with each django-celery release.

.. _`South`: http://pypi.python.org/pypi/South/

.. _240-news:

News
----

* Now depends on Celery 2.4.0 or higher.

* South migrations have been added.

    Migration 0001 is a snapshot from the previous stable release (2.3.3).
    For those who do not use South, no action is required.
    South users will want to read the :ref:`240-upgrade_south` section
    below.

    Contributed by Greg Taylor.

* Test runner now compatible with Django 1.4.

    Test runners are now classes instead of functions,
    so you have to change the ``TEST_RUNNER`` setting to read::

        TEST_RUNNER = "djcelery.contrib.test_runner.CeleryTestSuiteRunner"

    Contributed by Jonas Haag.

.. _240-upgrade_south:

Upgrading for south users
-------------------------

For those that are already using django-celery 2.3.x, you'll need to fake the
newly added migration 0001, since your database already has the current
``djcelery_*`` and ``celery_*`` tables::

    $ python manage.py migrate djcelery 0001 --fake

If you're upgrading from the 2.2.x series, you'll want to drop/reset your
``celery_*`` and ``djcelery_*`` tables and run the migration::

    $ python manage.py migrate djcelery

.. _version-2.3.3:

2.3.3
=====
:release-date: 2011-08-22 12:00 AM BST

* Precedence issue caused database backend tables to not be
  created (Issue #62).

.. _version-2.3.2:

2.3.2
=====
:release-date: 2011-08-20 12:00 AM BST

* Fixes circular import of DatabaseBackend.

.. _version-2.3.1:

2.3.1
=====
:release-date: 2011-08-11 12:00 PM BST

* Django database result backend tables were not created.

  If you are having troubles because of this, be sure you do a ``syncdb``
  after upgrading, that should resolve the issue.

.. _version-2.3.0:

2.3.0
=====
:release-date: 2011-08-05 12:00 PM BST

* Now depends on Celery 2.3.0

    Please read the Celery 2.3.0 changelog!

.. _version-2.2.4:

2.2.4
=====

* celerybeat: DatabaseScheduler would not react to changes when using MySQL and
  the default transaction isolation level ``REPEATABLE-READ`` (Issue #41).

    It is still recommended that you use isolation level ``READ-COMMITTED``
    (see the Celery FAQ).

.. _version-2.2.3:

2.2.3
=====
:release-date: 2011-02-12 16:00 PM CET

* celerybeat: DatabaseScheduler did not respect the disabled setting after restart.

* celeryevcam: Expiring objects now works on PostgreSQL.

* Now requires Celery 2.2.3

.. _version-2.2.2:

2.2.2
=====
:release-date: 2011-02-03 16:00 PM CET

* Now requires Celery 2.2.2

* Periodic Task Admin broke if the CELERYBEAT_SCHEDULE setting was not set.

* DatabaseScheduler No longer creates duplicate interval models.

* The djcelery admin templates were not included in the distribution.

.. _version-2.2.1:

2.2.1
=====

:release-date: 2011-02-02 16:00 PM CET

* Should now work with Django versions previous to 1.2.

.. _version-2.2.0:

2.2.0
=====
:release-date: 2011-02-01 10:00 AM CET

* Now depends on Celery v2.2.0

* djceleryadm: Adds task actions Kill and Terminate task

* celerycam: Django's queryset.delete() fetches everything in
  memory THEN deletes, so we need to use raw SQL to expire objects.

* djcelerymon: Added Command.stdout + Command.stderr  (Issue #23).

* Need to close any open database connection after any embedded
  celerybeat process forks.

* Added contrib/requirements/py25.txt

* Demoproject now does ``djcelery.setup_loader`` in settings.py.

.. _version-2.1.1:

2.1.1
=====
:release-date: 2010-10-14 02:00 PM CEST

* Now depends on Celery v2.1.1.

* Snapshots: Fixed bug with losing events.

* Snapshots: Limited the number of worker timestamp updates to once every second.

* Snapshot: Handle transaction manually and commit every 100 task updates.

* snapshots: Can now configure when to expire task events.

    New settings:

    * ``CELERYCAM_EXPIRE_SUCCESS`` (default 1 day),
    * ``CELERYCAM_EXPIRE_ERROR`` (default 3 days), and
    * ``CELERYCAM_EXPIRE_PENDING`` (default 5 days).

* Snapshots: ``TaskState.args`` and ``TaskState.kwargs`` are now
  represented as ``TextField`` instead of ``CharField``.

    If you need to represent arguments larger than 200 chars you have
    to migrate the table.

* ``transaction.commit_manually`` doesn't accept arguments on older
  Django version.

    Should now work with Django versions previous to v1.2.

* The tests doesn't need :mod:`unittest2` anymore if running on Python 2.7.

.. _version-2.1.0:

2.1.0
=====
:release-date: 2010-10-08 12:00 PM CEST

Important Notes
---------------

This release depends on Celery version 2.1.0.
Be sure to read the Celery changelog before you upgrade:
http://celery.github.com/celery/changelog.html#version-2-1-0

News
----

* The periodic task schedule can now be stored in the database and edited via
  the Django Admin interface.

    To use the new database schedule you need to start ``celerybeat`` with the
    following argument::

        $ python manage.py celerybeat -S djcelery.schedulers.DatabaseScheduler

    Note that you need to add your old periodic tasks to the database manually
    (using the Django admin interface for example).

* New Celery monitor for the Django Admin interface.

    To start monitoring your workers you have to start your workers
    in event mode::

        $ python manage.py celeryd -E

    (you can do this without restarting the server too::

        >>> from celery.task.control import broadcast
        >>> broadcast("enable_events")

    You need to do a syncdb to create the new tables:

        python manage.py syncdb

    Then you need to start the snapshot camera::

        $ python manage.py celerycam -f 2.0

    This will take a snapshot of the events every 2 seconds and store it in
    the database.

Fixes
-----

* database backend: Now shows warning if polling results with transaction isolation level
  repeatable-read on MySQL.

    See http://github.com/celery/django-celery/issues/issue/6

* database backend: get result does no longer store the default result to
  database.

    See http://github.com/celery/django-celery/issues/issue/6

2.0.2
=====

Important notes
---------------

* Due to some applications loading the Django models lazily, it is recommended
  that you add the following lines to your ``settings.py``::

       import djcelery
       djcelery.setup_loader()

    This will ensure the Django celery loader is set even though the
    model modules haven't been imported yet.

News
----

* ``djcelery.views.registered_tasks``: Added a view to list currently known
  tasks.

2.0.0
=====
:release-date: 2010-07-02 02:30 P.M CEST

* Initial release
