# Changelog

## v0.6.0 (17/04/2019)

### Improved handling of exceptions and tasks

API changes in `daptics_client.py`:

* Wrapped all GraphQL calls in `call_api` method to trap exceptions
* Added `print` method
* Added `wait_for_current_task` method
* Removed `demo` argument from `create_session` method

Notebook changes:

* `03_SimpleTutorial.ipynb` substantially reworked to take advantage of
`wait_for_current_task` API, and more documentation added.

---

## v0.5.1 (02/04/2019)

### get_analytics fix, more examples

API changes in `daptics_client.py`:

* Added `list_sessions` method
* Changed interface for `get_analytics` method
* Documented timeout defaults for each method
* Better documentation for `simulate_experiment_responses` method
* Better documentation for `simulate_experiment_responses_csv` method

Added two more interactive notebooks:

* `04_GetAnalytics.ipynb` - Testing `get_analytics` method
* `05_RestartSession.ipynb` - Example of connecting to existing session

---

## v0.5.0 (29/03/2019)

### First release of public repository

Initial public API release with Python client and interactive notebook:

* `daptics_client.py` - Python GraphQL client with persistence
* `03_SimpleTutorial.ipynb` - notebook that uses client to demonstrate basic functions
