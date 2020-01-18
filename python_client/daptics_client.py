"""# Python API Client

See comments and docstrings for the DapticsClient class in the code below
for suggestions for using this class. For additional help or information,
please visit or contact daptics:

* On the web at <a href="https://daptics.ai">https://daptics.ai
* By email at [support@daptics.ai](mailto:support@daptics.ai)

Daptics API Version 0.9.2
Copyright (c) 2020 Daptics Inc.

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
"""

import csv
import enum
import gql
import gql.transport.requests
import os
import json
import pprint
import random
import requests
import requests.auth
import time
import sys


# Authentication object used to authorize DapticsClient requests

class TokenAuth(requests.auth.AuthBase):
    """A callable authentication object for the Python "requests" moudule.
    If acess token is set, add a "Bearer" authorization header to the HTTP request.

    # Attributes
    token (str):
        An access token obtained from the API for the authenticated user.
    """
    def __init__(self):
        self.token = None

    def __call__(self, r):
        """Insert the authorization header as a bearer token.
        """
        if self.token is not None:
            r.headers['Authorization'] = 'Bearer ' + self.token
        return r


# Errors raised by the DapticsClient class

class MissingConfigError(Exception):
    def __init__(self, path):
        self.message = 'The specified configuration file {} does not exist.'.format(path)

class InvalidConfigError(Exception):
    def __init__(self, path):
        self.message = 'The configuration file {} is invalid.'.format(path)

class NoHostError(Exception):
    def __init__(self):
        self.message = 'No host or configuration file specified.'

class NoCredentialsError(Exception):
    def __init__(self):
        self.message = 'No credentials or configuration file specified.'

class NoCurrentTaskError(Exception):
    def __init__(self):
        self.message = 'There is no current task active in the session.'

class InvalidTaskTypeError(Exception):
    def __init__(self, task_type):
        self.message = 'The task type {} is not valid.'.format(task_type)

class TaskTimeoutError(Exception):
    def __init__(self):
        self.message = 'The current task did not complete within the timeout duration.'

class TaskFailedError(Exception):
    def __init__(self, type_):
        self.message = 'The {} task failed to return a valid result.'.format(type_)

class SessionParametersNotValidatedError(Exception):
    def __init__(self):
        self.message = 'The session parameters have not been validated.'

class InvalidSpaceParameterError(Exception):
    def __init__(self, space_type, param):
        self.message = 'Invalid parameter for space type {}: {}.'.format(space_type, param)

class InvalidExperimentsTypeError(Exception):
    def __init__(self, experiments_type):
        self.message = 'The experiments type {} is not valid.'.format(experiments_type)

class NextGenerationError(Exception):
    def __init__(self, gen):
        self.message = 'The next requested generation must be {}.'.format(gen)

class CsvFileEmptyError(Exception):
    def __init__(self, fname):
        self.message = 'No rows were found in the file {}.'.format(fname)

class CsvNoDataRowsError(Exception):
    def __init__(self, fname):
        self.message = 'No data rows were found in the file {}.'.format(fname)

class SpaceOrDesignRequiredError(Exception):
    def __init__(self):
        self.message = 'To generate random experiments you must supply experimental space or design.'


# Enums used by the DapticsClient class

@enum.unique
class DapticsTaskType(enum.Enum):
    """Enumerates the different asynchronous tasks that the daptics system can create and
    that can be searched for using the `poll_for_current_task` or `wait_for_current_task`
    methods.
    """

    SPACE = 'space'
    """The task type to be searched was created by the `put_experimental_parameters`
    or `put_experimental_parameters_csv` methods.
    """

    GENERATE = 'generate'
    """The task type to be searched was created by the `generate_design` method."""

    SIMULATE = 'simulate'
    """A task that simulates a given number of experimental generations."""

@enum.unique
class DapticsExperimentsType(enum.Enum):
    """Enumerates the purpose for the experiments that are being uploaded to the
    session via the `put_experiments` or `put_experiments_csv` methods.
    """

    INITIAL_EXTRAS_ONLY = 'initial'
    """The experiments submitted are initial experiments. No designed experiments are included."""

    DESIGNED_WITH_OPTIONAL_EXTRAS = 'designed'
    """The experiments submitted are designed experiments, and may also include optional
    extra experiments.
    """

    FINAL_EXTRAS_ONLY = 'final'
    """Not used in current API."""


