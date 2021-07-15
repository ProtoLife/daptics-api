---
description: |
    API documentation for modules: daptics_client, daptics_client.daptics_client.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...




    
## Sub-modules

* [daptics_client.daptics_client](#daptics_client.daptics_client)





# Python API Client

See comments and docstrings for the DapticsClient class in the code below
for suggestions for using this class. For additional help or information,
please visit or contact daptics:

* On the web at <a href="https://daptics.ai"><https://daptics.ai>
* By email at [support@daptics.ai](mailto:support@daptics.ai)

Daptics API Version 0.12.0
Copyright (c) 2021 Daptics Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), the
rights to use, copy, modify, merge, publish, and/or distribute, copies of
the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

You do not have the right to sub-license or sell copies of the Software.

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.




    
## Functions


    
### Function `can_set_result`



    
> `def can_set_result(future)`


Helper function to see if a future is done or canceled.

    
### Function `log_task_coroutine`



    
> `async def log_task_coroutine(task, **kwargs)`


A useful coroutine (callback) that can be be called asynchronously if the
"run_tasks_async" option has been set in the client. This coroutine logs
progress information to a file named <code>daptics\_task.log</code> in the current directory.


    
## Classes


    
### Class `CsvFileEmptyError`



> `class CsvFileEmptyError(fname)`


An error raised if there were no rows that could be read from the specified CSV file.





    
### Class `CsvNoDataRowsError`



> `class CsvNoDataRowsError(fname)`


An error raised if there were no rows after the header row that could be read from
the specified CSV file.





    
### Class `DapticsClient`



> `class DapticsClient(host=None, config=None)`


A Python GraphQL client for maintaining the state of a Daptics optimization session.
Between API invocations, data such as the user id, access token, session id,
last generated design, etc. are retained in the object's attributes.

host (str):
    The host part of the API endpoint, as read from configuration, or set manually
    prior to calling <code>connect</code>.

config (str):
    File path to a JSON configuration file, used to read the host, login credentials and
    runtime options. Defaults to <code>daptics.conf</code>. The items in the JSON file are:

<code>host</code> - host part of the API endpoint

<code>user</code> - email of the database user to login with

<code>password</code> - password for the database user to login with

<code>auto\_export\_path</code> - see <code>options</code> below

<code>auto\_generate\_next\_design</code> - see <code>options</code> below

<code>auto\_task\_timeout</code> - see <code>options</code> below

<code>run\_tasks\_async</code> - see <code>options</code> below

<code>verify\_ssl\_certificates</code> - see <code>options</code> below

If `config is set to None, configuration can be read from OS environment
variables, if they exist. The environment variable names are:

<code>DAPTICS\_HOST</code> - host part of the API endpoint

<code>DAPTICS\_USER</code> - email of the database user to login with

<code>DAPTICS\_PASSWORD</code> - password for the database user to login with

<code>DAPTICS\_AUTO\_EXPORT\_PATH</code> - see <code>options</code> below

<code>DAPTICS\_AUTO\_GENERATE\_NEXT\_DESIGN</code> - see <code>options</code> below

<code>DAPTICS\_AUTO\_TASK\_TIMEOUT</code> - see <code>options</code> below

<code>DAPTICS\_RUN\_TASKS\_ASYNC</code> - see <code>options</code> below

<code>DAPTICS\_VERIFY\_SSL\_CERTIFICATES</code> - see <code>options</code> below

options (dict):
    A Python <code>dict</code> containing runtime options. As of this version, there
    are four available options:

<code>auto\_export\_path</code> - If not None, a string indicating the relative or absolute directory
where the validated experimental space and generated design files will be saved,
so that the user will not have to explicitly call the <code>export</code> functions.

<code>auto\_generate\_next\_design</code> - If set (True), uploading (initial or later) experiment responses
will automatically start a <code>generate</code> task for the next design generation. If not set
(None or False), the uploading will only validate the responses, and the user
will have to call the <code>generate</code> task manually after a successful validation.

<code>auto\_task\_timeout</code> - If set to a positive number indicating the
number of seconds to wait, this option will immediately start to wait on a
just-created task, so that the user will not have to explicitly call
<code>poll\_for\_current\_task</code> or <code>wait\_for\_current\_task</code>. Setting this option to a negative
number, means to wait indefinitely. Setting the option to zero will poll the task
just once. The default, None, means that the user wants to explicitly call
<code>poll\_for\_current\_task</code> or <code>wait\_for\_current\_task</code>.

<code>run\_tasks\_async</code> - If set (True), methods that start long-running tasks
(<code>put\_experimental\_parameters</code>, <code>put\_experiments</code>, <code>generate\_design</code>, <code>run\_simulation</code>,
and <code>create\_analytics</code>) will be run in an asynchronous event loop. Normally
you will only set this flag if you want to receive progress information via
a coroutine (callback) function.

<code>verify\_ssl\_certificates</code> - If set (True), strict checking of
the validity of the API server's SSL certificates will be done when the
<code>connect</code> method is called. Set this to False, with extreme caution, to
disable this check.


    
#### Class variables


    
##### Variable `DEFAULT_CONFIG`

The default location for the option configuration file.

    
##### Variable `REQUIRED_SPACE_PARAMS`

The names of required experimental space parameters.

    
##### Variable `TASK_FRAGMENT`




    
#### Instance variables


    
##### Variable `analytics`

A Python <code>dict</code> containing information and links to available analytics files,
as updated by the result of a "analytics" task.

    
##### Variable `api_url`

The full API endpoint URL.

    
##### Variable `auth`

A <code>requests.auth</code> object used to insert the required authorization
header in API requests. The auth object's <code>token</code> attribute is set by the <code>login</code> method.

    
##### Variable `client_version`

The version number of this client.

    
##### Variable `completed`

A boolean indicating whether the design space has been completely explored.

    
##### Variable `config`

The file path to the JSON configuration file used to read the host, login credentials and
runtime options.

    
##### Variable `credentials`

A tuple of (<code>username</code>, <code>password</code>), as read from configuration, or set manually
prior to calling <code>login</code>.

    
##### Variable `design`

A Python <code>dict</code> containing the current generated design, as updated by the
result of a "generate" task.

    
##### Variable `experiments_history`

A list of Python <code>dict</code>s containing all the experiments and responses that
have been simulated, as updated by the result of a "simulate" task.

    
##### Variable `gen`

An integer storing the current design "generation number" for the session.
This is -1 for a new session, 0 when the session's experimental space has been
validated, and greater than zero when a design has been generated by the system.

    
##### Variable `gql`

The <code>gql.Client</code> object used to make GraphQL requests to the API.

    
##### Variable `host`

The host part of the API endpoint, as read from configuration, or set manually
prior to calling <code>connect</code>.

    
##### Variable `initial_params`

A Python <code>dict</code> containing the experimental space parameters defaults as
initially returned by the <code>create\_session</code> method.

    
##### Variable `options`

A Python <code>dict</code> containing the runtime options.

    
##### Variable `pp`

A <code>pprint.PrettyPrinter</code> object used for printing Python <code>dict</code>s.

    
##### Variable `remaining`

If not None, an integer representing the number of possible generations that
can be generated until the entire design space has been explored.

    
##### Variable `session_id`

The session id for a connected Daptics session, as set by the <code>create\_session</code> method.

    
##### Variable `session_name`

The name of the connected Daptics session, as set by the <code>create\_session</code> method.

    
##### Variable `session_tag`

The tag (a read-only identifier) of the connected Daptics session, as set by the <code>create\_session</code> method.

    
##### Variable `task_info`

A Python <code>dict</code> that holds information about the polling status for
running tasks in the session.

    
##### Variable `task_updated_coroutine`

A user-specified coroutine (callback) that will be called with information
on task progress.  The coroutine will be called with a Python <code>dict</code> containing
<code>progress</code> and <code>status</code> items. Optional keyword arguments that the coroutine
will receive can be specified by setting the client's <code>task\_updated\_kwargs</code>
attribute.

If you supply a coroutine, the coroutine MUST be defined as <code>async</code>
and MUST return a boolean value. The return value of your coroutine
indicates whether you wish to continue receiving the callback for the
current task. Generally, you should return <code>False</code> if the <code>status</code>
value of the task does not have the value "running", meaning that the
the task has completed or failed.

Here's a simple example of a coroutine. See the code for <code>[log\_task\_coroutine()](#daptics\_client.daptics\_client.log\_task\_coroutine)</code>
in this module for another example.

```
async def my_coroutine(task, **kwargs):
    if 'progress' in task:
        print(task['progress']['message'])

    if task['status'] == 'running':
        # Return True to continue receiving callbacks
        return True

    # Return False to stop receiving callbacks
    return False
