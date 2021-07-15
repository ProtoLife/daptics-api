# Changelog

## v0.12.0 (15/07/2021)

* Updated URL to new server (v0.14) at https://api.daptics.ai, with new
task API for "create", "update" and "analytics" tasks.
* GraphQL schema breaking changes:
    ❌ Type `Loadavg` was removed
    ❌ Type `SessionAuth` was removed
    ❌ Type `FinalizeTaskResult` was removed
    ❌ Type `Server` was removed
    ❌ Input Field `passwordConfirmation` removed from input type `NewUserInput`
    ❌ Field `regDate` was removed from object type `User`
    ❌ Field `finalizeCampaign` was removed from object type `RootMutationType`
    ❌ Field `saveSessionParameters` was removed from object type `RootMutationType`
    ❌ Field `verifyUser` was removed from object type `RootMutationType`
    ❌ Field `saveExperiments` was removed from object type `RootMutationType`
    ❌ `RootMutationType.createAnalytics` type changed from `Analytics` to `Task`
    ❌ Field `userLevel` was removed from object type `UserSummary`
    ❌ Field `regDate` was removed from object type `UserSummary`
    ❌ Field `regDate` was removed from object type `UserCreated`
    ❌ Field `startedAt` was removed from object type `Session`
    ❌ Field `path` was removed from object type `Session`
    ❌ Field `restartedAt` was removed from object type `Session`
    ❌ `Session.auth` type changed from `SessionAuth` to `AuthenticationToken`
    ❌ Field `path` was removed from object type `SessionSummary`
    ❌ Field `campaign` was removed from object type `SessionSummary`
    ❌ Field `params` was removed from object type `SessionSummary`
    ❌ Field `user` was removed from object type `SessionSummary`
    ❌ Field `server` was removed from object type `RootQueryType`
    ❌ Field `servers` was removed from object type `RootQueryType`
    ❌ Removed argument `includeArchivedTasks` from `RootQueryType.tasks`
    ❌ Field `regDate` was removed from object type `UserProfile`
    ❌ Input Field `type: String!` was added to input type `ExperimentsInput`
    ❌ Input Field `passwordConfirmation` removed from input type `ChangePasswordInput`
    ❌ Union member `FinalizeTaskResult` was removed from `TaskResult` Union type
    ❌ Schema subscription root has changed from `None` to `RootSubscriptionType`
* Dangerous changes:
    ⚠️ Union member `AnalyticsTaskResult` was added to `TaskResult` Union type
    ⚠️ Union member `UpdateTaskResult` was added to `TaskResult` Union type
    ⚠️ Union member `CreateTaskResult` was added to `TaskResult` Union type
* Non-breaking changes:
    ✔️ Type `SchemaChange` was added
    ✔️ Type `SchemaVersionInfo` was added
    ✔️ Type `RootSubscriptionType` was added
    ✔️ Type `SessionUpdated` was added
    ✔️ Type `AnalyticsTaskResult` was added
    ✔️ Type `UpdateSessionInput` was added
    ✔️ Type `CreateTaskResult` was added
    ✔️ Type `UpdateTaskResult` was added
    ✔️ Field `confirmedAt` was added to object type `User`
    ✔️ Field `lastActiveSession` was added to object type `User`
    ✔️ Field `termsVersionAgreed` was added to object type `User`
    ✔️ Field `disabledAt` was added to object type `User`
    ✔️ Field `registeredAt` was added to object type `User`
    ✔️ Field `path` was added to object type `CategorizedError`
    ✔️ Field `gen` was added to object type `TaskSummary`
    ✔️ Field `archived` was added to object type `TaskSummary`
    ✔️ Field `putExperimentalParameters` was added to object type `RootMutationType`
    ✔️ Field `confirmUser` was added to object type `RootMutationType`
    ✔️ Field `agreeToTerms` was added to object type `RootMutationType`
    ✔️ Field `generateDesign` was added to object type `RootMutationType`
    ✔️ Field `putExperiments` was added to object type `RootMutationType`
    ✔️ Field `updateSession` was added to object type `RootMutationType`
    ✔️ Field `lastActiveSession` was added to object type `UserSummary`
    ✔️ Field `registeredAt` was added to object type `UserSummary`
    ✔️ Field `termsVersionAgreed` was added to object type `UserSummary`
    ✔️ Field `registeredAt` was added to object type `UserCreated`
    ✔️ Field `lastStartedAt` was added to object type `Session`
    ✔️ Field `designedExperimentsCount` was added to object type `Session`
    ✔️ Field `extraExperimentsCount` was added to object type `Session`
    ✔️ Field `totalCost` was added to object type `Session`
    ✔️ Field `parameterCount` was added to object type `SessionSummary`
    ✔️ Field `totalCost` was added to object type `SessionSummary`
    ✔️ Field `userId` was added to object type `SessionSummary`
    ✔️ Field `lastStartedAt` was added to object type `SessionSummary`
    ✔️ Field `spaceType` was added to object type `SessionSummary`
    ✔️ Field `gen` was added to object type `SessionSummary`
    ✔️ Field `designedExperimentsCount` was added to object type `SessionSummary`
    ✔️ Field `extraExperimentsCount` was added to object type `SessionSummary`
    ✔️ Field `designCost` was added to object type `SessionSummary`
    ✔️ Field `gen` was added to object type `Task`
    ✔️ Field `clientCompatibility` was added to object type `RootQueryType`
    ✔️ Argument `active: Boolean` added to `RootQueryType.sessions`
    ✔️ Argument `demo: Boolean` added to `RootQueryType.sessions`
    ✔️ Argument `includeArchived: Boolean` added to `RootQueryType.tasks`
    ✔️ Field `termsVersionAgreed` was added to object type `UserProfile`
    ✔️ Field `updatedAt` was added to object type `UserProfile`
    ✔️ Field `status` was added to object type `UserProfile`
    ✔️ Field `registeredAt` was added to object type `UserProfile`


