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


Usage
-----

The following public endpoints are provided by the hosted web service:


 Resource | Endpoint    | Description                                   
----------|-------------|-----------------------------------------------
 Agency   | /agency/    | A listing of all transportation agencies.     
 Route    | /route/     | Information about routes at an agency.        
 Message  | /message/   | Status messages about routes at an agency.    
 Schedule | /schedule/  | Schedules for different routes at an agency.  
 Vehicle  | /vehicle/   | A listing of vehicles on a given route.       


*NOTE:* The predictions API is not yet supported but is being planned.


### Agency

Does not accept any filters. Provides the following endpoints:

- List all agencies: http://localhost:8000/agency/

### Route

Requires an `agency` filter which should be set to the tag of whichever agency
this route belongs to.

- List all routes for a 'sf-muni': http://localhost:8000/route/?agency=sf-muni
- Details for `sf-muni` route `F`: http://localhost:8000/route/F/?agency=sf-muni

### Message

Requires an `agency` filter which should be set to the tag of whichever agency
the messages belong to.

- List all message IDs for 'sf-muni': http://localhost:8000/message/?agency=sf-muni
- Messages for `sf-muni` route `F`: http://localhost:8000/message/F/?agency=sf-muni

### Schedule

Requires an `agency` filter which should be set to the tag of whichever agency
the messages belong to.

- List all possible schedules for `sf-muni`: http://localhost:8000/schedule/?agency=sf-muni
- Schedule details for `sf-muni` route `F`: http://localhost:8000/schedule/?agency=sf-muni

### Vehicle

Requires an `agency` filter which should be set to the tag of whichever agency
the messages belong to. Requires a `route` filter to filter by specific routes.

Optionally accepts a `time` filter, which will filter results to only show
vehicles which have changed in `time` seconds.

- List all active vehicles for `sf-muni` route `F`: http://localhost:8000/vehicle/?agency=sf-muni&route=F


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

- Caching would be nice for resources which don't change often.
- Consistent error responses with i18n & localization
- Tests have been omitted since this is a prototype.
- Pagination would be nice, but has been omitted.


[pytn]: https://python.org
[venv]: https://virtualenv.pypa.io/en/latest/