```

    
##### Variable `task_updated_kwargs`

User-specified keyword dictionary to be passed to the async task updated coroutine.

    
##### Variable `user_id`

The user id for the authenticated user, set by the <code>login</code> method.

    
##### Variable `validated_params`

A Python <code>dict</code> containing the experimental space parameters as updated
from the result of a "space" task.

    
##### Variable `websocket_url`

The full websocket endpoint URL.



    
#### Methods


    
##### Method `call_api`



    
> `def call_api(self, document, vars, timeout=None)`


Performs validation on the GraphQL query or mutation document and then
executes the query, returning both the <code>data</code> and <code>errors</code> items from the JSON
response.

##### Arguments
document (str):
    The GraphQL query document, as a string.

vars (dict):
    A python 'dict' containing the variables for the query.

timeout (float, optional):
    The maximum number of seconds to wait before a response is returned.

##### Returns
data (dict):
    The <code>data</code> item of the GraphQL response, a Python <code>dict</code> with an
    item whose key is the GraphQL query name for the request.

errors (list):
    The <code>errors</code> item of the GraphQL response. Each item in the list
    is guaranteed to have a <code>message</code> item.

##### Notes
Either <code>data</code> or <code>errors</code> may be <code>None</code>. Exceptions encountered during the
request are converted into an item in the <code>errors</code> list.

    
##### Method `check_api_compatibility`



    
> `def check_api_compatibility(self)`


Checks the version of this client against the requirements of
the api at the connected host.

##### Returns
dict containing <code>minimumClientVersion</code> and compatibility information.

##### Raises
Exception if the (older) API does not support checking version 
compatibility.

    
##### Method `connect`



    
> `def connect(self)`


Reads and processes client configuration, and instantiates the client if it has not
been done before. Creates an HTTP transport instance from the client's
<code>api\_url</code> attribute, and attempts to connect to the introspection interface.
The <code>gql.Client</code> value is stored in the client's <code>gql</code> attribute.

##### Returns
Nothing

##### Raises
IncompatibleApiError
    If the API at <code>self.host</code> requires a higher client version number.

MissingConfigError
    If the config file specified does not exist.

InvalidConfigError
    If the config file specified cannot be parsed, or does not have a 'host'
    value.

NoHostError
    If there is no config file specifed and no host has been set.

requests.exceptions.ConnectionError
    If the connection cannot be made.

    
##### Method `create_session`



    
> `def create_session(self, name, description)`


Creates a new daptics session.

##### Arguments
name (str):
    The unique name for the session among the authenticated user's sessions.

description (str):
    A description for the session.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>createSession</code> item.

##### Notes
On successful creation, the session id, session name and
initial parameters are stored in the client's attributes.

    
##### Method `download_all_analytics_files`



    
> `def download_all_analytics_files(self, analytics, directory='.', name_by_gen=False)`


Processes the result of an "analytics" task for all the available analytics
by downloading the contents of each file, and saving them to the specified directory.

For each file, download its contents and save it in the specified directory.

##### Arguments
analytics (dict):
    The <code>analytics</code> <code>dict</code> from the results of an "analytics" task, with <code>gen</code>,
    and <code>files</code> items.  You can use <code>self.analytics</code> to use the most recent
    analytics results.

directory (str, optional):
    If supplied, the target directory to save the files to. If the directory
    does not exist, attempt to create it.

name_by_gen (bool, optional):
    If true, <code>auto\_genN\_</code> will be prefixed to each file name.

##### Returns
file_count (int):
    The number of files created.

##### Raises
PermissionError
     If the user does not have permission to create directories or files in the specified
     directory.

    
##### Method `download_analytics_file`



    
> `def download_analytics_file(self, file_url, fname)`


Gets the contents of an analytics file. Once a URL to a particular analytics file
has been obtained from the result of an "analytics" task, specify the <code>url</code> and <code>filename</code>
values from the result as the arguments to this convenience method to request the file's
contents over HTTP, submitting a request with the authentication token that
was stored in the client.

##### Arguments
url (str):
    The URL for the file, as returned from the result of an "analytics" task.

fname (str):
    Save the file's contents to this file system location.
    The directory that the file will be created in must exist
    and the user must have permission to create files in that directory.

##### Returns
response (<code>requests.Response</code>)
    The <code>requests</code> library's <code>response</code> object for the authenticated HTTP request.

##### Raises
PermissionError
     If the user does not have permission to create a file at the specified
     file system location.

    
##### Method `download_url_and_params`



    
> `def download_url_and_params(self, url)`


Strips the query string from the given url, then checks to see if
there is a 'token' entry in it. If not, uses the client's authentication 
token if it exists.

##### Arguments
url (str):
    The download url, usually with query string containing an encrpyted token.

##### Returns
(url, params):
    A 2-tuple containing the url minus the query string, and a params
    Python dictionary, containing the token.

    
##### Method `error_messages`



    
> `def error_messages(self, errors)`


Extracts the <code>message</code> values from the <code>errors</code> list returned in a GraphQL response.

##### Arguments
errors (list):
    The list of GraphQL errors. Each error must have a <code>message</code> value, and
    can optionally have <code>key</code>, <code>path</code> and <code>locations</code> values.

##### Returns
message (str or list):
    The message (or messages) extracted from the GraphQL response.

    
##### Method `execute_query`



    
> `def execute_query(self, document, vars, timeout=None)`


Performs validation on the GraphQL query or mutation document and then
executes the query. Converts errors returned by <code>gql</code> into <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code>
errors.

##### Arguments
document (str):
    The GraphQL query document, as a string.

vars (dict):
    A python 'dict' containing the variables for the query.

timeout (float, optional):
    The maximum number of seconds to wait before a response is returned.

##### Returns
data (dict):
    The <code>data</code> item of the GraphQL response, a Python <code>dict</code> with an
    item whose key is the GraphQL query name for the request.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

    
##### Method `experiment_with_random_response`



    
> `def experiment_with_random_response(self, experiment, max_response_value)`


Uses a random number generator to generate a numerical response value
in the range [0, n] and then replaces any existing response value with
the generated value.

##### Arguments
experiment (list):
    A list of values representing an experiment, including a (possibly
    empty) response value.

max_response_value (float):
    The maximum random response value to be generated for the experiment.

##### Returns
experiment (list):
    The list of parameter values for the specified experiment, and a generated
    response value. Each value is encoded as a string.

    
##### Method `experiments_table_column_names`



    
> `def experiments_table_column_names(self, space)`


Generates the required header for the experiments table, including the
names of each parameter in the experimental space, and the reserved name
"Response" for the experiment response value.

##### Arguments
space (dict):
    A Python <code>dict</code> that defines the experimental space.

##### Returns
column_headers (list):
    The list is made up from the names of all parameters, and the additional
    string "Response".

    
##### Method `experiments_table_template`



    
> `def experiments_table_template(self, space)`


Generates the column header for the experiments table, with no data
rows. Can be used to export an empty experiments table template CSV file,
or to submit "empty" initial experiments.

##### Arguments
space (dict):
    A Python <code>dict</code> that defines the experimental space.

##### Returns
table (dict):
    A Python <code>dict</code> with with a <code>colHeaders</code>
    item containing the column header row, and an empty <code>data</code> list item.

    
##### Method `export_csv`



    
> `def export_csv(self, fname, table, headers=True)`


Writes an experimental space or experiments table to a CSV file on disk.

##### Arguments
fname (str):
    The filesystem path where the file will be written.

table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> items, representing an
    experimental space or experiments table.

headers (bool, optional):
    If <code>False</code>, no header row will be written (this is the standard for
    experimental space CSV files). If <code>True</code>, the header row will be
    written to the file.

##### Notes
There is nothing returned by this method.

    
##### Method `export_experimental_space_csv`



    
> `def export_experimental_space_csv(self, fname)`


Gets the validated experimental space table and writes the table to
a CSV file on disk.

##### Arguments
fname (str):
    The filesystem path where the file will be written.

##### Returns
space (dict):
    A Python <code>dict</code> representing the validated experimental space.

    
##### Method `export_experiments_history_csv`



    
> `def export_experiments_history_csv(self, fname)`


Gets and returns the experiments and responses for all generations in the session,
and writes them to a summary CSV file on disk. Also updates the <code>experiments\_history</code>
attribute in the client.

##### Arguments
fname (str):
    The filesystem path where the file will be written.

##### Returns
experiments_history (list): or None
    The value of the client's <code>experiments\_history</code> attribute, which may be
    None if no experiments have been submitted or designed, or is a list of <code>dict</code>s.
    See the documentation for the <code>get\_experiments\_history</code> method for a description
    of this value.

##### Notes
The CSV file for the experiments history contains three extra columns, "Seq_", "Gen_",
and "Designed_", in addition to the standard experiments CSV columns (the input arameters
for the experimental space, and the "Response" column). For each data row in the
CSV file, "Seq_" will be a sequential index, starting at 1, "Gen_" will contain the
generation number for the experiment, and "Designed_" will be "Y" if the experiment
was designed by the daptics process, or "N" if the experiment was an initial or extra
experiment submitted by the user.

    
##### Method `export_generated_design_csv`



    
> `def export_generated_design_csv(self, fname, gen=None)`


Gets a design generation from the session, and writes the
table (with empty responses) to a CSV file on disk.

##### Arguments
fname (str):
    The filesystem path where the file will be written.

gen (int, optional):
    The generation number for the design to be retrieved.
    If None, retreive the design for the current generation.

##### Returns
design_table (dict):
    The generated design, a Python <code>dict</code> representing an experiments table
    with empty responses with <code>colHeaders</code>, and <code>data</code> keys.

    
##### Method `export_initial_experiments_template_csv`



    
> `def export_initial_experiments_template_csv(self, fname)`


Gets the validated experimental space table and writes an
empty initial experiments table to a CSV file on disk.

##### Arguments
fname (str):
    The filesystem path where the file will be written.

##### Returns
column_headers (list):
    The experiments table header row that was written to disk, as a list of strings.

    
##### Method `generate_analytics`



    
> `def generate_analytics(self)`


Starts an "analytics" task that will create and return a list of all the
available analytics files for the session at the current design generation.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>createAnalytics</code> item. The <code>createAnalytics</code> value will contain information on the
    "analytics" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

###### # Notes

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "analytics" task completes
successfully, the result of the task can be accessed at
`data['createAnalytics']['result']`.

If the task completes successfully and the <code>auto\_export\_path</code> option is set,
the set of all available PDF analytics files for the generation will be
downloaded to that directory. The file name for each of the downloaded files
will have the prefix <code>auto\_genN\_</code> where <code>N</code> is the generation number.

    
##### Method `generate_design`



    
> `def generate_design(self, gen=None)`


If (initial or subsequent) experiments have been successfully validated against the
experimental parameters, a "generate" task is started.

##### Arguments
gen (int, optional):
    The current generation number for the experiments that have successfully validated.
    Use zero for initial experiments. Use <code>None</code> to use the <code>gen</code> attribute stored
    in the client.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>generateDesign</code> item. The <code>generateDesign</code> contains information on the
    "generate" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Raises
GraphQLError
    If the task failed or timed out.

##### Notes
If the <code>auto\_export\_path</code> option is set, a CSV file of the generated
design is saved at <code>auto\_genN\_design.csv</code>.

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "generate" task completes
successfully, the result of the task can be accessed at
`data['generateDesign']['result']`.

See the documentation on the "generate" task result in
the <code>poll\_for\_current\_task</code> method for information on the CSV file
generated if the <code>auto\_export\_path</code> option is set.

    
##### Method `get_experimental_space`



    
> `def get_experimental_space(self)`


Utility method to retrieve the validated experimental space from
the session. If the session was restarted and the experimental space
had been previously validated, it will be in the <code>validated\_params</code>
attribute of the client, and this method will return it.

##### Returns
space (dict):
    The validated space, a Python <code>dict</code> with <code>type</code>, and <code>table</code> items, and
    a <code>totalUnits</code> item if the space type is "mixture", or None if
    the space has not been validated.

    
##### Method `get_experiments`



    
> `def get_experiments(self, design_only=False, gen=None)`


Gets the designed or completed experiments for the current or any
previous generation.

##### Arguments
design_only (bool):
    If <code>gen</code> is specified, and this argument is set to <code>True</code>, only
    return the designed experiments (without responses).

gen (int):
    The generation number to search for. Use 0 to specify initial
    experiments. Use <code>None</code> to search for the last designed generation.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with an
    <code>experiments</code> item. The <code>experiments</code> value is a <code>dict</code> containing
    these items:

validated (bool):
    <code>True</code> if these experiments have been validated.

hasResponses (bool):
    <code>True</code> if at least some of these experiments have responses.

designRows (int):
    The number of rows of experiments that were designed. Rows after the <code>designRows</code>
    are "extra" experiments.

table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> items, representing the
    experiments submitted or designed for the generation.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

    
##### Method `get_experiments_history`



    
> `def get_experiments_history(self)`


Gets all of the experiments and any responses for all the generations in the session.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with an
    <code>experimentsHistory</code> item. The <code>experimentsHistory</code> value is either <code>None</code>
    if no experiments have been submitted or designed, or a list.
    Each item in the list is either <code>None</code>, or a <code>dict</code> with information
    about a generation. The first item in the list is for generation "zero",
    the initial experiments.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
Each generation available in the list (not <code>None</code>), is a Python <code>dict</code>
with the following items:

gen (int):
    The generation number (zero meaning initial experiments).

validated (bool):
    <code>True</code> if these experiments have been validated.

hasResponses (bool):
    <code>True</code> if at least some of these experiments have responses.

designRows (int):
    The number of rows of experiments that were designed. Rows after the <code>designRows</code>
    are "extra" experiments.

table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> values, representing the
    experiments submitted or designed for the generation.

This method also updates the client's <code>experiments\_history</code> attribute.

    
##### Method `get_generated_design`



    
> `def get_generated_design(self, gen=None)`


Gets a design generation from the session.

##### Arguments
gen (int):
    The generation number for the design to be retrieved.
    If <code>None</code>, retreive the design for the current generation.

##### Returns
experiments (dict):
    The value of the <code>experiments</code> item from the GraphQL response,
    a Python <code>dict</code> with these items:

validated (bool):
    <code>True</code> if these experiments have been validated.

hasResponses (bool):
    <code>True</code> if at least some of these experiments have responses.

designRows (int):
    The number of rows of experiments that were designed. Rows after the <code>designRows</code>
    are "extra" experiments.

table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> values, representing the
    experiments submitted or designed for the generation.

    
##### Method `halt_session`



    
> `def halt_session(self, session_id)`


Closes an connected session, to release all resources.

##### Arguments
session_id (str):
    The session id to close.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>haltSession</code> item. The 'haltSession' value is a <code>dict</code> containing
    these items:

action (str):
    The action taken, either 'close' (if the session was connected) or 'none' if
    had previously been closed.

status (str):
    The session status, which should always be 'closed', if the action was successful,
    or if the sesson had previously been closed.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

    
##### Method `init_config`



    
> `def init_config(self)`


Reads and processes the client configuration from either a configuration
file or from environment variables.

##### Raises
MissingConfigError
    If the config file specified does not exist.

InvalidConfigError
    If the config file specified cannot be parsed, or does not have a 'host'
    value.

##### Notes
There is nothing returned by this method.

    
##### Method `list_sessions`



    
> `def list_sessions(self, user_id=None, name=None)`


Returns a list of all the user's sessions.

##### Arguments
user_id (str):
    (optional) Limit the results to the user with this id. Omitting this argument
    is normal for regular users.

name (str):
    (optional) Limit the results to any session whose name, description,
    <code>tag</code> or id contains this string.

##### Returns
data (list):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>sessions</code> item. The <code>sessions</code> value is a list, where each item in the list
    is a Python <code>dict</code> containing summary information about the session`s
    identifier, name, and description.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

    
