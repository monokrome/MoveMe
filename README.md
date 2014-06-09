MoveMe
======

MoveMe is a project that provides Muni / BART transportation data over a
RESTful web service in various formats.


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


[pytn]: https://python.org
[venv]: https://virtualenv.pypa.io/en/latest/

