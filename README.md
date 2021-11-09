# Bevendo

A Django/React companion app to "[Drinking with the Saints]".

Django layout is based off of the [Django Twoscoops Project].

[django twoscoops project]: https://github.com/twoscoops/django-twoscoops-project/
[drinking with the saints]: https://drinkingwiththesaints.com/

# Testing

Running unittests:

    bevendo_project$ bevendo/manage.py test

Running unitests with coverage:

    bevendo_project$ coverage run --source='.' bevendo/manage.py test
    bevendo_project$ coverage run --source='.' bevendo/manage.py test api
    bevendo_project$ coverage report

## Links

    https://docs.python.org/3/library/unittest.html#unittest.TestCase
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