# The main DapticsClient class
class DapticsClient(object):
    """A Python gql client for maintaining the state of a Daptics optimization session.
    Between API invocations, data such as the user id, access token, session id,
    last generated design, etc. are retained in the object's attributes.

    host (str):
        The host part of the API endpoint, as read from configuration, or set manually
        prior to calling `connect`.

    config (str):
        File path to a JSON configuration file, used to read the host, login credentials and
        runtime options. Defaults to `daptics.conf`. The keys in the JSON file are:

    `host` - host part of the API endpoint

    `user` - email of the database user to login with

    `password` - password for the database user to login with

    `auto_export_path` - see `options` below

    `auto_generate_next_design` - see `options` below

    `auto_task_timeout` - see `options` below

    If `config is set to None, configuration can be read from OS environment
    variables, if they exist. The environment variable names are:

    `DAPTICS_HOST` - host part of the API endpoint

    `DAPTICS_USER` - email of the database user to login with

    `DAPTICS_PASSWORD` - password for the database user to login with

    `DAPTICS_AUTO_EXPORT_PATH` - see `options` below

    `DAPTICS_AUTO_GENERATE_NEXT_DESIGN` - see `options` below

    `DAPTICS_AUTO_TASK_TIMEOUT` - see `options` below

    options (dict):
        A Python `dict` containing runtime options. As of this version, there
        are three available options:

    'auto_export_path` - If not None, a string indicating the relative or absolute directory
    where the validated experimental space and generated design files will be saved,
    so that the user will not have to explicitly call the `export` functions.

    `auto_generate_next_design` - If set (True), uploading (initial or later) experiment responses
    will automatically start a `generate` task for the next design generation. If not set
    (None or False), the uploading will only validate the responses, and the user
    will have to call the `generate` task manually after a successful validation.

    `auto_task_timeout` - If set to a positive number indicating the
    number of seconds to wait, this option will immediately start to wait on a
    just-created task, so that the user will not have to explicitly call
    `poll_for_current_task` or `wait_for_current_task`. Setting this option to a negative
    number, means to wait indefinitely. Setting the option to zero will poll the task
    just once. The default, None, means that the user wants to explicitly call
    `poll_for_current_task` or `wait_for_current_task`.
    """

    REQUIRED_SPACE_PARAMS = frozenset(('populationSize', 'replicates', 'space'))
    """The names of required experimental space parameters."""

    DEFAULT_CONFIG = './daptics.conf'
    """The default location for the option configuration file."""

    GET_ANALYTICS_TIMEOUT = 90
    """The default timeout for generating analytics files, in seconds."""

    def __init__(self, host=None, config=None):
        self.host = host
        """The host part of the API endpoint, as read from configuration, or set manually
        prior to calling `connect`.
        """

        self.config = config
        """The file path to the JSON configuration file used to read the host, login credentials and
        runtime options.
        """

        self.options = {
            'auto_export_path': None,
            'auto_generate_next_design': False,
            'auto_task_timeout': None
        }
        """A Python `dict` containing the runtime options."""

        self.credentials = None
        """A tuple of (`username`, `password`), as read from configuration, or set manually
        prior to calling `login`.
        """

        self.api_url = None
        """The full API endpoint URL."""

        self.pp = pprint.PrettyPrinter(indent=4)
        """A `pprint.PrettyPrinter` object used for printing Python `dict`s."""

        self.gql = None
        """The `gql.Client` object used to make GraphQL requests to the API."""

        self.auth = TokenAuth()
        """A `requests.auth` object used to insert the required authorization
        header in API requests. The auth object's `token` attribute is set by the `login` method.
        """

        self.user_id = None
        """The user id for the authenticated user, set by the `login` method."""

        self.session_id = None
        """The session id for a connected PDT session, as set by the `create_session` method."""

        self.task_info = {}
        """A Python `dict` that holds information about the polling status for
        running tasks in the session.
        """

        self.gen = -1
        """An integer storing the current design "generation number" for the session.
        This is -1 for a new session, 0 when the session's experimental space has been
        validated, and greater than zero when a design has been generated by the system.
        """

        self.remaining = None
        """If not None, an integer representing the number of possible generations that
        can be generated until the entire design space has been explored.
        """

        self.completed = False
        """A boolean indicating whether the design space has been completely explored."""

        self.initial_params = None
        """A Python `dict` containing the experimental space parameters defaults as
        initially returned by the `create_session` method.
        """

        self.validated_params = None
        """A Python `dict` containing the experimental space parameters as updated
        from the result of a "space" task.
        """

        self.design = None
        """A Python `dict` contining the current generated design, as updated by the
        result of a "generate" task.
        """

        self.experiments_history = None
        """A list of Python `dict`s containing all the experiments and responses that
        have been simulated, as updated by the result of a "simulate" task.
        """

    def print(self):
        """Print out debugging information about the session."""
        print('host = ', self.host)
        print('credentials = ', self.credentials)
        print('options = ', self.options)
        print('user_id = ', self.user_id)
        print('session_id = ', self.session_id)
        print('session_path = ', self.session_path)
        print('task_info = ', self.task_info)
        print('gen = ', self.gen)
        print('remaining = ', self.remaining)
        print('completed = ', self.completed)
        if self.validated_params is not None:
            print('Experimental Space Definition:')
            for x in self.validated_params:
                if x == 'space':
                    sp = self.validated_params[x]
                    for y in sp:
                        if y == 'table':
                            print('\t ESD Data:')
                            print('\t\t', sp['table']['colHeaders'])
                            for z in sp['table']['data']:
                                zz = [z[i] for i in range(len(z)) if z[i] != '']
                                print('\t\t', zz)
                        else:
                            print('\t', y, ':  ', sp[y])
                else:
                    print('\t', x, ':  ', self.validated_params[x])
        else:
            print('Experimental Space Definition: None')

        if self.design is not None:
            print('Design:')
            print(self.design['table']['colHeaders'])
            for dd in self.design['table']['data']:
                print(dd)
        else:
            print('Design: None')

        if self.experiments_history is not None:
            print('Experiments History:')
            max_gen = len(self.experiments_history)
            for gen, exp in enumerate(self.experiments_history):
                if exp is not None:
                    print('\tGeneration {}:'.format(gen))
                    print('\t', exp['table']['colHeaders'])
                    for dd in exp['table']['data']:
                        print('\t', dd)
                else:
                    print('\tGeneration {}: None'.format(gen))
        else:
            print('Experiments History: None')

    def call_api(self, document, vars, timeout=None):
        """Perform validation on the gql query or mutation document and then
        execute the query. We cannot call `self.gql.execute` directly, because it converts
        'errors' returned into an Exception. We want to preserve the 'errors'
        if they exist, and also return the data.

        # Arguments
        fname (str):
            The file path to save the client state to.

        # Returns
        (dict, dict):
            A tuple containing two `dicts`: The first element is the `data` component
            of the GraphQL response, a Python dict with `currentTask`, and the second
            element is the `errors` component of the GraphQL response. Either `data` or
            `errors` may be None.
        """

        if self.gql.schema:
            self.gql.validate(document)

        try:
            result = self.gql._get_result(document, variable_values=vars, timeout=timeout)
            return (result.data, result.errors)
        except Exception as e:
            return (None, [{'message': str(e)}])

    def error_messages(self, errors):
        """Extract the `message` values from the errors list returned in a GraphQL response.

        # Arguments
        errors (list):
            The list of GraphQL errors. Each error must have a `message` value, and
            can optionally have `key`, `path` and `locations` values.

        # Returns
        str or list:
            The message (or messages) extracted from the GraphQL response.
        """
        messages = []
        for e in errors:
            if e and 'message' in e:
                if 'key' in e:
                    messages.append('{} {}'.format(e['key'], e['message']))
                else:
                    messages.append(e['message'])

        if len(messages) == 0:
            return 'No error information is available.'
        elif len(messages) == 1:
            return messages[0]
        return messages

    def save(self, fname):
        """Save the user and session id to a JSON file.

        # Arguments
        fname (str):
            The file path to save the client state to.

        # Returns
        Nothing
        """
        with open(fname, 'w') as outfile:
            data = {
                'user_id': self.user_id,
                'token': self.auth.token,
                'session_id': self.session_id
            }
            json.dump(data, outfile, ensure_ascii=False, indent=4)

    def load(self, fname):
        """Restore a previously saved client from a JSON file.

        # Arguments
        fname (str):
            The file path to restore the client state from.

        # Returns
        Nothing
        """
        self.auth = TokenAuth()
        self.user_id = None
        self.session_id = None
        self.session_path = None
        self.task_info = {}
        self.gen = -1
        self.remaining = None
        self.completed = False
        self.initial_params = None
        self.validated_params = None
        self.design = None
        with open(fname, 'r') as infile:
            data = json.load(infile)
            if 'user_id' in data and data['user_id'] is not None:
                self.user_id = data['user_id']
                if 'token' in data and data['token'] is not None:
                    self.auth.token = data['token']
                if 'session_id' in data and data['session_id'] is not None:
                    self.session_id = data['session_id']

    def init_config(self):
        """Read in the client configuration from possible sources.

        # Returns
        Nothing

        # Raises
        MissingConfigError:
            If the config file specified does not exist.

        InvalidConfigError:
            If the config file specified cannot be parsed, or does not have a 'host'
            value.
        """
        config_path = os.path.abspath(DapticsClient.DEFAULT_CONFIG)
        config_must_exist = False
        if self.config:
            config_path = os.path.abspath(self.config)
            config_must_exist = True
            if not self.load_config_file(config_path, config_must_exist):
                self.load_config_env()

    def load_config_file(self, config_path, config_must_exit):
        if os.path.exists(config_path):
            try:
                with open(config_path) as f:
                    config = json.load(f)
                    self.config = config_path
                    if self.host is None:
                        self.host = config.get('host')
                    if self.credentials is None:
                        username = config.get('user')
                        password = config.get('password')
                        if username and password:
                            self.credentials = (username, password)
                    self.options['auto_export_path'] = config.get('auto_export_path', self.options['auto_export_path'])
                    self.options['auto_generate_next_design'] = config.get('auto_generate_next_design', self.options['auto_generate_next_design'])
                    self.options['auto_task_timeout'] = config.get('auto_task_timeout', self.options['auto_task_timeout'])
                    return True
            except:
                raise InvalidConfigError(config_path)
        elif config_must_exist:
            raise MissingConfigError(config_path)
        return False

    def load_config_env(self):
        if self.host is None:
            self.host = os.getenv('DAPTICS_HOST')
        if self.credentials is None:
            username = os.getenv('DAPTICS_USER')
            password = os.getenv('DAPTICS_PASSWORD')
            if username and password:
                self.credentials = (username, password)
        self.options['auto_export_path'] = os.getenv('DAPTICS_AUTO_EXPORT_PATH', default=self.options['auto_export_path'])
        auto_generate_next_design = os.getenv('DAPTICS_AUTO_GENERATE_NEXT_DESIGN')
        if auto_generate_next_design is not None:
            self.options['auto_generate_next_design'] = auto_generate_next_design.lower() in ("true", "t", "yes", "y", "on", "enabled", "1")
        auto_task_timeout = os.getenv('DAPTICS_AUTO_TASK_TIMEOUT')
        if auto_task_timeout is not None:
            self.options['auto_task_timeout'] = float(auto_task_timeout)

    def connect(self):
        """Read in the configuration and instantiate the client if it has not
        been done before. Creates an HTTP transport instance from the client's
        `api_url` attribute, and attempts to connect to the introspection interface.
        The gql.Client value is stored in the client's `gql` attribute.

        # Returns
        Nothing

        # Raises
        MissingConfigError:
            If the config file specified does not exist.

        InvalidConfigError:
            If the config file specified cannot be parsed, or does not have a 'host'
            value.

        NoHostError:
            If there is no config file specifed and no host has been set.

        requests.ConnectionError:
            If the connection cannot be made.
        """
        if self.gql is None:
            self.init_config()
            if self.host is None:
                raise NoHostError()
            self.api_url = '{0}/api'.format(self.host)
            http = gql.transport.requests.RequestsHTTPTransport(
                self.api_url, auth=self.auth, use_json=True)
            self.gql = gql.Client(transport=http, fetch_schema_from_transport=True)

    def login(self, email=None, password=None):
        """Authenticate to a user record in the database as identified in the client's
        `email` and `password` attributes, and create an access token.

        # Arguments
        email (str):
            The email adddress of the database user that will be used for authentication.
        password (str):
            The cleartext password of the database user that will be used for authentication.

        If called with default (`None`) arguments, the email and password will
        be retrieved from the `credentials` attribute.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `login` and/or
            `errors` keys. On successful authentication, the user id and access token
            are stored in the client's `user_id` and `auth` attributes.
        """

        if email is None or password is None:
            try:
                email, password = self.credentials
            except:
                raise NoCredentialsError()
        vars = {
            'email': email,
            'password': password
        }
        # print('Login on {} for user {}'.format(self.host, email), file=sys.stderr)

        # The 'login' mutation authenticates a user's email and password and returns
        # an access token that self.auth will then use to add an Authorization
        # header, required for session queries and mutations.
        doc = gql.gql("""
mutation Login($email:String!, $password:String!) {
    login(email:$email, password:$password) {
        token user {
            userId
        }
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)
        if 'login' in data and data['login'] is not None:
            self.auth.token = data['login']['token']
            self.user_id = data['login']['user']['userId']
        return data

    def create_session(self, name, description):
        """Create a new PDT session.

        # Arguments
        name (str):
            The unique name for the session among the authenticated user's sessions.
        description (str):
            A description for the session.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `createSession` and/or
            `errors` keys. On successful creation, the session id, session_path and
            initial parameters are stored in the client's attributes.
        """
        vars = {
            'session': {
                'userId': self.user_id,
                'name': name,
                'description': description,
                'demo': False
            }
        }

        # The 'createSession' mutation will add a new session to the backend's database,
        # copy runtime files to a fresh Rserve session directory on the Rserve filesystem,
        # start the session and return initial session information.
        doc = gql.gql("""
mutation CreateSession($session:NewSessionInput!) {
    createSession(session:$session) {
        sessionId version tag name description host path active demo campaign {
            gen remaining completed
        }
        params {
            validated populationSize replicates designCost space {
                type totalUnits table {
                    colHeaders data
                }
            }
        }
    }
}
        """)

        data, errors = self.call_api(doc, vars)
        if data and 'createSession' in data and data['createSession'] is not None:
            session = data['createSession']
            self.session_id = session['sessionId']
            self.session_path = session['path']
            self.gen = session['campaign']['gen']
            self.remaining = session['campaign']['remaining']
            self.completed = session['campaign']['completed']
            self.initial_params = session['params']
            if self.gen >= 0:
                self.validated_params = session['params']
            else:
                self.validated_params = None
            self.task_info = {}
            self.design = None
        else:
            print('Problem creating session!')
            print('Error: {}'.format(self.error_messages(errors)))
            print('Hint: session name may have already been taken, in which case choose another one.')
            return None

        return data

    def list_sessions(self, user_id=None, name=None):
        """Show a list of the user's sessions.

        # Arguments
        user_id (str):
            (optional) Limit the results to the user with this id. Omitting this argument
            is normal for regular users.
        name (str):
            (optional) Limit the results to any session whose name, description,
            `tag` or id contains this string.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `sessions` and/or
        `errors` keys.
        """
        vars = {
            'userId': user_id,
            'q': name
        }

        # The 'sessions' query will return a list of sessions.
        doc = gql.gql("""
query GetSessions($userId:String, $q:String) {
    sessions(userId:$userId, q:$q) { sessionId tag name description active demo }
}
        """)
        return self.gql.execute(doc, variable_values=vars)

    def reconnect_session(self, session_id):
        """Find an existing session.

        # Arguments
        session_id (str):
            The session id to find.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `session` and/or
            `errors` keys.
        """
        vars = {
            'sessionId': session_id
        }

        # The 'session' query will return the state of the session.
        doc = gql.gql("""
query GetSession($sessionId:String!) {
    session(sessionId:$sessionId) {
        sessionId version tag name description host path active demo campaign {
            gen remaining completed
        }
        params {
            validated populationSize replicates designCost space {
                type totalUnits table {
                    colHeaders data
                }
            }
        }
        experiments {
            gen validated hasResponses designRows table {
                colHeaders data
            }
        }
        tasks {
            taskId type description status startedAt
        }
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)
        if 'session' in data and data['session'] is not None:
            session = data['session']
            self.session_id = session['sessionId']
            self.session_path = session['path']
            self.gen = session['campaign']['gen']
            self.remaining = session['campaign']['remaining']
            self.completed = session['campaign']['completed']
            self.initial_params = session['params']
            if self.gen >= 0:
                self.validated_params = session['params']
            else:
                self.validated_params = None
            self.design = session['experiments']
        return data

    def halt_session(self, session_id):
        """Close an connected session, to release all resources.

        # Arguments
        session_id (str):
            The session id to close.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `haltSession` and/or
            `errors` keys. If the call is successful, the 'haltSession' value contains
            these keys:

        action (str):
            The action taken, either 'close' (if the session was connected) or 'none' if
            had already been closed.

        status (str):
            The session status, which should always be 'closed',
        """

        vars = {
            'sessionId': session_id
        }

        doc = gql.gql("""
mutation HaltSession($sessionId:String!) {
    haltSession(sessionId:$sessionId) {
        action status
    }
}
        """)
        return self.gql.execute(doc, variable_values=vars)

    def put_experimental_parameters(self, params):
        """Validate the experimental parameters at the beginning of a session,
        and start a "space" task. The individual experimental parameter names,
        types and permissible values in the space definition are specified at
        the `['space']['table']` key of the `params` dict.

        # Arguments
        params (dict):
            A Python `dict` containing the experimental parameters to be
            used for the session. See the Notes section that describes the
            required keys for the `params` dict.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `putExperimentalParameters` and/or
            `errors` keys.

        If the task was successfully started, the task information is stored in the client's
        `task_info` attribute. Also, if the `auto_task_timeout` option was set to a
        positive or negative number,  the task will be retried until a result is obtained
        or the task failed, or the timeout is exceeded.

        # Notes
        These are the required keys for the `params` dict:

        populationSize (int):
            The number of experiments per replicate. A positive integer.

        replicates (int):
            The number of replicates. A non-negative integer. The total number of
            experiments per design generation is `populationSize * (replicates + 1)`.

        space (dict):
            The experimental space definition. Required keys for the `space` dict are:

        type (str):
            The type of the space, a string, either "factorial" or "mixture".

        totalUnits (int):
            For `mixture` type spaces, this is the mixture constraint parameter,
            a non-negative integer.

        table (dict):
            The (optional) column headers and rows of parameter data.  See
            an example below. the `colHeaders` value is ignored when importing
            or validating the experimental space definition.

        To maintain uniformity, header and data row elements should be
        Python strings, even if they represent numeric values.

        For `mixture` type spaces, there should only be 4 columns of data
        in each row: the name of the parameter, the type of the parameter
        (which must always be the string "unit"), the minimum value of the
        parameter (a non-negative integer) and the maximum value of the
        parameter (a positive integer, less than or equal to the `totalUnits`
        constraint parameter).

        For `factorial` type spaces, there must be at least 4 columns of data
        in each row: the name of the parameter, the type of the parameter
        (a string, either "numerical" or "categorical"), and at least
        two possible distinct values that the parameter can have in an experiment.
        Different parameters can have either 2 or more than 2 possible values.
        The rows must be all be of the same size, so make sure to pad the
        rows with fewer values with empty strings at the end.

        In addition to the required `params` listed above, optional additional
        parameters may be submitted. Please contact daptics for more information
        about these advanced parameters.

        # Examples
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
        """

        col_headers = self.space_table_column_names(params['space'])
        params['space']['table']['colHeaders'] = col_headers

        # Split off additional params, format them and add them to the required params.
        params_ = {key: params[key] for key in (params.keys() & DapticsClient.REQUIRED_SPACE_PARAMS)}
        additional_params = [{'name': key, 'jsonValue': json.dumps(params[key])} for key in (params.keys() - DapticsClient.REQUIRED_SPACE_PARAMS)]
        params_['additionalParams'] = additional_params

        vars = {
            'sessionId': self.session_id,
            'params': params_
        }

        # The 'putExperimentalParameters' mutation must be run to validate the
        # user's experimental design. The mutation will return errors if the
        # parameters or space are not valid (don't generate enough complexity, etc.).
        # If the parameters are valid, information about the long running 'space'
        # task is returned, and the user should poll until the task has completed.
        doc = gql.gql("""
mutation PutExperimentalParameters($sessionId:String!, $params:SessionParametersInput!) {
    putExperimentalParameters(sessionId:$sessionId, params:$params) {
        sessionId taskId type description status startedAt
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)
        if 'putExperimentalParameters' in data and data['putExperimentalParameters'] is not None:
            task_id = data['putExperimentalParameters']['taskId']
            self.task_info[task_id] = data['putExperimentalParameters']
            auto_task, errors = self.do_auto_task()
            if auto_task is not None:
                return {'putExperimentalParameters': auto_task, 'errors': errors}
        return data

    def put_experimental_parameters_csv(self, fname, params):
        """Validate the experimental parameters at the beginning of a session,
        and start a "space" task. The individual experimental parameter names,
        types and permissible values in the space definition are read from a CSV file.

        # Arguments
        fname (str):
            The location on the filesystem for a CSV file that will define
            the experimental space definition. See the Examples section
            below for an example.

        params (dict):
            A Python `dict` containing the experimental parameters to be
            used for the session. See the Notes section for more information.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `putExperimentalParameters` and/or
            `errors` keys.

        If the task was successfully started, the task information is stored in the client's
        `task_info` attribute. Also, if the `auto_task_timeout` option was set to a
        positive or negative number,  the task will be retried until a result is obtained
        or the task failed, or the timeout is exceeded.

        # Raises
        csv.Error:
            If the specified CSV file is incorrectly formatted.

        # Notes
        Keys for the `params` dict are:

        populationSize (int):
            The number of experiments per replicate. A positive integer.

        replicates (int):
            The number of replicates. A non-negative integer. The total number of
            experiments per design generation is `populationSize * (replicates + 1)`.

        space (dict):
            The experimental space definition. The single required key for the `space` dict is:

        type (str):
            `factorial` or `mixture`

        In addition to the required `params` listed above, optional additional
        parameters may be submitted. Please contact daptics for more information
        about these advanced parameters.

        # Examples
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

        The contents of an example CSV file for a `factorial` space might be:

        ```
        param1,numerical,0,1,2,3
        param2,numerical,2,3,4,
        param3,numerical,0,1,,
        param4,numerical,0,1,2,3
        ```

        Each parameter row in a factorial space definition should have the same
        number of columns.  Parameter rows with fewer than the maximum number of values
        should have the empty columns at the end of the row, as shown above.

        The contents of an example CSV file for a `mixture` space might be:

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
        """

        param_rows = []
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            param_rows = [r for r in reader]
        params['space']['table'] = { 'data': param_rows }
        return self.put_experimental_parameters(params)

    def get_experiments(self, design_only=False, gen=None):
        """Get the designed or completed experiments for the current or any
        previous generation.

        # Arguments
        design_only (bool):
            If gen is specified, and this argument is set to `True`, only
            return the designed experiments (without responses).

        gen (int):
            The generation number to search for. Use 0 to specify initial
            experiments. Use None to search for the last designed generation.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `experiments` and/or
            `errors` keys. The value at the `experiments` key is a Python
            dict with these keys:

        validated (bool):
            True if these experiments have been validated.

        hasResponses (bool):
            True if at least some of these experiments have responses.

        designRows (int):
            The number of rows of experiments that were designed. Rows after the `designRows`
            are "extra" experiments.

        table (dict):
            A Python dict with `colHeaders` and `data` values, representing the
            experiments submitted or designed for the generation.
        """

        vars = {
            'sessionId': self.session_id,
            'designOnly': False
        }
        if gen is not None:
            vars['gen'] = gen
            if design_only:
                vars['designOnly'] = True

        doc = gql.gql("""
query GetExperiments($sessionId:String!, $designOnly:Boolean!, $gen:Int){
    experiments(sessionId:$sessionId, designOnly:$designOnly, gen:$gen) {
        gen validated hasResponses designRows table {
            colHeaders data
        }
    }
}
        """)
        return self.gql.execute(doc, variable_values=vars)

    def get_experiments_history(self):
        """Get all of the experiments and any responses for all the generations in the session.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `experimentsHistory` and/or
            `errors` keys. Also updates the client's `experiments_history` attribute.
            The `experimentsHistory` value is either None if no experiments have been submitted or
            designed, or a list. Each item in the list is either None, or a Python dict that
            represents a generation. The first item in the list is generation "zero",
            the initial experiments. If a generation is available (non None), it is a Python
            dict with the following keys:

        gen (int):
            The generation number (zero meaning initial experiments).

        validated (bool):
            True if these experiments have been validated.

        hasResponses (bool):
            True if at least some of these experiments have responses.

        designRows (int):
            The number of rows of experiments that were designed. Rows after the `designRows`
            are "extra" experiments.

        table (dict):
            A Python dict with `colHeaders` and `data` values, representing the
            experiments submitted or designed for the generation.
        """

        vars = {
            'sessionId': self.session_id
        }
        doc = gql.gql("""
query GetExperimentsHistory($sessionId:String!){
    experimentsHistory(sessionId:$sessionId) {
        gen validated hasResponses designRows table {
            colHeaders data
        }
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)

        if 'experimentsHistory' in data:
            self.experiments_history = data['experimentsHistory']
        return data

    def get_generated_design(self, gen=None):
        """Retrieves a design generation from the session.

        # Arguments
        gen (int):
            The generation number for the design to be retrieved.
            If None, retreive the design for the current generation.

        # Returns
        dict:
            The value of the `experiments` key from the GraphQL response,
            a Python dict with these keys:

        validated (bool):
            True if these experiments have been validated.

        hasResponses (bool):
            True if at least some of these experiments have responses.

        designRows (int):
            The number of rows of experiments that were designed. Rows after the `designRows`
            are "extra" experiments.

        table (dict):
            A Python dict with `colHeaders` and `data` values, representing the
            experiments submitted or designed for the generation.
        """

        data = self.get_experiments(design_only=True, gen=gen)
        return data['experiments']

    def simulate_experiment_responses(self, experiments = None):
        """Generate values for the "Response" column.  The values are a
        substitute for actual experimental results, computed with a
        synthetic data generator that takes as an input each
        experiment (i.e. each row of the experiments argument) and
        gives as output a single number, added as a 'Response'.  The
        data generator samples a complex surface, constructed to have
        several peaks that are randomly placed in the space.  There is
        a global optimum (highest peak), but optimization runs often
        will find one of the lower peaks.

        # Arguments
        experiments (dict):
            A "table" of experiments that includes columns,
            defined in the `colHeaders` value of the table, for each of the defined
            space parameters, and a column named 'Response' to record the result of
            experiments.

            Each row in the `data` value for the table represents
            an individual experiment.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with
            `simulateExperiments` and/or `errors` keys.
        """

        vars = {
            'sessionId': self.session_id
        }
        if experiments is not None:
            vars['experiments'] = experiments

        # A 'simulateResponses' mutation may supply an `experiments` table.
        doc = gql.gql("""
mutation SimulateResponses($sessionId:String!, $experiments:DataFrameInput) {
    simulateResponses(sessionId:$sessionId, experiments:$experiments) {
        gen validated hasResponses designRows table {
            colHeaders data
        }
    }
}
        """)
        return self.gql.execute(doc, variable_values=vars)

    def simulate_experiment_responses_csv(self, fname):
        """Generate values for the "Response" column.  The values are a
        substitute for actual experimental results, computed with a
        synthetic data generator that takes as an input each
        experiment (i.e. each row of the experiments argument) and
        gives as output a single number, added as a 'Response'.  The
        data generator samples a complex surface, constructed to have
        several peaks that are randomly placed in the space.  There is
        a global optimum (highest peak), but optimization runs often
        will find one of the lower peaks.

        # Arguments
        fname (str):
            The location on the filesystem for a CSV file that will define
            the parameters for designed and any extra experiments.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with
            `simulateExperiments` and/or `errors` keys.
        """

        experiments = None
        header_and_experiments = []
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header_and_experiments = [r for r in reader]
        if len(header_and_experiments) > 1:
            experiments = {
                'colHeaders': header_and_experiments[0],
                'data': header_and_experiments[1:]
            }
        else:
            raise CsvNoDataRowsError(fname)
        return self.simulate_experiment_responses(experiments)

    def put_experiments(self, experiments_type, experiments):
        """Validate the responses for designed experiments, and any extra experiments
        for the current generation in the session. This method, or the
        `put_experiments_responses_csv` method, must be called before generating the
        next design, or finalizing the campaign.

        # Arguments
        experiments_type (DapticsExperimentsType):
            Describes the types of experiments that are being added to the session.

        If you wish to submit calibrating or existing experimental responses prior
        to the first design generartion, use `INITIAL_EXTRAS_ONLY`.

        If you are submitting the responses for a daptics-generated design, along
        with any extra experiments, use `DESIGNED_WITH_OPTIONAL_EXTRAS`.

        If you wish to submit any final extra experiments when you are satisified
        with the session's optimization but do not want to include the last
        generated experimental design use `FINAL_EXTRAS_ONLY`. Note that this
        will end the session's optimization and that no more designs will be
        generated.

        experiments (dict):
            A "table" of experiments that includes columns,
            defined in the `colHeaders` value of the table, for each of the defined
            space parameters, and a column named 'Response' to record the result of
            experiments.

        Each row in the `data` value for the table represents
        an individual experiment.

        If the `experiments type` is `DESIGNED_WITH_OPTIONAL_EXTRAS`,
        you must sumbit at least as many rows as exist in the currently
        generated design, and the parameter values for these rows
        must match the design exactly. Additional "extra" experiment
        rows, that use any valid experimental parameter values, can also
        be provided.

        For the `INITIAL_EXTRAS_ONLY` and `FINAL_EXTRAS_ONLY` experiments types,
        rows that use any valid experimental parameter values can be provided.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `putExperiments` and/or
            `errors` keys.

        If the experiments were successfully validated, the following actions may be
        automatically performed:

        If the `auto_export_path` option is set, a CSV file of the validated experiments
        is saved at `auto_genN_experiments.csv`.

        If the `auto_generate_next_design` option is set, a `generate`
        task is started, and the `task` key of the `putExperiments` key will contain
        information on the task.

        If the `auto_generate_next_design` AND `auto_task_timeout` options are set,
        this method will block as the task is polled until it succeeds, fails, or
        the timeout value is exceeded.

        # Examples
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
        """

        if type(experiments_type) != DapticsExperimentsType:
            raise InvalidExperimentsTypeError(experiments_type)

        vars = {
            'sessionId': self.session_id,
            'experiments': {
                'type': experiments_type.value,
                'gen': self.gen,
                'table': experiments
            }
        }

        # A 'putExperiments' mutation for a designed generation ('gen' > 0) requires
        # responses for the designed generation (and any optional additional non-designed
        # experiments and their responses), sent in the 'table' variable.
        # If the generation number and saved responses are valid, information
        # about the long running 'generate' task is returned, and the user should
        # poll until the task has completed.
        doc = gql.gql("""
mutation PutExperiments($sessionId:String!, $experiments:ExperimentsInput!) {
    putExperiments(sessionId:$sessionId, experiments:$experiments) {
        gen validated hasResponses designRows table {
            colHeaders data
        }
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)
        if 'putExperiments' in data and data['putExperiments'] is not None:
            auto_export_path = self.options.get('auto_export_path')
            if auto_export_path is not None:
                fname = os.path.join(auto_export_path, 'auto_gen{0}_experiments.csv'.format(self.gen))
                self.export_csv(fname, data['putExperiments']['table'], True)

            if self.options.get('auto_generate_next_design'):
                if self.remaining is None or self.remaining > 0:
                    task_data = self.generate_design()
                    data['putExperiments']['task'] = task_data['generateDesign']
        return data

    def put_experiments_csv(self, experiments_type, fname):
        """Validate the responses for designed experiments, and any extra experiments
        for the current generation in the session. This method, or the
        `put_experiments_responses` method, must be called before generating the
        next design, or finalizing the campaign.

        # Arguments
        experiments_type (DapticsExperimentsType):
            Describes the types of experiments that are being added to the session.

        If you wish to submit calibrating or existing experimental responses prior
        to the first design generartion, use `INITIAL_EXTRAS_ONLY`.

        If you are submitting the responses for a daptics-generated design, along
        with any extra experiments, use `DESIGNED_WITH_OPTIONAL_EXTRAS`.

        If you wish to submit any final extra experiments when you are satisified
        with the session's optimization but do not want to include the last
        generated experimental design use `FINAL_EXTRAS_ONLY`. Note that this
        will end the session's optimization and that no more designs will be
        generated.

        fname (str):
            The location on the filesystem for a CSV file that will define
            the results of the designed and any extra experiments. See the Examples section
            below for an example.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `putExperiments` and/or
            `errors` keys.

        If the experiments were successfully validated, the following actions may be
        automatically performed:

        If the `auto_export_path` option is set, a CSV file of the validated experiments
        is saved at `auto_genN_experiments.csv`.

        If the `auto_generate_next_design` option is set, a `generate`
        task is started, and the `task` key of the `putExperiments` key will contain
        information on the task.

        If the `auto_generate_next_design` AND `auto_task_timeout` options are set,
        this method will block as the task is polled until it succeeds, fails, or
        the timeout value is exceeded.

        # Examples
        A header row must be provided, the columns in the header row
        must match the names of the parameters defined by the experimental space definition
        exactly, and a final column named `Response` must be filled with the results
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
        """
        experiments = { 'colHeaders': '', 'data': [] }
        header_and_experiments = []
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header_and_experiments = [r for r in reader]
        if len(header_and_experiments) > 1:
            experiments['colHeaders'] = header_and_experiments[0]
            experiments['data'] = header_and_experiments[1:]
        else:
            raise CsvNoDataRowsError(fname)
        return self.put_experiments(experiments_type, experiments)

    def generate_design(self, gen = None):
        """If (initial or subsequent) experiments have been successfully validated against the
        experimental parameters, a "generate design" task is started.

        # Arguments
        gen:
            The current generation number for the experiments that have successfully validated.
            Use zero for initial experiments. Use `None` to use the `gen` attribute stored
            in the client.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `generateDesign` and/or
            `errors` keys.

        If the task was successfully started, the task information is stored in the client's
        `task_info` attribute. Also, if the `auto_task_timeout` option was set to None
        or a positive number,  the task will be retried until a result is obtained
        or the task failed.
        """

        current_gen = self.gen if gen is None else gen
        vars = {
            'sessionId': self.session_id,
            'gen': current_gen
        }

        # The 'generateDesign' mutation sends any initial or designed experiment
        # responses. For this demo we don't send any initial experiments.
        # If the generation number and saved responses are valid, information
        # about the long running 'generate' task is returned, and the user should
        # poll until the task has completed.
        doc = gql.gql("""
mutation GenerateDesign($sessionId:String!, $gen:Int!) {
    generateDesign(sessionId:$sessionId, gen:$gen) {
        sessionId taskId type description status startedAt
    }
}
        """)

        data, errors = self.call_api(doc, vars)
        if errors:
            # This is what gql does with errors
            raise Exception(str(errors[0]))

        if 'generateDesign' in data and data['generateDesign'] is not None:
            task_id = data['generateDesign']['taskId']
            self.task_info[task_id] = data['generateDesign']
            auto_task, errors = self.do_auto_task()
            if auto_task is not None:
                return {'generateDesign': auto_task, 'errors': errors}
        return data

    def start_simulation(self, ngens, params):
        """Start a simulation task for several design generations, specifying the
        desired experimental parameters and the number of generations
        to run.

        # Arguments
        ngens (int):
            The number of generations to attempt to design. Must be greater than zero.
            If the experimental space is exhausted the actual number of generations
            designed may be less than this number.

        params (dict):
            A Python `dict` containing the experimental parameters to be
            used for the session. See the Notes section that describes the
            required keys for the `params` dict.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `runSimulation` and/or
            `errors` keys.

        If the task was successfully started, the task information is stored in the client's
        `task_info` attribute. Also, if the `auto_task_timeout` option was set to a
        positive or negative number,  the task will be retried until a result is obtained
        or the task failed, or the timeout is exceeded.

        # Notes
        For more examples of how to submit space parameters, please
        see the documentation for the `put_experimental_parameters` method.
        Keys for the `params` dict are:

        populationSize (int):
            The number of experiments per replicate. A positive integer.

        replicates (int):
            The number of replicates. A non-negative integer. The total number of
            experiments per design generation is `populationSize * (replicates + 1)`.

        space (dict):
            The experimental space definition. Keys for the `space` dict are:

        type (str):
            The type of the space, a string, either "factorial" or "mixture".

        totalUnits (int):
            For `mixture` type spaces, this is the mixture constraint parameter,
            a non-negative integer.

        table (dict):
            The (optional) column headers and rows of parameter data.  See
            an example below. the `colHeaders` value is ignored when importing
            or validating the experimental space definition.
        """

        vars = {
            'sessionId': self.session_id,
            'ngens': ngens,
            'params': params
        }

        doc = gql.gql("""
mutation RunSimulation($sessionId:String!, $ngens:Int!, $params:SessionParametersInput!) {
    runSimulation(sessionId:$sessionId, ngens:$ngens, params:$params) {
        sessionId taskId type description status startedAt
    }
}
        """)
        data = self.gql.execute(doc, variable_values=vars)
        if 'runSimulation' in data and data['runSimulation'] is not None:
            task_id = data['runSimulation']['taskId']
            self.task_info[task_id] = data['runSimulation']
            auto_task, errors = self.do_auto_task()
            if auto_task is not None:
                return {'runSimulation': auto_task, 'errors': errors}
        return data

    def start_simulation_csv(self, ngens, fname, params):
        """Run a simulation for several design generations, specifying the
        desired experimental parameters and the number of generations to run.
        The experimental space is read from a CSV file. If the space parameters
        are successfully validated a "simulate" task is started.

        # Arguments
        ngens (int):
            The number of generations to attempt to design. Must be greater than zero.
            If the experimental space is exhausted the actual number of generations
            designed may be less than this number.

        fname (str):
            The location on the filesystem for a CSV file that will define
            the experimental space definition. See the Examples section
            below for an example.

        params (dict):
            A Python `dict` containing the experimental parameters to be
            used for the session.  See the Notes section that describes the
            required keys for the `params` dict.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `runSimulation` and/or
            `errors` keys.

        If the task was successfully started, the task information is stored in the client's
        `task_info` attribute. Also, if the `auto_task_timeout` option was set to a
        positive or negative number,  the task will be retried until a result is obtained
        or the task failed, or the timeout is exceeded.

        # Raises
        csv.Error:
            If the specified CSV file is incorrectly formatted.

        # Notes
        For more examples of how to submit space parameters, please
        see the documentation for the `put_experimental_parameters` method.
        Keys for the `params` dict are:

        populationSize (int):
            The number of experiments per replicate. A positive integer.

        replicates (int):
            The number of replicates. A non-negative integer. The total number of
            experiments per design generation is `populationSize * (replicates + 1)`.

        space (dict):
            The experimental space definition. Keys for the `space` dict are:

        type (str):
            The type of the space, a string, either "factorial" or "mixture".

        totalUnits (int):
            For `mixture` type spaces, this is the mixture constraint parameter,
            a non-negative integer.
        """

        param_rows = []
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            param_rows = [r for r in reader]
        params['space']['table'] = { 'data': param_rows }
        return self.start_simulation(ngens, params)

    def poll_for_current_task(self, task_type=None):
        """If there is a currently running task saved in the client, poll the
        session to see if a result is ready.

        # Arguments
        task_type (DapticsTaskType):
            `SPACE`, `GENERATE`, or None. If None is supplied (the default), find
            the most recently started task of any type.

        # Returns
        (dict, dict):
            A tuple containing two `dicts`: The first element is the `data` component
            of the GraphQL response, a Python dict with `currentTask`, and the second
            element is the `errors` component of the GraphQL response. Either `data` or
            `errors` may be None.

        If the current task was a "save experimental space" task and it successfully completed,
        the client's `gen` attribute is set to zero.

        If the current task was a "generate design" task and it successfully completed,
        the client's `gen` attribute is updated to a number greater than zero, and the
        design is stored in the client's `design` attribute.
        """

        vars = {
            'sessionId': self.session_id,
            'taskId': None,
            'type': None
        }
        if task_type is not None:
            if type(task_type) == DapticsTaskType:
                vars['type'] = task_type.value
            else:
                raise InvalidTaskTypeError(task_type)


        # Saving the experimental and space parameters will start a long running
        # 'space' task. Saving experimental responses will start a long running
        # 'generate' task. This function queries the backend to check the status
        # of the task based on the task type. If the task is still running, we
        # do nothing. If no task is found, or if the task has failed, we assert
        # an error. If the task has completed, we update self.gen
        # for 'space' and 'generate' task results, and save self.design
        # from a 'generate' task result.
        doc = gql.gql("""
query CurrentTask($sessionId:String!, $taskId:String, $type:String) {
    currentTask(sessionId:$sessionId, taskId:$taskId, type:$type) {
        taskId type description status startedAt progress {
            message
        }
        errors {
            message category fatalError systemError
        }
        result {
            ... on SpaceTaskResult {
                type campaign {
                    gen remaining completed
                }
                params {
                    validated populationSize replicates designCost space {
                        type totalUnits table {
                            colHeaders data
                        }
                    }
                }
            }
            ... on GenerateTaskResult {
                type campaign {
                    gen remaining completed
                }
                params {
                    validated populationSize replicates designCost space {
                        type totalUnits table {
                            colHeaders data
                        }
                    }
                }
                experiments {
                    gen validated hasResponses designRows table {
                        colHeaders data
                    }
                }
            }
            ... on UpdateTaskResult {
                type campaign {
                    gen remaining completed
                }
                params {
                    validated populationSize replicates designCost space {
                        type totalUnits table {
                            colHeaders data
                        }
                    }
                }
                experiments {
                    gen validated hasResponses designRows table {
                        colHeaders data
                    }
                }
            }
            ... on SimulateTaskResult {
                type campaign {
                    gen remaining completed
                }
                params {
                    validated populationSize replicates designCost space {
                        type totalUnits table {
                            colHeaders data
                        }
                    }
                }
                experimentsHistory {
                    gen validated hasResponses designRows table {
                        colHeaders data
                    }
                }
            }
        }
    }
}
        """)

        data, errors = self.call_api(doc, vars)
        if data and 'currentTask' in data and data['currentTask'] is not None:
            if 'status' in data['currentTask'] and 'type' in data['currentTask']:
                # A task's status can be 'new', 'running', 'success', 'error', or 'canceled'
                task_id = data['currentTask']['taskId']
                self.task_info[task_id] = data['currentTask']
                status = data['currentTask']['status']
                type_ = data['currentTask']['type']
                if status == 'new' or status == 'running':
                    # We will try again
                    pass
                elif status == 'canceled':
                    # Message will be in response error
                    # TESTME: will we ever get here, or will exception be thrown first?
                    pass
                elif status == 'error':
                    # Message will be in response error
                    # TESTME: will we ever get here, or will exception be thrown first?
                    pass
                elif status == 'success':
                    if 'result' in data['currentTask'] and data['currentTask']['result'] is not None:
                        auto_export_path = self.options.get('auto_export_path')
                        result = data['currentTask']['result']
                        if type_ == 'space':
                            self.gen = result['campaign']['gen']
                            self.remaining = result['campaign']['remaining']
                            self.completed = result['campaign']['completed']
                            self.validated_params = result['params']
                            if auto_export_path is not None:
                                fname = os.path.join(auto_export_path, 'auto_validated_space.csv')
                                self.export_csv(fname, self.validated_params['space']['table'], False)
                        elif type_ == 'generate':
                            self.gen = result['campaign']['gen']
                            self.remaining = result['campaign']['remaining']
                            self.completed = result['campaign']['completed']
                            self.design = result['experiments']
                            if auto_export_path is not None:
                                fname = os.path.join(auto_export_path, 'auto_gen{0}_design.csv'.format(self.gen))
                                self.export_csv(fname, self.design['table'], True)
                        elif type_ == 'simulate':
                            self.gen = result['campaign']['gen']
                            self.remaining = result['campaign']['remaining']
                            self.completed = result['campaign']['completed']
                            self.validated_params = result['params']
                            self.experiments_history = result['experimentsHistory']
                            if auto_export_path is not None:
                                fname = os.path.join(auto_export_path, 'auto_history.csv')
                                self.export_experiments_history_csv(fname)
        else:
            data = {'currentTask': None}
        return (data, errors)

    def wait_for_current_task(self, task_type=None, timeout=None):
        """Wraps poll_for_current_task in a loop. Repeat until task disappears,
        when `status` is `success` or `failure`.

        # Arguments
        task_type (DapticsTaskType):
            `SPACE`, `GENERATE`, or None. If None is supplied (the default), find
            the most recently started task of any type.

        timeout (float):
            Maximum number of seconds to wait. If None or a negative number, wait forever.

        # Returns
        (dict, dict):
            A tuple containing two `dicts`: The first element is the `data` component
            of the GraphQL response, a Python dict with `currentTask`, and the second
            element is the `errors` component of the GraphQL response. Either `data` or
            `errors` may be None.

        If the current task was a "save experimental space" task and it successfully completed,
        the client's `gen` attribute is set to zero.

        If the current task was a "generate design" task and it successfully completed,
        the client's `gen` attribute is updated to a number greater than zero, and the
        design is stored in the client's `design` attribute.

        If either type of task completed or failed, the client's `current_task` attribute
        is reset to None.
        """
        max_time = None
        if timeout is not None and timeout >= 0:
            if timeout == 0:
                timeout = -1.0
            max_time = time.time() + timeout

        retry = 0
        while True:
            data, errors = self.poll_for_current_task(task_type)
            if data and 'currentTask' in data and data['currentTask'] is not None:
                status = data['currentTask']['status']
                if status == 'canceled':
                    if retry > 0:
                        sys.stdout.write('\n')
                    print('Task was canceled!  Messages are:')
                    errors = data['currentTask']['errors']
                    for ee in errors[0]:
                        print(ee, '\t', errors[0][ee])
                    return (data, errors)
                elif status == 'error':
                    if retry > 0:
                        sys.stdout.write('\n')
                    print('Task had an error!  Messages are:')
                    errors = data['currentTask']['errors']
                    for ee in errors[0]:
                        print(ee, '\t', errors[0][ee])
                    return (data, errors)
                elif status == 'success':
                    if retry > 0:
                        sys.stdout.write('\n')
                    print('Task completed!')
                    return (data, errors)

                # status == 'new' or status == 'running'
                retry += 1
                mystr = '\rTask status = {} after {} retries...'.format(status, retry)
                sys.stdout.write(mystr)
                if max_time is not None and max_time <= time.time():
                    sys.stdout.write('\nTimed out.')
                    if errors is None:
                        errors = []
                    errors.append({ 'message': 'timeout exceeded' })
                    return (data, errors)

                # We will try again
                time.sleep(1.0)
            else:
                sys.stdout.write('\nNo current task was found!')
                return (data, errors)

    def do_auto_task(self):
        """Calls wait_for_current_task if the `auto_task_timeout` option was set.

        # Arguments
        timeout (float):
            Maximum number of seconds to wait. If a negative number, wait forever.

        # Returns
        (dict, dict):
            A tuple containing two `dicts`: The first element is the `currentTask` component,
            and the second element is the `errors` component of the GraphQL response. Either
            `currentTask` (for example on timeout) or `errors` may be None.
        """

        timeout_option = self.options.get('auto_task_timeout')
        if timeout_option is not None:
            data, errors = self.wait_for_current_task(task_type=None, timeout=timeout_option)
            if errors:
                # This is what gql does with errors
                raise Exception(str(errors[0]))
            return (data['currentTask'], errors)
        else:
            return (None, None)

    def get_experimental_space(self):
        """Utility method to retrieve the validated experimental space from
        the session. If the session was restarted and the experimental space
        had been previously validated, it will be in the `validated_params`
        attribute, and this method will return it.

        # Arguments
        None

        # Returns
        dict:
            The validated space, a Python dict with `type`, and `table` keys, and
            a `totalUnits` key if the space type is "mixture", or None if
            the space has not been validated.
        """

        if self.validated_params is not None:
            return self.validated_params['space']

        return None

    def get_analytics_file_list(self, timeout=None):
        """Get a list of the available analytics files for the session.

        # Arguments
        timeout (int):
            The maximum number of seconds that the client will wait for a
            response from the session. The default is 90 seconds.

        # Returns
        dict:
            The JSON response from the gql request, a Python dict with `createAnalytics` and/or
            `errors` keys. If there are any files available, they will be returned in the
            `createAnalytics` value as a Python dict. The `createAnalytics` dict will have
            two keys:

        gen (int):
            The current generation number in the session, for which the files were created.

        files (list):
            A list of the availiable files. Each file is represented by a Python dict
            with the following keys:

        title (str):
            The title (description) for the file.

        filename (str):
            The default file name that can be passed to the `get_analytics_file` method.

        url (str):
            The public URL from which to fetch the file.
        """

        vars = {
            'sessionId': self.session_id,
        }

        # The 'createAnalytics' mutation generates PDF files on the Rserve
        # server, and returns the titles and file names for these PDF files.
        # To download one or more of these files, another query (not tested here)
        # will be used.
        doc = gql.gql("""
mutation CreateAnalytics($sessionId:String!) {
    createAnalytics(sessionId:$sessionId) {
        gen files {
            title filename url
        }
    }
}
        """)
        if timeout is None:
            timeout = DapticsClient.GET_ANALYTICS_TIMEOUT
        return self.gql.execute(doc, variable_values=vars, timeout=timeout)

    def get_analytics_file(self, url, save_as=None):
        """Fetch the contents of an analytics file. Once a URL to a particular analytics file
        has been obtained using the `get_analytics` method, use this method to request the
        file's contents over HTTP.

        # Arguments
        url (str):
            The URL for the file, as returned from `get_analytics` method.

        save_as (str):
            If supplied, save the file's contents to this file system location.
            The location must be writable by the calling user.

        # Returns
        requests.Response:
            The `requests` library's `response` object for the authenticated HTTP request.
        """

        # Access token is added as query string
        params = {}
        if self.auth and self.auth.token:
            params['token'] = self.auth.token
        response = requests.get(url, params=params)
        if save_as is not None and response.status_code == requests.codes.ok and response.content is not None:
            with open(save_as, "wb") as pdf_file:
                pdf_file.write(response.content)
        return response

    def get_all_analytics_files(self, directory=".", timeout=None):
        """For each available analytics file, fetch its contents and save it as a file in the
        specified directory.

        # Arguments
        directory (str):
            If supplied, the target directory to save the files to. If the directory
            does not exist, attempt to create it.

        timeout (int):
            The maximum number of seconds that the client will wait for a
            response from the session. The default is 90 seconds.

        # Returns
        int:
            The number of files created.
        """

        nfiles = 0
        path = os.path.abspath(directory)
        if timeout is None:
            timeout = DapticsClient.GET_ANALYTICS_TIMEOUT
        data = self.get_analytics_file_list(timeout=timeout)
        if 'createAnalytics' in data:
            # Access token is added as query string
            params = {}
            if self.auth and self.auth.token:
                params['token'] = self.auth.token
            for file_info in data['createAnalytics']['files']:
                response = requests.get(file_info['url'], params=params)
                if response.status_code == requests.codes.ok and response.content is not None:
                    if nfiles == 0:
                        os.makedirs(path, exist_ok=True)
                    save_as = os.path.join(path, file_info['filename'])
                    with open(save_as, "wb") as pdf_file:
                        pdf_file.write(response.content)
                        nfiles += 1

        return nfiles

    def export_csv(self, fname, table, headers=True):
        """Utility method to write an expeimental space or experiments table to
        a CSV file on disk.

        # Arguments
        fname (str):
            The filesystem path where the file will be written.

        table (dict):
            A Python dict with `colHeaders` and `data` values, representing an
            experimental space or experiments table.

        headers (bool):
            If False, no header row will be written (this is the standard for
            experimental space CSV files). If True, the header row will be
            written to the file.

        # Returns
        Nothing
        """

        if table is not None and 'data' in table:
            with open(fname, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
                if headers and 'colHeaders' in table and table['colHeaders'] is not None:
                    writer.writerow(table['colHeaders'])
                if table['data'] is not None:
                    for row in table['data']:
                        writer.writerow(row)

    def export_experimental_space_csv(self, fname):
        """Retrieves the validated experimental space table and writes the table to
        a CSV file on disk.

        # Arguments
        fname (str):
            The filesystem path where the file will be written.

        # Returns
        dict:
            A Python dict representing the validated experimental space.
        """

        space = self.get_experimental_space()
        if space is None:
            raise SessionParametersNotValidatedError()

        self.export_csv(fname, space['table'], False)
        return space

    def export_initial_experiments_template_csv(self, fname):
        """Retrieves the validated experimental space table and writes an
        empty initial experiments table to a CSV file on disk.

        # Arguments
        fname (str):
            The filesystem path where the file will be written.

        timeout (int):
            The maximum number of seconds that the client will poll the session
            to retrieve the experimental space. The default is 300 (5 minutes).

        # Returns
        list:
            The experiments table header row that was written to disk, as a list of strings.
        """

        space = self.get_experimental_space()
        if space is None:
            raise SessionParametersNotValidatedError()

        col_headers = self.experiments_table_column_names(space)
        self.export_csv(fname, {'colHeaders': col_headers, 'data':[]}, True)
        return col_headers

    def export_generated_design_csv(self, fname, gen=None):
        """Retrieves a design generation from the session, and writes the
        table (with empty responses) to a CSV file on disk.

        # Arguments
        fname (str):
            The filesystem path where the file will be written.

        gen (int):
            The generation number for the design to be retrieved.
            If None, retreive the design for the current generation.

        # Returns
        dict:
            The generated design, a Python dict representing an experiments table
            with empty responses with `colHeaders`, and `data` keys.
        """

        design = self.get_generated_design(gen=gen)
        self.export_csv(fname, design['table'], True)
        return design

    def export_experiments_history_csv(self, fname):
        """Retrieves and returns the experiments and responses for all generations in the session,
        and writes them to a summary CSV file on disk. Also updates the `experiments_history`
        attribute in the client.

        # Arguments
        fname (str):
            The filesystem path where the file will be written.

        timeout (int):
            The maximum number of seconds that the client will poll the session
            to retrieve the generated design. The default is 1800 (30 minutes).

        # Returns
        list or None:
            The value of the client's `experiments_history` attribute, which may be
            None if no experiments have been submitted or designed, or is a list of dicts.
            Each item in the list is a Pythoon dict that represents a generation
            (the first item is generation "zero", the initial experiments, etc.) with the
            following keys:


        """

        if self.experiments_history is None:
            self.get_experiments_history()
        history = self.experiments_history
        if history is not None and len(history) > 0:
            with open(fname, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
                seq = 0
                header_written = False
                for gen, exp in enumerate(history):
                    if exp is not None and 'table' in exp and exp['table'] is not None:
                        if not header_written:
                            writer.writerow(['Seq_', 'Gen_', 'Designed_'] + exp['table']['colHeaders'])
                            header_written = True
                        drows = exp['designRows']
                        for i, row in enumerate(exp['table']['data']):
                            seq += 1
                            designed = 'Y' if i < drows else 'N'
                            writer.writerow([seq, gen, designed] + row)

        return history

    def space_table_value_column_name(self, space_type, i):
        """Utility method to format a header column name for in an
        experimental space table.

        # Arguments
        space_type (str):
            "mixture" or "factorial"

        i (int):
            Index of the value column (starting at zero).

        # Returns
        str:
            "Min" or "Max" for a "mixture" space type, or "Value.1", "Value.2", etc.
            for a "factorial" space type.
        """

        if space_type == 'mixture':
            if i == 0:
                return 'Min'
            elif i == 1:
                return 'Max'
        return 'Value.{0}'.format(i + 1)

    def space_table_column_names(self, space):
        """Generates the canonically formatted column header names for
        the experimental space table.

        # Arguments
        space (dict):
            A Python dict that defines the experimental space.

        # Returns
        list:
            A list of strings to build the column header for an experimental space.
            The list will contain "Name", "Type", "Min" and "Max" for a "mixture" space,
            or "Name", "Type", "Value.1", "Value.2", etc. for a "factorial" space.
        """

        params = space['table']['data']
        if len(params) > 0:
            space_type = space['type']
            n_value_cols = len(params[0]) - 2
            value_cols = [ self.space_table_value_column_name(space_type, i) for i in range(0, n_value_cols) ]
            return [ 'Name', 'Type' ] + value_cols
        return []

    def experiments_table_column_names(self, space):
        """Generates the required header for the experiments table, including the
        names of each parameter in the experimental space, and the reserved name
        "Response" for the experiment response value.

        # Arguments
        space (dict):
            A Python dict that defines the experimental space.

        # Returns
        list:
            The list is made up from the names of all parameters, and the additional
            string "Response".
        """

        params = space['table']['data']
        if len(params) > 0:
            param_names = [param[0] for param in params]
            return param_names + ['Response']
        return []

    def experiment_with_random_response(self, experiment, max_response_value):
        """Uses a random number generator to generate a numerical response value
        in the range [0, n] and then replaces any existing response value with
        the generated value.

        # Arguments
        experiment (list):
            A list of values representing an experiment, including a (possibly
            empty) response value.

        max_response_value (float):
            The maximum random response value to be generated for the experiment.

        # Returns
        list:
            The list of parameter values for the specified experiment, with a generated
            response value. Each value is encoded as a string.
        """

        response = '{:.3f}'.format(random.uniform(0.0, max_response_value))
        new_experiment = experiment[0:-1]
        new_experiment.append(response)
        return new_experiment

    def random_parameter_value(self, space_type, param):
        """Uses a random number generator to select a parameter value that is valid
        for the space type and specified parameter definition.

        # Arguments
        space_type (str):
            The space type, either "mixture" or "factorial".

        param (list):
            The row from the experimental space definition table that defines
            a particular parameter in the space (name, type, and min / max or
            allowed values for the parameter). Each element in the list is
            encoded as a string.

        # Returns
        str:
            A valid value for the parameter, encoded as a string.
        """

        if len(param) < 4:
            raise InvalidSpaceParameterError(space_type, param)
        if space_type == 'mixture':
            if param[1] != 'unit':
                raise InvalidSpaceParameterError(space_type, param)
            min_value = int(param[2])
            max_value = int(param[3])
            return str(random.randint(min_value, max_value))
        else:
            if param[1] not in ['factorial', 'numerical']:
                raise InvalidSpaceParameterError(space_type, param)
            values = [s for s in param[2:] if s != '']
            return random.choice(values)

    def random_experiment_for_space(self, space, max_response_value=None):
        """Uses a random number generator to select parameter values and
        optionally to create a random response value.

        # Arguments
        space (dict):
            A Python dict that defines the experimental space.

        max_response_value : None or float
            If None, the experiment is generated with an empty response.
            If a number, the response value is a randomly generated number
            in the range [0.0, max_response_value].

        # Returns
        str:
            A valid value for the parameter, encoded as a string.
        """

        space_type = space['type']
        params = space['table']['data']
        experiment = [self.random_parameter_value(space_type, param) for param in params] + ['']
        if max_response_value is not None:
            return self.experiment_with_random_response(experiment, max_response_value)
        return experiment

    def experiments_table_template(self, space):
        """Generate the column header for the experiments table, with no data
        rows. Can be used to export an empty experiments table template CSV file,
        or to submit "empty" initial experiments.

        # Arguments
        space (dict):
            A Python dict that defines the experimental space.

        # Returns
        dict:
            A Python dict with `colHeaders` and `data` values, representing an
            empty experiments table.
        """

        col_headers = self.experiments_table_column_names(space)
        if col_headers is None:
            raise SpaceOrDesignRequiredError()
        return {'colHeaders': col_headers, 'data': [] }

    def random_experiments_with_responses(self, space, design, num_extras=0, max_response_value=5.0):
        """Generate an experiments table with where each experiment row
        contains a randomly generated response value. The experiment rows
        are optionally  composed of "designed" rows and "extra" rows.
        The "designed" rows have one experiment row for each row in the
        currently generated design. And the "extra" rows contain randomly
        generated parameter values as well as responses.

        # Arguments
        space (dict):
            A Python dict that defines the experimental space.

        design (dict): or None
            If supplied, a Python dict that defines the currently generated
            design as a table. The dict has `colHeaders` and `data` keys.

        num_extras: int
            If non-zero, generate this number of extra rows. The extra rows
            will be appended to any designed rows.

        max_response_value : float
            The maximum value for generated responses. Each genreated response value
            is a randomly generated number in the range [0.0, max_response_value].

        # Returns
        dict:
            A Python dict with `colHeaders` and `data` values, representing an
            experiments table.
        """

        col_headers = None
        designed_experiments = []
        extra_experiments = []
        if space is not None:
            col_headers = self.experiments_table_column_names(space)
            if num_extras > 0:
                extra_experiments = [self.random_experiment_for_space(space, max_response_value) for i in range(0, num_extras)]
        if design is not None:
            col_headers = design['table']['colHeaders']
            designed_experiments = [self.experiment_with_random_response(experiment, max_response_value) for experiment in design['table']['data']]
        if col_headers is None:
            raise SpaceOrDesignRequiredError()
        return { 'colHeaders': col_headers, 'data': designed_experiments + extra_experiments }
