MoveMe
======

MoveMe is a project that provides NextBus transportation data over a RESTful
web service in various formats.


Installation
------------

You will need the following repositories in order to get the project running:

- [Python 2.6.x][pytn]
- [VirtualEnv][venv] (recommended)

*NOTE: Python 3.x may work, but is currently untested*

After having installed these depedencies, clone this project:

```sh
git clone https://github.com/monokrome/MoveMe
```

You should now be able to run the following commands within the newly created
`MoveMe` directory:

```sh
virtualenv --distribute .
source bin/activate
./manage.py syncdb --migrate
./manage.py runserver
```

*NOTE: Don't forget to `source bin/activate` to use the virtual environment.*


Developing
----------

Development of this project follows the same process as documented in the
**Installation** section with the following additional steps:

- It is recommended to use `./manage.py runserver_plus` for running the server.
- It is recommended to set `MOVEME_ENV=development` in your environment.

An example command to run a server in development would be:

```sh
MOVEME_ENV=development ./manage.py runserver_plus

```

If preferred, you can set MOVEME_ENV globally in bash by running the following
command and then restarting your terminal instead of typing it every time:

```sh
echo 'MOVEME_ENV=development' >> ~/.bashrc

```

Potential Enhancements
----------------------

The following trade-offs were made in order to minimize development time, but
would be good to reconsider if the project were to grow substantially:

- Consistent error responses
- Centralized error message strings text for localization/internationalization
- Tests have been omitted, but really should exist.
- Pagination would be nice, but has been omitted.
- nextbus.py could be made more DRY by leveraging common naming conventions
- Caching would be nice


[pytn]: https://python.org
[venv]: https://virtualenv.pypa.io/en/latest/