## v0.9.3 (23/01/2020)

* Bug fix for _auto_task method.
* https://api-alpha.daptics.ai is now the API server URL

### Breaking changes to daptics client

Changes in `daptics_client.py`:

* Better return value from get_all_analytics_files


## v0.9.2 (17/01/2020)

Better documentation using mkdocs and pdoc3.

### Breaking changes to daptics client

Changes in `daptics_client.py`:

* export_experimental_space_csv no longer has a timeout argument

### Non-breaking changes

Changes in `daptics_client.py`:

* Fixed export_csv bugs for auto exports
* No other code changes

Changes in notebooks:

* Added 06_AutomationWorkflow.ipynb


## v0.9.1 (25/09/2019)

### Non-breaking changes

Changes in `daptics_client.py`:

* Fixed pydocmd-markdown errors
* No code changes

Changes in notebooks:

* Fixed incorrect localhost URL in 03_SimpleTutorial.ipynb


## v0.9.0 (10/09/2019)

### Breaking changes to daptics client

Changes in `daptics_client.py`:

* New error classes added
* New `DapticsTaskType` and `DapticsExperimentsType` enumerations added

Changes to DapticsClient class attributes:

* New `auto_export_path` option added that automatically saves generated CSV files
* New `auto_generate_next_design` option added to allow manual control of
when designs are generated
* New `auto_task_timeout` option added to allow manual control of polling of
active tasks
* New `credentials` and `session_path` attributes added
* New `task_info` attribute replaces removed `current_task` attribute

Changes to DapticsClient methods:

* Constructor - A new `config` argument was added to `DapticsClient` constructor,
to allow for easier configuration from a JSON file. If `config` is not provided,
configuration parameters may also be read from environment variables. See the
documentation in `daptics_client.py` for more information.
* `login` method - If no email or password arguments are supplied, use the values
from the `credentials` attribute.
* `get_experiments` method - a `design_only` argument was added, so that users
can request just the designed experiments for a particular generation, without
previously submitted responses or extra experiments
* New `get_experimental_space` and `get_generated_design` convenience methods added
* New `generate_design` method was added to give users manual control of the
design generation process, either when the user has no initial experiments, or
when the `auto_generate_next_design` option is disabled.
* New `put_experimental_parameters` and `put_experimental_parameters_csv` methods replace
the removed `save_experimental_and_space_parameters...` methods, and the key for the
GraphQL data result was renamed to `putExperimentalParameters`. The new `auto_task_timeout`
option can be used to block until a result has been received.
* New `put_experiments` and `put_experiments_csv` methods replace
the removed `save_initial_experiments...` and `save_experiment_responses...` methods,
and the key for the GraphQL data result was renamed to `putExperiments`.
The new `auto_generate_next_design` option can be used to start a "generate" task
after the experiments have been saved, and the new `auto_task_timeout` option can then
be used to wait until the next generation design result has been received.
* New `get_analytics_file_list` method replaces removed `get_analytics` method
* New `get_analytics_file` and `get_all_analytics_files` methods replace the removed
`save_analytics_file` and `save_all_analytics_files` methods.

Notebook changes:




## v0.7.3 (30/07/2019)

### Non-breaking change to daptics client

API changes in `daptics_client.py`:

* `restore_session` method now correctly sets `design` attribute
* `save_analytics_file` and `save_all_analytics_files` use required authorization token in
get query string, per changes in server functionality
* other minor bug fixes

Notebook changes:

None.


## v0.7.2 (22/05/2019)

### Non-breaking change to daptics client

API changes in `daptics_client.py`:

* added `halt_session` method to fully disconnect from connected session.

Notebook changes:

None.


## v0.7.1 (15/05/2019)

### Minor but breaking changes to daptics client

API changes in `daptics_client.py`:

* added `remaining` and `completed` attributes that can be read to determine
  whether to proceed with design generations.
* added `experiments_history` attribute
* added `finalize_campaign` method to be used after all generations are finished (e.g. when
  `remaining` equals zero). A "finalize" task is created by this method, and it
  can be polled for a result, just like the "space" and "generate" tasks.
* added `start_simulation` and `start_simulation_csv` methods to run an automated
  simulation of a campaign for an arbitrary experimental space and number of generations.
* added `get_experiments_history` and `export_experiments_history_csv` methods to
  retrieve all the experiments in the session and save them to a CSV file.
* added a `save_all_analytics_files` method to create and save all the available analytics
  files to a specified location.
* augmented the `poll_for_current_task` method to handle the new "finalize" and "simulate"
  task types.
* added an `error_messages` method to nicely format GraphQL error messages from response.
* BREAKING - changed return value of `poll_for_current_task` method, so that errors can be
  inspected.
* BREAKING - changed return value of `call_api` method, so that errors can be inspected.
* BREAKING - changed order of arguments in `export_csv` method (so that all "export" and "save"
  csv methods now take `fname` as their first argument).
* BREAKING - changed order of arguments in `save_experimental_and_space_parameters_csv` method
  (so that all "export" and "save" csv methods now take `fname` as their first argument).
* BREAKING - removed the `gen` argument from the `get_analytics` method, which always
  returns analytics for all the generations in a session.
* BREAKING - renamed the `get_analytics_file` to `save_analytics_file`.

Notebook changes:

Changed method names, arguments and return values as required, for the `save_analytics_file`,
`poll_for_current_task`, `export_csv`, and `save_experimental_and_space_parameters_csv` calls.


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