##### Method `load`



    
> `def load(self, fname)`


Restores a previously saved client from a JSON file.

##### Arguments
fname (str):
    The file path to restore the client state from.

##### Notes
There is nothing returned by this method.

    
##### Method `login`



    
> `def login(self, email=None, password=None)`


Authenticates to a user record in the database as identified in the client's
<code>email</code> and <code>password</code> attributes, and create an access token.

##### Arguments
email (str):
    The email adddress of the database user that will be used for authentication.

password (str):
    The cleartext password of the database user that will be used for authentication.

If called with default (<code>None</code>) arguments, the email and password will
be retrieved from the <code>credentials</code> attribute.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>login</code> item. The <code>login</code> item is a <code>dict</code> with these items:

token (str):
    The access token to be used for user access to the API.

user (dict):
    A Python <code>dict</code> with one string item, <code>userId</code>, that can be used
    to create sessions.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
On successful authentication, the user id and access token
are stored in the client's <code>user\_id</code> and <code>auth</code> attributes. On failure
the value of the <code>login</code> item in the returned dict will be <code>None</code>.

    
##### Method `poll_for_current_task`



    
> `def poll_for_current_task(self, task_type=None)`


If there is a currently running task saved in the client, poll the
session to see if a result is ready.

##### Arguments
task_type (<code>[DapticsTaskType](#daptics\_client.daptics\_client.DapticsTaskType)</code>):
    <code>SPACE</code>, <code>UPDATE</code>, <code>GENERATE</code>, <code>SIMULATE</code>, <code>ANALYTICS</code>, or None.
If None is supplied (the default), find the most recently started task of any type.

##### Returns
data (dict):
    The <code>data</code> item of the GraphQL response, a Python <code>dict</code> with a
    <code>currentTask</code> item, described below.

errors (list):
    The <code>errors</code> item of the GraphQL response. Each item in the list
    is guaranteed to have a <code>message</code> item.

##### Notes
Either <code>data</code> or <code>errors</code> may be None.

The <code>currentTask</code> value returned is a Python <code>dict</code> containing information
on the task (if found). The items in the <code>dict</code> are as follows:

taskId (str):
    The unique identifier for the task.

type (str):
    The type of task, either "space", "update", "generate", "simulate", or "analytics".

description (str):
    A user-friendly description of what the task is.

startedAt (str):
    An ISO 8601 string value of the UTC time at which the task was started.

status (str):
    The status of the task, either <code>new</code>, <code>running</code>, <code>success</code>, <code>failed</code>, or <code>canceled</code>.

result (dict):
    If the status of the task is <code>success</code>, the value of the <code>result</code> is another
    Python <code>dict</code>. The results for each type of task are as follows:

###### Result for "space" Tasks
The result for all tasks is a Python <code>dict</code>. For the "space" task,
the <code>dict</code> has two items, <code>campaign</code> and <code>params</code>:

campaign (dict):
    A Python <code>dict</code> with these items:

gen (int):
    The generation number for the session (0).

remaining (int):
    If available, how many more generations can be performed.

completed (bool):
    If available, whether the campaign has been completed.

params (dict):
    A Python <code>dict</code> with these items:

validated (bool):
    <code>True</code> if the space was validated.

designCost (int):
    If available, the cost in daptics credit that will be deducted
    from the user's account for each design generation.

populationSize, replicates, and space:
    See the description for these values in the documentation for the
    arguments for the <code>put\_experimetal\_parameters</code> method.

If a "space" task has successfully completed, the client's <code>gen</code> attribute is
set to zero.

Also, if the <code>auto\_export\_path</code> option is set, a CSV file named
"auto_validated_space.csv" is written at that directory,
containing the experimental space parameters.

###### Result for "update" Tasks

The result for an "update" task will contain all the items as the result for a "space"
task, described above, with an additional <code>experiments</code> item:

experiments (dict):
    A Python <code>dict</code> with these items:

gen (int):
    The generation number for this set of experiments.

validated (bool):
    <code>True</code> if the experiments validated successfully.

hasResponses (bool):
    <code>True</code> if any of the experiments in this set were submitted with responses.

designRows (int):
    The number of rows of daptics-designed experiments in this set of experiments.
    <code>designRows</code> will be zero if these are initial experiments.

table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> items, as described in
    the arguments for the <code>put\_experiments</code> method.

If the <code>auto\_generate\_next\_design</code> option has been set on the client, when an
"update" task completes, a "generate" task will be automatically started. The
information on the "generate" task will be returned in the location
`data['currentTask']['autoGenerateTask']`.

If the <code>auto\_task\_timeout</code> option has also been set, and the "generate" task
result has completed, the result (containing the next generation design),
will be available at the location `data['currentTask']['autoGenerateTask']['result']`,
formatted as described below.

Also, if the <code>auto\_export\_path</code> option is set, a CSV file named
"auto_genN_experiments.csv" is written at that directory,
containing the validated experiments, where "N" is the generation number.

###### Result for "generate" Tasks

The result for a "generate" task has the same structure as the result for a
"update" task, described above. The <code>experiments</code> value will contain the generated design,
and the <code>hasResponses</code> value within the design will be <code>False</code>, as the generated design
returned in the result will not have responses.

If the "generate" task has successfully completed, the client's <code>gen</code> attribute is updated
to a number greater than zero, and the generated design from the <code>experiments</code> value
will be stored in the client's <code>design</code> attribute.

Also, if the <code>auto\_export\_path</code> option is set, a CSV file named
"auto_genN_design.csv" is written at that directory,
containing the designed experiments, where "N" is the generation number.

###### Result for "simulate" Tasks
The result for a "simulate" task will contain all the items as the result for a "space"
task, described above, with one additional item, <code>experimentsHistory</code>:

experimentsHistory (list):
    A list of all the experiments in generations 1 through N, that were simulated.
    Each element of the list will be a Python <code>dict</code> with <code>gen</code>, <code>validated</code>,
    <code>hasResponses</code>, <code>designRows</code> and <code>table</code> items as described above in the
    documentation for the result of an "update" task.

If the <code>auto\_export\_path</code> option is set, a CSV file named
"auto_history.csv" is written at that directory,
containing all the simulated experiments. See the documentation for the
<code>export\_experiments\_history\_csv</code> method for a description of this file's
contents.

###### Result for "analytics" Tasks

The result <code>dict</code> will have one item, <code>analytics</code>:

analytics (dict):
    A Python <code>dict</code> with these items:

gen (int):
    The current generation number that the analytics were generated for.

files (list):
    A list of Python <code>dict</code>s, with information about each analytics file
    generated.

Information about each file is contained in a Python <code>dict</code> with these items:

title (str):
    The title (caption) describing the file.

filename (str):
    The suggested filename to save the file to.

url (str):
    The HTTP URL where the file can be downloaded. A valid authentication token for the
    user must be included as the value of a <code>token</code> query string parameter
    added to the URL for the download request.

If the "analytics" task has successfully completed, the <code>analytics</code> Python <code>dict</code>,
containing the generation number and file list, will be stored in the client's
<code>analytics</code> attribute.

If the <code>auto\_export\_path</code> option is set, the set of all available PDF analytics
files for the generation will be downloaded to that directory.
The file name for each of the downloaded files will have the
prefix <code>auto\_genN\_</code> where <code>N</code> is the generation number.

    
##### Method `print`



    
> `def print(self)`


Prints out debugging information about the session.

    
##### Method `put_experimental_parameters`



    
> `def put_experimental_parameters(self, params)`


Validates the experimental parameters at the beginning of a session,
and starts a "space" task. The individual experimental parameter names,
types and permissible values in the space definition are specified at
the `['space']['table']` key of the <code>params</code> <code>dict</code>.

##### Arguments
params (dict):
    A Python <code>dict</code> containing the experimental parameters to be
    used for the session. See the Notes section that describes the
    required items for the <code>params</code> <code>dict</code>.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>putExperimentalParameters</code> item. The <code>putExperimentalParameters</code> value
    is a Python <code>dict</code> with information about the "space" task.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
If the task was successfully started, the task information is stored in the client's
<code>task\_info</code> attribute.

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "space" task completes
successfully, the result of the task can be accessed at
`data['putExperimentalParameters']['result']`.

See the documentation on the "space" task result in the <code>poll\_for\_current\_task</code> method
for information on the CSV file generated if the <code>auto\_export\_path</code> option is set.

These are the required items for the <code>params</code> <code>dict</code>:

populationSize (int):
    The number of experiments per replicate. A positive integer.

replicates (int):
    The number of replicates. A non-negative integer. The total number of
    experiments per design generation is `populationSize * (replicates + 1)`.

space (dict):
    The experimental space definition. The required items for the <code>space</code> <code>dict</code> are:

type (str):
    The type of the space, a string, either "factorial" or "mixture".

totalUnits (int):
    For "mixture" type spaces, this is the mixture constraint parameter,
    a non-negative integer.

table (dict):
    The (optional) column headers and rows of parameter data.  See
    an example below. the <code>colHeaders</code> value is ignored when importing
    or validating the experimental space definition.

To maintain uniformity, header and data row elements should be
Python strings, even if they represent numeric values.

For "mixture" type spaces, there should only be 4 columns of data
in each row: the name of the parameter, the type of the parameter
(which must always be the string "unit"), the minimum value of the
parameter (a non-negative integer) and the maximum value of the
parameter (a positive integer, less than or equal to the <code>totalUnits</code>
constraint parameter).

For "factorial" type spaces, there must be at least 4 columns of data
in each row: the name of the parameter, the type of the parameter
(a string, either "numerical" or "categorical"), and at least
two possible distinct values that the parameter can have in an experiment.
Different parameters can have either 2 or more than 2 possible values.
The rows must be all be of the same size, so make sure to pad the
rows with fewer values with empty strings at the end.

In addition to the required <code>params</code> listed above, optional additional
parameters may be submitted. Please contact daptics for more information
about these advanced parameters.

##### Examples
Here is a mixture space design that will have enough combinations to be
validated by the backend.

```python
>>> params = {
    'populationSize': 30,
    'replicates': 2,
    'space': {
        'type': 'mixture',
        'totalUnits': 25,
        'table': {
            'colHeaders':
                [ 'Name', 'Type', 'Min', 'Max' ],
            'data': [
                [ 'param1', 'unit', '1', '10' ],
                [ 'param2', 'unit', '2', '10' ],
                [ 'param3', 'unit', '4', '8' ],
                [ 'param4', 'unit', '2', '5' ]
            ]
        }
    }
}
```

Here is a factorial space design that will have enough combinations to be
validated by the backend.

```python
>>> params = {
    'populationSize': 30,
    'replicates': 2,
    'space': {
        'type': 'factorial',
        'table': {
            'colHeaders':
                [ 'Name', 'Type', 'Value.1', 'Value.2', 'Value.3', 'Value.4' ],
            'data': [
                [ 'param1', 'numerical', '0', '1', '2', '3' ],
                [ 'param2', 'numerical', '2', '3',  '',  '' ],
                [ 'param3', 'numerical', '0', '1', '2',  '' ],
                [ 'param4', 'numerical', '0', '1', '2', '3' ]
            ]
        }
    }
}
```

    
##### Method `put_experimental_parameters_csv`



    
> `def put_experimental_parameters_csv(self, fname, params)`


Validates the experimental parameters at the beginning of a session,
and starts a "space" task. The individual experimental parameter names,
types and permissible values in the space definition are read from a CSV file.

##### Arguments
fname (str):
    The location on the filesystem for a CSV file that will define
    the experimental space definition. See the Examples section
    below for an example.

params (dict):
    A Python <code>dict</code> containing the experimental parameters to be
    used for the session. See the Notes section for more information.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>putExperimentalParameters</code> item. The <code>putExperimentalParameters</code> value
    is a Python <code>dict</code> with information about the "space" task.

##### Raises
csv.Error
    If the specified CSV file is incorrectly formatted.

##### Notes
If the task was successfully started, the task information is stored in the client's
<code>task\_info</code> attribute.

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "space" task completes
successfully, the result of the task can be accessed at
`data['putExperimentalParameters']['result']`.

See the documentation on the "space" task result in the <code>poll\_for\_current\_task</code> method
for information on the CSV file generated if the <code>auto\_export\_path</code> option is set.

Items for the <code>params</code> <code>dict</code> are:

populationSize (int):
    The number of experiments per replicate. A positive integer.

replicates (int):
    The number of replicates. A non-negative integer. The total number of
    experiments per design generation is `populationSize * (replicates + 1)`.

space (dict):
    The experimental space definition. The single required item for the <code>space</code> <code>dict</code> is:

type (str):
    "factorial" or "mixture"

In addition to the required <code>params</code> listed above, optional additional
parameters may be submitted. Please contact daptics for more information
about these advanced parameters.

##### Examples
Here is a space design that will have enough combinations to be
validated by the backend.

```python
>>> params = {
    'populationSize': 30,
    'replicates': 2,
    'space': {
        'type': 'factorial',
    }
}
```

The contents of an example CSV file for a "factorial" space might be:

```
param1,numerical,0,1,2,3
param2,numerical,2,3,4,
param3,numerical,0,1,,
param4,numerical,0,1,2,3
```

Each parameter row in a factorial space definition should have the same
number of columns.  Parameter rows with fewer than the maximum number of values
should have the empty columns at the end of the row, as shown above.

The contents of an example CSV file for a "mixture" space might be:

```
param1,unit,0,10
param2,unit,5,10
param3,unit,0,10
param4,unit,0,5
```

Each parameter fow in a mixture space defintion must specify a minimum and
maximum unit volume, as shown above.

Do not supply a header row for the space definition (for any type), just the parameter
rows.

    
##### Method `put_experiments`



    
> `def put_experiments(self, experiments_type, experiments)`


Validate the responses for designed experiments, and any extra experiments
for the current generation in the session. This method, or the
<code>put\_experiments\_responses\_csv</code> method, must be called before generating the
next design, or finalizing the campaign.

##### Arguments
experiments_type (<code>[DapticsExperimentsType](#daptics\_client.daptics\_client.DapticsExperimentsType)</code>):
    Describes the types of experiments that are being added to the session.

If you wish to submit calibrating or existing experimental responses prior
to the first design generartion, use <code>INITIAL\_EXTRAS\_ONLY</code>.

If you are submitting the responses for a daptics-generated design, along
with any extra experiments, use <code>DESIGNED\_WITH\_OPTIONAL\_EXTRAS</code>.

If you wish to submit any final extra experiments when you are satisified
with the session's optimization but do not want to include the last
generated experimental design use <code>FINAL\_EXTRAS\_ONLY</code>. Note that this
will end the session's optimization and that no more designs will be
generated.

experiments (dict):
    A "table" of experiments that includes columns,
    defined in the <code>colHeaders</code> value of the table, for each of the defined
    space parameters, and a column named 'Response' to record the result of
    experiments.

Each row in the <code>data</code> value for the table represents
an individual experiment.

If the <code>experiments type</code> is <code>DESIGNED\_WITH\_OPTIONAL\_EXTRAS</code>,
you must sumbit at least as many rows as exist in the currently
generated design, and the parameter values for these rows
must match the design exactly. Additional "extra" experiment
rows, that use any valid experimental parameter values, can also
be provided.

For the <code>INITIAL\_EXTRAS\_ONLY</code> and <code>FINAL\_EXTRAS\_ONLY</code> experiments types,
rows that use any valid experimental parameter values can be provided.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>putExperiments</code> item. The <code>putExperiments</code> value will contain information on the
    "update" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
If the task was successfully started, the task information is stored in the client's
<code>task\_info</code> attribute.

If the experiments were successfully validated, the following actions may be
automatically performed:

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "update" task completes
successfully, the result of the task can be accessed at
`data['putExperiments']['result']`.

If the <code>auto\_generate\_next\_design</code> option is set, a "generate"
task is started, and the <code>autoGenerateTask</code> item of the <code>putExperiments</code>
item will contain information on the "generate" task that was started.

If the <code>auto\_generate\_next\_design</code> AND <code>auto\_task\_timeout</code> options are set,
the "generate" task will be polled until it completes, fails, or times out.
If the "generate" task completes, the generated design can be accessed at
`data['putExperiments']['autoGenerateTask']['result']['experiments']`. See
the documentation for the <code>poll\_for\_current\_task</code> for more information.

See the documentation on the "update" and "generate" task results in
the <code>poll\_for\_current\_task</code> method for information on the CSV files
generated if the <code>auto\_export\_path</code> option is set.

##### Examples
Here's an expamle of an experiments table:

```python
>>> experiments = {
    'colHeaders': ['param1', 'param2', 'param3', 'param4', 'Response'],
    'data': [
        ['0', '4', '1', '1', '3.25'],
        ['1', '4', '1', '1', '4.5'],
        ... etc, matching generated design rows
    ]
}
```

    
##### Method `put_experiments_csv`



    
> `def put_experiments_csv(self, experiments_type, fname)`


Validate the responses for designed experiments, and any extra experiments
for the current generation in the session. This method, or the
<code>put\_experiments\_responses</code> method, must be called before generating the
next design, or finalizing the campaign.

##### Arguments
experiments_type (<code>[DapticsExperimentsType](#daptics\_client.daptics\_client.DapticsExperimentsType)</code>):
    Describes the types of experiments that are being added to the session.

    If you wish to submit calibrating or existing experimental responses prior
    to the first design generartion, use <code>INITIAL\_EXTRAS\_ONLY</code>.

    If you are submitting the responses for a daptics-generated design, along
    with any extra experiments, use <code>DESIGNED\_WITH\_OPTIONAL\_EXTRAS</code>.

    If you wish to submit any final extra experiments when you are satisified
    with the session's optimization but do not want to include the last
    generated experimental design use <code>FINAL\_EXTRAS\_ONLY</code>. Note that this
    will end the session's optimization and that no more designs will be
    generated.

fname (str):
    The location on the filesystem for a CSV file that will define
    the results of the designed and any extra experiments. See the Examples section
    below for an example.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>putExperiments</code> item. The <code>putExperiments</code> value will contain information on the
    "update" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Notes
If the experiments were successfully validated, the following actions may be
automatically performed:

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "update" task completes
successfully, the result of the task can be accessed at
`data['putExperiments']['result']`.

If the <code>auto\_generate\_next\_design</code> option is set, a "generate"
task is started, and the <code>autoGenerateTask</code> item of the <code>putExperiments</code> item
will contain information on the "generate" task that was started.

If the <code>auto\_generate\_next\_design</code> AND <code>auto\_task\_timeout</code> options are set,
the "generate" task will be polled until it completes, fails, or times out.
If the "generate" task completes, the generated design can be accessed at
`data['putExperiments']['autoGenerateTask']['result']['experiments']`. See
the documentation for the <code>poll\_for\_current\_task</code> for more information.

See the documentation on the "update" and "generate" task results in
the <code>poll\_for\_current\_task</code> method for information on the CSV files
generated if the <code>auto\_export\_path</code> option is set.

##### Examples
A header row must be provided, the columns in the header row
must match the names of the parameters defined by the experimental space definition
exactly, and a final column named <code>Response</code> must be filled with the results
of each experiment row.

```
param1,param2,param3,param4,Response
0,4,1,1,3.25
1,4,1,1,4.5
```

Each non-header row in the file represents an individual experiment. There must be at
least as many experiment rows as the current design has, and the parameter values
for these rows must match the design exactly. Additional "extra" experiment
rows can also be provided.

    
##### Method `random_experiment_for_space`



    
> `def random_experiment_for_space(self, space, max_response_value=None)`


Uses a random number generator to select parameter values and
optionally to create a random response value.

##### Arguments
space (dict):
    A Python <code>dict</code> that defines the experimental space.

max_response_value (float, optional):
    If omiited, the experiment is generated with an empty response.
    If a number, the response value is a randomly generated number
    in the range [0.0, max_response_value].

##### Returns
experiment (list):
    The list of randomly generated parameter values for an experiment,
    and the optionally generated response value. Each value is encoded as a string.
    If <code>max\_response\_value</code> is not given, the response value will be the
    empty string.

    
##### Method `random_experiments_with_responses`



    
> `def random_experiments_with_responses(self, space, design, num_extras=0, max_response_value=5.0)`


Generates an experiments table where each experiment row
contains a randomly generated response value. The experiment rows
are optionally  composed of "designed" rows and "extra" rows.
The "designed" rows have one experiment row for each row in the
currently generated design. And the "extra" rows contain randomly
generated parameter values as well as responses.

##### Arguments
space (dict):
    A Python <code>dict</code> that defines the experimental space.

design (dict, optional):
    If supplied, a Python <code>dict</code> that defines the currently generated
    design as a table. The <code>dict</code> has <code>colHeaders</code> and <code>data</code> items.

num_extras: int, optional
    If non-zero, generate this number of extra rows. The extra rows
    will be appended to any designed rows.

max_response_value (float):
    The maximum value for generated responses. Each genreated response value
    is a randomly generated number in the range [0.0, max_response_value].

##### Returns
table (dict):
    A Python <code>dict</code> with <code>colHeaders</code> and <code>data</code> values, representing an
    experiments table.

    
##### Method `random_parameter_value`



    
> `def random_parameter_value(self, space_type, param)`


Uses a random number generator to select a parameter value that is valid
for the space type and specified parameter definition.

##### Arguments
space_type (str):
    The space type, either "mixture" or "factorial".

param (list):
    The row from the experimental space definition table that defines
    a particular parameter in the space (name, type, and min / max or
    allowed values for the parameter). Each element in the list is
    encoded as a string.

##### Returns
param_value (str):
    A valid value for the parameter, encoded as a string.

    
##### Method `reconnect_session`



    
> `def reconnect_session(self, session_id)`


Finds an existing session and returns session information.

##### Arguments
session_id (str):
    The session id to find.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>session</code> item. The <code>session</code> value is a Python <code>dict</code> containing
    information about the session's name, description, experimental
    space parameters, experiments history, and any active tasks.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
Sets client attributes for the reconnected session.

    
##### Method `run_task_async`



    
> `def run_task_async(self, document, vars)`


Performs validation on the GraphQL mutation document and then
executes the query, returning both the <code>data</code> and <code>errors</code> items from the JSON
response. Before submitting the query, a "taskUpdated" subscription is
set up, and the asynchronous loop processes subscription data messages,
eventually passing task progress and status information to the coroutine
specified by the client's <code>task\_updated\_coroutine</code> attribute.

    
##### Method `save`



    
> `def save(self, fname)`


Saves the user and session id to a JSON file.

##### Arguments
fname (str):
    The file path to save the client state to.

##### Notes
There is nothing returned by this method.

    
##### Method `simulate_experiment_responses`



    
> `def simulate_experiment_responses(self, experiments=None)`


Generates values for the "Response" column.  The values are a
substitute for actual experimental results, computed with a
synthetic data generator that takes as an input each
experiment (i.e. each row of the experiments argument) and
gives as output a single number, added as a 'Response'.  The
data generator samples a complex surface, constructed to have
several peaks that are randomly placed in the space.  There is
a global optimum (highest peak), but optimization runs often
will find one of the lower peaks.

##### Arguments
experiments (dict):
    An optional "table" of experiments that includes columns,
    defined in the <code>colHeaders</code> value of the table, for each of the defined
    space parameters, and a column named 'Response' to record the result of
    experiments.

Each row in the <code>data</code> value for the table represents
an individual experiment. If <code>experiments</code> is set to <code>None</code>, and 
a generated design exists in the session (gen number is greater than zero),
simulated responses for the design will be created and returned.
It is an error to set <code>experiments</code> to <code>None</code> if no design has been
generated in the session (gen number is less than or equal to zero).

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>simulateExperiments</code> item. See the documentation for the <code>get\_experiments</code>
    method for a description of the values returned.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

    
##### Method `simulate_experiment_responses_csv`



    
> `def simulate_experiment_responses_csv(self, fname)`


Generates values for the "Response" column.  The values are a
substitute for actual experimental results, computed with a
synthetic data generator that takes as an input each
experiment (i.e. each row of the experiments argument) and
gives as output a single number, added as a 'Response'.  The
data generator samples a complex surface, constructed to have
several peaks that are randomly placed in the space.  There is
a global optimum (highest peak), but optimization runs often
will find one of the lower peaks.

##### Arguments
fname (str):
    The location on the filesystem for a CSV file that will define
    the parameters for designed and any extra experiments.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>simulateExperiments</code> item.

    
##### Method `space_table_column_names`



    
> `def space_table_column_names(self, space)`


Generates the canonically formatted column header names for
the experimental space table.

##### Arguments
space (dict):
    A Python <code>dict</code> that defines the experimental space.

##### Returns
column_headers (list):
    A list of strings to build the column header for an experimental space.
    The list will contain "Name", "Type", "Min" and "Max" for a "mixture" space,
    or "Name", "Type", "Value.1", "Value.2", etc. for a "factorial" space.

    
##### Method `space_table_value_column_name`



    
> `def space_table_value_column_name(self, space_type, i)`


Formats a single column name for the header row in an experimental space table.

##### Arguments
space_type (str):
    "mixture" or "factorial"

i (int):
    Index of the value column (starting at zero).

##### Returns
column_name (str):
    "Min" or "Max" for a "mixture" space type, or "Value.1", "Value.2", etc.
    for a "factorial" space type.

    
##### Method `start_simulation`



    
> `def start_simulation(self, ngens, params)`


Starts a simulation task for several design generations, specifying the
desired experimental parameters and the number of generations
to run.

##### Arguments
ngens (int):
    The number of generations to attempt to design. Must be greater than zero.
    If the experimental space is exhausted the actual number of generations
    designed may be less than this number.

params (dict):
    A Python <code>dict</code> containing the experimental parameters to be
    used for the session. See the Notes section that describes the
    required items for the <code>params</code> <code>dict</code>.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>runSimulation</code> item. The <code>runSimulation</code> value contains information on the
    "simulate" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Raises
GraphQLError
    If no data was returned by the query request, a <code>[GraphQLError](#daptics\_client.daptics\_client.GraphQLError)</code> is raised,
    containing the message for the first item in the GraphQL response's <code>errors</code> list.

##### Notes
Items to be specified in the <code>params</code> <code>dict</code> are:

populationSize (int):
    The number of experiments per replicate. A positive integer.

replicates (int):
    The number of replicates. A non-negative integer. The total number of
    experiments per design generation is `populationSize * (replicates + 1)`.

space (dict):
    The experimental space definition. Items in the <code>space</code> <code>dict</code> are:

type (str):
    The type of the space, a string, either "factorial" or "mixture".

totalUnits (int):
    For "mixture" type spaces, this is the mixture constraint parameter,
    a non-negative integer.

table (dict):
    The (optional) column headers and rows of parameter data.  See
    an example below. the <code>colHeaders</code> value is ignored when importing
    or validating the experimental space definition.

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "simulate" task completes
successfully, the result of the task can be accessed at
`data['runSimulation']['result']`.

See the documentation on the "simulate" task result in
the <code>poll\_for\_current\_task</code> method for information on the CSV file
generated if the <code>auto\_export\_path</code> option is set.

For more examples of how to submit space parameters, please
see the documentation for the <code>put\_experimental\_parameters</code> method.

    
##### Method `start_simulation_csv`



    
> `def start_simulation_csv(self, ngens, fname, params)`


Run a simulation for several design generations, specifying the
desired experimental parameters and the number of generations to run.
The experimental space is read from a CSV file. If the space parameters
are successfully validated a "simulate" task is started.

##### Arguments
ngens (int):
    The number of generations to attempt to design. Must be greater than zero.
    If the experimental space is exhausted the actual number of generations
    designed may be less than this number.

fname (str):
    The location on the filesystem for a CSV file that will define
    the experimental space definition. See the Examples section
    below for an example.

params (dict):
    A Python <code>dict</code> containing the experimental parameters to be
    used for the session.  See the Notes section that describes the
    required items for the <code>params</code> <code>dict</code>.

##### Returns
data (dict):
    The JSON response from the GraphQL request, a Python <code>dict</code> with a
    <code>runSimulation</code> item. The <code>runSimulation</code> value will contain information on the
    "simulate" task that was started, as described in the return value for the
    <code>poll\_for\_current\_task</code> method.

##### Raises
csv.Error
    If the specified CSV file is incorrectly formatted.

##### Notes
Items to be specified in the <code>params</code> <code>dict</code> are:

populationSize (int):
    The number of experiments per replicate. A positive integer.

replicates (int):
    The number of replicates. A non-negative integer. The total number of
    experiments per design generation is `populationSize * (replicates + 1)`.

space (dict):
    The experimental space definition. Items in the <code>space</code> <code>dict</code> are:

type (str):
    The type of the space, a string, either "factorial" or "mixture".

totalUnits (int):
    For "mixture" type spaces, this is the mixture constraint parameter,
    a non-negative integer.

If the <code>auto\_export\_path</code> option is set, a CSV file of each generation of
simulated experiments is saved at <code>auto\_genN\_experiments.csv</code>.

If the <code>auto\_task\_timeout</code> option was set to a
positive or negative number, the task will be retried until a result is obtained
or the task failed, or the timeout is exceeded. If the "simulate" task completes
successfully, the result of the task can be accessed at
`data['runSimulation']['result']`.

See the documentation on the "simulate" task result in
the <code>poll\_for\_current\_task</code> method for information on the CSV file
generated if the <code>auto\_export\_path</code> option is set.

For more examples of how to submit space parameters, please
see the documentation for the <code>put\_experimental\_parameters</code> method.

    
##### Method `wait_for_current_task`



    
> `def wait_for_current_task(self, task_type=None, timeout=None)`


Wraps poll_for_current_task in a loop. Repeat until task disappears,
when <code>status</code> is <code>success</code>, <code>failed</code>, or <code>canceled</code>.

##### Arguments
task_type (<code>[DapticsTaskType](#daptics\_client.daptics\_client.DapticsTaskType)</code>, optional):
    <code>SPACE</code>, <code>UPDATE</code>, <code>GENERATE</code>, <code>SIMULATE</code>, <code>ANALYTICS</code>, or None.
    If None is supplied (the default), find the most recently started task of any type.

timeout (float, optional):
    Maximum number of seconds to wait. If None or a negative number, wait forever.

##### Returns
data (dict):
    The <code>data</code> item of the GraphQL response, a Python <code>dict</code> with a
    <code>currentTask</code> item, described below.

errors (list):
    The <code>errors</code> item of the GraphQL response. Each item in the list
    is guaranteed to have a <code>message</code> item.

##### Notes
Either <code>data</code> or <code>errors</code> may be None.

See the documentation on the <code>poll\_for\_current\_task</code> method for more information
about the <code>data</code> item returned for different types of tasks,
and for how task completion affects attributes of the client instance.

    
### Class `DapticsExperimentsType`



> `class DapticsExperimentsType(value, names=None, *, module=None, qualname=None, type=None, start=1)`


Enumerates the purpose for the experiments that are being uploaded to the
session via the <code>put\_experiments</code> or <code>put\_experiments\_csv</code> methods.


    
#### Class variables


    
##### Variable `DESIGNED_WITH_OPTIONAL_EXTRAS`

The experiments submitted are designed experiments, and may also include optional
extra experiments.

    
##### Variable `FINAL_EXTRAS_ONLY`

Indicates that the experiments being submitted are final experiments.
Not used in current API version.

    
##### Variable `INITIAL_EXTRAS_ONLY`

The experiments submitted are initial experiments. No designed experiments are included.




    
### Class `DapticsTaskType`



> `class DapticsTaskType(value, names=None, *, module=None, qualname=None, type=None, start=1)`


Enumerates the different asynchronous tasks that the daptics system can create and
that can be searched for using the <code>poll\_for\_current\_task</code> or <code>wait\_for\_current\_task</code>
methods.


    
#### Class variables


    
##### Variable `ANALYTICS`

A task that generates analytics files at the current generation.

    
##### Variable `GENERATE`

The task type to be searched was created by the <code>generate\_design</code> method.

    
##### Variable `SIMULATE`

A task that simulates a given number of experimental generations.

    
##### Variable `SPACE`

The task type to be searched was created by the <code>put\_experimental\_parameters</code>
or <code>put\_experimental\_parameters\_csv</code> methods.

    
##### Variable `UPDATE`

The task type to be searched was created by the <code>put\_experiments</code>
or <code>put\_experimens\_csv</code> methods.




    
### Class `GraphQLError`



> `class GraphQLError(message)`


An error raised by converting the first item in the <code>errors</code> item of the GraphQL response.





    
### Class `IncompatibleApiError`



> `class IncompatibleApiError(client_version_required)`


An error raised if the API at <code>host</code> is not compatible with this client.





    
### Class `InvalidConfigError`



> `class InvalidConfigError(path)`


An error raised if the option configuration file cannot be parsed.





    
### Class `InvalidExperimentsTypeError`



> `class InvalidExperimentsTypeError(experiments_type)`


An error raised if the type of experiments is not a valid type.





    
### Class `InvalidSpaceParameterError`



> `class InvalidSpaceParameterError(space_type, param)`


An error raised if the specified experimental space parameters are missing or invalid.





    
### Class `InvalidTaskTypeError`



> `class InvalidTaskTypeError(task_type)`


An error raised if the task type specified was not a valid type.





    
### Class `MissingConfigError`



> `class MissingConfigError(path)`


An error raised if the option configuration file cannot be found.





    
### Class `NextGenerationError`



> `class NextGenerationError(gen)`


An error raised if the generation number specified is not the next generation
number for the session.





    
### Class `NoCredentialsError`



> `class NoCredentialsError()`


An error raised if no login credentials were specified.





    
### Class `NoCurrentTaskError`



> `class NoCurrentTaskError()`


An error raised if no current task could be found, when one was expected.





    
### Class `NoHostError`



> `class NoHostError()`


An error raised if no <code>host</code> value was specified.





    
### Class `SessionParametersNotValidatedError`



> `class SessionParametersNotValidatedError()`


An error raised if the method cannot be completed, because the experimental space
parameters for the session have not been saved and validated yet.





    
### Class `SpaceOrDesignRequiredError`



> `class SpaceOrDesignRequiredError()`


An error raised if neither an experimental space nor an experimental design was
submitted for generating random experiments.





    
### Class `TaskFailedError`



> `class TaskFailedError(type_)`


An error raised if a completed task did not return a valid result.





    
### Class `TaskTimeoutError`



> `class TaskTimeoutError()`


An error raised if a task was not completed within the specified timeout.





    
### Class `TokenAuth`



> `class TokenAuth()`


A callable authentication object for the Python <code>requests</code> moudule.
If the <code>token</code> attribute is set, the <code>\_\_call\_\_</code> method will insert an
"Authorization" header with a "Bearer" token into the HTTP request.

### Attributes
token (str):
    An access token obtained from the API for the authenticated user.






-----
Generated by *pdoc* 0.9.2 (<https://pdoc3.github.io>).
