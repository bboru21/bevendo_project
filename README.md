# Bevendo

A Django/React companion app to "[Drinking with the Saints]".

Django layout is based off of the [Django Twoscoops Project].

# Testing

Running unittests:

    bevendo_project$ bevendo/manage.py test

Running unitests with coverage:

    bevendo_project$ coverage run --source='.' bevendo/manage.py test
    bevendo_project$ coverage run --source='.' bevendo/manage.py test api
    bevendo_project$ coverage report

## Testing Links

    [Python Unittest TestCase]
    [Django Testing]

# Floating Feast Days

As there are many feasts and seasons that whose dates are not set in stone but vary from year to year, a third party Liturgical calendar source must be used. To that end, I've integrated the app with the [Calapi Inadiutorium API], which seems to be a pretty great resouce thus far. Data is cached in the database via the import_calapi_inadiutorium_data management command.

    (venv) bevendo_project$ python bevendo/manage.py import_calapi_inadiutorium_data --settings bevendo.settings.local --month 12 --year 2021
    (venv) bevendo_project$ python bevendo/manage.py import_calapi_inadiutorium_data --settings bevendo.settings.local --year 2022
    (venv) bevendo_project$ python bevendo/manage.py import_calapi_inadiutorium_data --settings bevendo.settings.local # defaults to next year

[django twoscoops project]: https://github.com/twoscoops/django-twoscoops-project/
[drinking with the saints]: https://drinkingwiththesaints.com/
[calapi inadiutorium api]: http://calapi.inadiutorium.cz/
[python unittest testcase]: https://docs.python.org/3/library/unittest.html#unittest.TestCase
[django testing]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
