# Changelog

## v0.7.0 (09/05/2019)

### Minor but breaking changes to daptics client

API changes in `daptics_client.py`:

* added `remaining` and `completed` attributes that can be read to determine
  whether to proceed with design generations.
* added `finalize_campaign` method to be used after all generations are finished (e.g. when
  `remaining` equals zero). A "finalize" task is created by this method, and it
  can be polled for a result, just like the "space" and "generate" tasks.
* added `error_messages` method to nicely format GraphQL error messages from response.
* BREAKING - changed return value of `poll_for_current_task` method, so that errors can be
  inspected.
* BREAKING - changed return value of `call_api` method, so that errors can be inspected.
* BREAKING - changed order of arguments in `export_csv` method (so that all "export" and "save"
  csv methods now take `fname` as their first argument).
* BREAKING - changed order of arguments in `save_experimental_and_space_parameters_csv` method
  (so that all "export" and "save" csv methods now take `fname` as their first argument).

Notebook changes:

Changed argument and return values as required, for the `poll_for_current_task`, `export_csv`,
and `save_experimental_and_space_parameters_csv` calls.


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
