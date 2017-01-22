# pypers

Brower your [Papers.app](http://papersapp.com/) library from your web browser. You can now access your papers from non-MacOS computers.


## Caveats

* Read-only (no risk to corrupt your Papers.app database)
* Only tested with Papers 3.4.7 (may break in future releases)
* More useful when Dropbox sync is enabled in Papers


## How it works

The app finds the compressed sqlite database in `~/Dropbox/Library.papers3/` (by default), loads it using pandas, and populates the django database with it. To update the database you can delete it and reimport it.


## Installation

* Dependencies: Python 3, django, pandas
* git clone the repo
* Update `PAPERS_LIBRARY_PATH` in `pypers/settings.py` if necessary
* `make migrate` to import the Papers library into pypers
* `make serve`
* go to `http://localhost:8000/admin/`
* Default username/password: `admin/admin`
