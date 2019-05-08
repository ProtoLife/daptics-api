# Schema Types

<details>
  <summary><strong>Table of Contents</strong></summary>

  * [Query](#query)
  * [Mutation](#mutation)
  * [Objects](#objects)
    * [Analytics](#analytics)
    * [AnalyticsFileInfo](#analyticsfileinfo)
    * [ApiParameters](#apiparameters)
    * [AuthenticationToken](#authenticationtoken)
    * [BatchTransactionResult](#batchtransactionresult)
    * [BraintreeToken](#braintreetoken)
    * [CampaignInfo](#campaigninfo)
    * [CategorizedError](#categorizederror)
    * [DataFrame](#dataframe)
    * [ExperimentalSpace](#experimentalspace)
    * [ExperimentalSpaceTemplate](#experimentalspacetemplate)
    * [Experiments](#experiments)
    * [GenerateTaskResult](#generatetaskresult)
    * [InfoUpdated](#infoupdated)
    * [Loadavg](#loadavg)
    * [Notification](#notification)
    * [PasswordChanged](#passwordchanged)
    * [Server](#server)
    * [Session](#session)
    * [SessionAuth](#sessionauth)
    * [SessionParameters](#sessionparameters)
    * [SessionSummary](#sessionsummary)
    * [SpaceTaskResult](#spacetaskresult)
    * [Task](#task)
    * [TaskProgress](#taskprogress)
    * [TaskSummary](#tasksummary)
    * [TokenSent](#tokensent)
    * [Transaction](#transaction)
    * [User](#user)
    * [UserCreated](#usercreated)
    * [UserProfile](#userprofile)
    * [UserSummary](#usersummary)
  * [Inputs](#inputs)
    * [ChangePasswordInput](#changepasswordinput)
    * [DataFrameInput](#dataframeinput)
    * [ExperimentsInput](#experimentsinput)
    * [GenInfoInput](#geninfoinput)
    * [NewNotificationInput](#newnotificationinput)
    * [NewSessionInput](#newsessioninput)
    * [NewTransactionInput](#newtransactioninput)
    * [NewUserInput](#newuserinput)
    * [RuntimeInfoInput](#runtimeinfoinput)
    * [SessionParametersInput](#sessionparametersinput)
    * [SpaceInfoInput](#spaceinfoinput)
    * [SpaceInput](#spaceinput)
    * [TaskInput](#taskinput)
    * [UserProfileInput](#userprofileinput)
  * [Scalars](#scalars)
    * [Boolean](#boolean)
    * [DateTime](#datetime)
    * [Float](#float)
    * [Int](#int)
    * [String](#string)

</details>

## Query (RootQueryType)
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>currentTask</strong></td>
<td valign="top"><a href="#task">Task</a></td>
<td>

Get the progress (if not completed) or the result (if completed) of the last un-archived task in the session. For non-admin users, returns information only if the session is owned by the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">taskId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

If provided, only returns information if the task's id matches.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">type</td>
<td valign="top"><a href="#string">String</a></td>
<td>

If provided, only returns information if the task's type ('space', 'generate', or 'finalize') matches.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>experiments</strong></td>
<td valign="top"><a href="#experiments">Experiments</a></td>
<td>

Get the experiments and any supplied responses for current or a previous generation. For non-admin users, returns information only if the session is owned by the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">gen</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The generation number. Use zero to get any initial experiments.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>server</strong></td>
<td valign="top"><a href="#server">Server</a></td>
<td>

Get the server by id. Admin-level users only.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">serverId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's id (unique name, like 'localhost').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>servers</strong></td>
<td valign="top">[<a href="#server">Server</a>]</td>
<td>

Search all servers. Admin-level users only.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">q</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A string to filter search on. If provided, will limit the response to matches on a server's name or url.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">status</td>
<td valign="top"><a href="#string">String</a></td>
<td>

Status to filter search on ('up' or 'down'). If provided, will limit the response to matches on a server's current runtime status.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>session</strong></td>
<td valign="top"><a href="#session">Session</a></td>
<td>

Get PDT session information. For admin-level user, get the session by id. For non-admin user, get the session only if it is owned by the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionParameters</strong></td>
<td valign="top"><a href="#sessionparameters">SessionParameters</a></td>
<td>

Get the experimental space and project parameters for a given session. For non-admin users, returns information only if the session is owned by the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessions</strong></td>
<td valign="top">[<a href="#sessionsummary">SessionSummary</a>]</td>
<td>

Search sessions. For Admin-level users, returns search over all sessions.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">q</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A string to filter search on. If provided, will limit the response to matches on session's id, tag, name or description.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

If provided, list only the sessions for this user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tasks</strong></td>
<td valign="top">[<a href="#task">Task</a>]</td>
<td>

Get list of all, or just un-archived tasks in the session. For non-admin users, returns information only if the session is owned by the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">includeArchivedTasks</td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

If false, limits the response to tasks that have not completed.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#user">User</a></td>
<td>

For admin-level user, get a user by id. For non-admin user, return the currently logged-in user if the user_id matches.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id (a generated base-36 hash).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>users</strong></td>
<td valign="top">[<a href="#usersummary">UserSummary</a>]</td>
<td>

For admin-level user, search all users. For non-admin user, returns a list containing just the currently logged-in user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">q</td>
<td valign="top"><a href="#string">String</a></td>
<td>

A string to filter search on. If provided, will limit the response to matches on a user's first name, last name or email address.

</td>
</tr>
</tbody>
</table>

## Mutation (RootMutationType)
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>changePassword</strong></td>
<td valign="top"><a href="#passwordchanged">PasswordChanged</a></td>
<td>

Change a user's password, authenticating via header or password change token.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">input</td>
<td valign="top"><a href="#changepasswordinput">ChangePasswordInput</a>!</td>
<td>

The data used to authenticate and set the new password.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's id, required if not authenticating via token.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createAnalytics</strong></td>
<td valign="top"><a href="#analytics">Analytics</a></td>
<td>

Generate a list of analytics files for the current or a previous generation.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">gen</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The generation number.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createBraintreeToken</strong></td>
<td valign="top"><a href="#braintreetoken">BraintreeToken</a></td>
<td>

Generate a Braintree client token for a user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">email</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createNotification</strong></td>
<td valign="top"><a href="#notification">Notification</a></td>
<td>

Create a new system notification.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">notification</td>
<td valign="top"><a href="#newnotificationinput">NewNotificationInput</a>!</td>
<td>

Information about the requested notification.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createSession</strong></td>
<td valign="top"><a href="#session">Session</a></td>
<td>

Create and start a new PDT session on a server, installing and initializing required application and user data files on the server.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">session</td>
<td valign="top"><a href="#newsessioninput">NewSessionInput</a>!</td>
<td>

The target server, the session's name and description, and whether this is a demo or regular session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createTransaction</strong></td>
<td valign="top"><a href="#transaction">Transaction</a></td>
<td>

Create a new pending or posted financial transaction. Debit transactions will be checked against the user's current balance. System-level users only.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">transaction</td>
<td valign="top"><a href="#newtransactioninput">NewTransactionInput</a>!</td>
<td>

Information about the requested transaction. The txn_status value must be 'authorized' or 'posted'.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createUser</strong></td>
<td valign="top"><a href="#usercreated">UserCreated</a></td>
<td>

Create an unverified user account. The account's email address must be verified before it is activated.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">createToken</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

If true, an email message with a verification link will be mailed to the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">promotionCode</td>
<td valign="top"><a href="#string">String</a></td>
<td>

If present, the promotion code that will be applied to the new user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">user</td>
<td valign="top"><a href="#newuserinput">NewUserInput</a>!</td>
<td>

The first name, last name, email address and password for the new user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>login</strong></td>
<td valign="top"><a href="#authenticationtoken">AuthenticationToken</a></td>
<td>

Log in a user by email and password. Use the returned token to authenticate other requests. Use the returned user_id to create new sessions.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">email</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">password</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's password (in cleartext).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>logout</strong></td>
<td valign="top"><a href="#authenticationtoken">AuthenticationToken</a></td>
<td>

Log out a user, by revoking the access token. Returns information about the revoked token.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">token</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The access token to revoke.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>restartSession</strong></td>
<td valign="top"><a href="#session">Session</a></td>
<td>

Restart a previously created PDT session, re-initializing application and user data files.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sesssion's id as returned by the createSession mutation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>saveExperiments</strong></td>
<td valign="top"><a href="#task">Task</a></td>
<td>

Validate and start a 'generate' task to save initial, extra and/or generated experiment responses.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">experiments</td>
<td valign="top"><a href="#experimentsinput">ExperimentsInput</a>!</td>
<td>

The experiments and responses to validate.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>saveSessionParameters</strong></td>
<td valign="top"><a href="#task">Task</a></td>
<td>

Validate and start a 'space' task to save a session's experimental space parameters (space type, population size, replicates, total volume and experimental parameter definitions).

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">params</td>
<td valign="top"><a href="#sessionparametersinput">SessionParametersInput</a>!</td>
<td>

The experimental space parameters to use for the session.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sendToken</strong></td>
<td valign="top"><a href="#tokensent">TokenSent</a></td>
<td>

Create and send a new verification or password reset token to a user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">email</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tokenType</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of token requested (`verify` or `reset`).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>simulateResponses</strong></td>
<td valign="top"><a href="#experiments">Experiments</a></td>
<td>

Generate simulated experiment responses for the current generation.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">experiments</td>
<td valign="top"><a href="#dataframeinput">DataFrameInput</a></td>
<td>

(Optional) The experiments for which responses will be generated, including initial or extra experiments.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateSessionInfo</strong></td>
<td valign="top"><a href="#infoupdated">InfoUpdated</a></td>
<td>

API callback to update session database with session information.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">genInfo</td>
<td valign="top"><a href="#geninfoinput">GenInfoInput</a></td>
<td>

Information on the number of the current and remaining generations.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">runtimeInfo</td>
<td valign="top"><a href="#runtimeinfoinput">RuntimeInfoInput</a></td>
<td>

Information on the session's runtime version.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">spaceInfo</td>
<td valign="top"><a href="#spaceinfoinput">SpaceInfoInput</a></td>
<td>

Information about the validated experimental space parameters defined for the session.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tag</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's unique tag.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateTask</strong></td>
<td valign="top"><a href="#task">Task</a></td>
<td>

Update, cancel or archive a task. For advanced users only!

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">sessionId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">task</td>
<td valign="top"><a href="#taskinput">TaskInput</a>!</td>
<td>

The task id and disposition.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateTaskTransactionStatus</strong></td>
<td valign="top"><a href="#batchtransactionresult">BatchTransactionResult</a></td>
<td>

Charge or cancel all pending transactions for a (design generation) task. System-level users only.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">taskId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">txnStatus</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The requested final status ('posted' or 'canceled').

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateTransactionStatus</strong></td>
<td valign="top"><a href="#batchtransactionresult">BatchTransactionResult</a></td>
<td>

Charge or cancel a pending transaction. If charging, debit transactions will be checked against the user's current balance. System-level users only.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">txnId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The transaction id returned by the createTransaction mutation.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">txnStatus</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The requested final status ('posted' or 'canceled').

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updateUserProfile</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

Update the user's profile.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">profile</td>
<td valign="top"><a href="#userprofileinput">UserProfileInput</a>!</td>
<td>

The first name, last name, email address and other information about the user.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">userId</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>verifyUser</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

Verify and activate an inactive user account. If successful (token matches
and has not expired and user account is inactive), return the user account profile.
Normally, verification tokens are sent to a non-API endpoint, but this
mutation can also be used.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">token</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The verification token that was emailed to the user.

</td>
</tr>
</tbody>
</table>

## Objects

### Analytics

Information about the analytics files available for the specified generation in a session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>files</strong></td>
<td valign="top">[<a href="#analyticsfileinfo">AnalyticsFileInfo</a>]</td>
<td>

The list of available file titles and locations.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>gen</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The last completed generation number.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
</tbody>
</table>

### AnalyticsFileInfo

Information about a single analytics file (PDF).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>filename</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The file's name, like 'RespSortBarplotSequence.pdf'.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The file's title, like 'Response Barplot Time Series'.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>url</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The file's url, like 'http://localhost:4041/session/sess_id/analytics/gen/1/RespSortBarplotSequence.pdf'.

</td>
</tr>
</tbody>
</table>

### ApiParameters

Parameters that a session must use to access other resources.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiBaseUri</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The URL for the session user to use to access the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiKey</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The 'API key' for the session user to use to authenticate to the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>loginUri</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The URL for the session user to use to log in.

</td>
</tr>
</tbody>
</table>

### AuthenticationToken

A user access (a JWT encoded and signed) token, used to authenticate to the API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>claims</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

All the claims stored in the token.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the token was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>expiresAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the token will expire.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The status of the the token ('active' or 'revoked').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>token</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The token. Use this as the 'Bearer' value for the HTTP authorization header.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of token ('access').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

The user account associated with this token.

</td>
</tr>
</tbody>
</table>

### BatchTransactionResult

Information about a batch of concurrently run transactions for a single user account.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>remainingBalanceInCents</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The user account's remaining available balance, in cents, after these transactions.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remainingBalanceInPdt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The user account's remaining available balance, in PDT credits, after these transactions.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>transactions</strong></td>
<td valign="top">[<a href="#transaction">Transaction</a>]</td>
<td>

The individual transactions in this batch.

</td>
</tr>
</tbody>
</table>

### BraintreeToken

A Braintree client authorization token

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>token</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The client authoriztion token.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

The user account associated with this token.

</td>
</tr>
</tbody>
</table>

### CampaignInfo

Information on current and remaining generations.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>completed</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the campaign has completed (no additional experiments can be generated).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>gen</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The generation number for the last-designed generation. -1 means experimental space parameters have not been validated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remaining</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of remaining generations in the session, if available.

</td>
</tr>
</tbody>
</table>

### CategorizedError

An error encountered while processing a query or mutation.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The type of error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>fatalError</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

True if the error is fatal.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A description of the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>systemError</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

True if the error is an internal system error.

</td>
</tr>
</tbody>
</table>

### DataFrame

A representation of a data table (similar to a CSV file). Numerical data is converted to strings, and NULL data is converted to empty strings.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>colHeaders</strong></td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The header row for the table.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[[<a href="#string">String</a>]!]!</td>
<td>

A list of rows containing data. Each row in turn is a list of strings.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>index</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

If returned, the row names for table.

</td>
</tr>
</tbody>
</table>

### ExperimentalSpace

The definition for a session's experimental space.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>spaceSize</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of possible or explorable parameter combinations.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>table</strong></td>
<td valign="top"><a href="#dataframe">DataFrame</a>!</td>
<td>

The table of experimental parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalUnits</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

For mixture spaces, the total number of volume units.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The space's type ('factorial' or 'mixture').

</td>
</tr>
</tbody>
</table>

### ExperimentalSpaceTemplate

A system-defined template for an experimental space.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of template, ('factorial-default', 'mixture-default', 'factorial-demo-default', or 'mixture-demo-default').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>template</strong></td>
<td valign="top"><a href="#experimentalspace">ExperimentalSpace</a>!</td>
<td>

The experimental space parameters for this template.

</td>
</tr>
</tbody>
</table>

### Experiments

Information about initial or subsequent experiments in a session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>designRows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of experiments generated by the system.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hasResponses</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the experiment data in the associated table contains responses.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>table</strong></td>
<td valign="top"><a href="#dataframe">DataFrame</a>!</td>
<td>

The experiment inputs (and possible responses) for the experiments.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>validated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the experiment data for this generation has been validated.

</td>
</tr>
</tbody>
</table>

### GenerateTaskResult

Result of a validate experiments task.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>campaign</strong></td>
<td valign="top"><a href="#campaigninfo">CampaignInfo</a>!</td>
<td>

Generation information.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#categorizederror">CategorizedError</a>]</td>
<td>

Errors encountered when validating the experiments.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>experiments</strong></td>
<td valign="top"><a href="#experiments">Experiments</a></td>
<td>

Designed experiments for current generation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>params</strong></td>
<td valign="top"><a href="#sessionparameters">SessionParameters</a>!</td>
<td>

Current validated experimental space parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's type ('space', 'generate', or 'finalize').

</td>
</tr>
</tbody>
</table>

### InfoUpdated

Session database updated status

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>sessId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

When update was committed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedFields</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td>

List of fields that were updated.

</td>
</tr>
</tbody>
</table>

### Loadavg

Process loadavg statistics for a linux server.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>load1</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

1 minute loadavg.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>load15</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

15 minute loadavg.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>load5</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

5 minute loadavg.

</td>
</tr>
</tbody>
</table>

### Notification

A system notification, either from a user or automatically generated.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The notification category (`bug`, `sales`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the notification was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>details</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Descriptive details about the notifcation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The reply-to email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>refNumber</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

A generated unique reference number for the notification.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sentAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

The date and time that the notification was sent to the target groups.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessTag</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The associated session's tag.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The notification's source (`system`, `session`, `inquiry`).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targets</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The notification's target email groups, comma-delimited (`sales`, `support`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The associated user's account id.

</td>
</tr>
</tbody>
</table>

### PasswordChanged

Confirming information for a password change.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The time that the password was updated.

</td>
</tr>
</tbody>
</table>

### Server

Information about a PDT server.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>bindir</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's filesystem path to basic executable scripts (deprecated).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cores</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of cores reported for the server.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>cost</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The last calulated cost metric for the server.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's fully qualified hostname.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>loadavg</strong></td>
<td valign="top"><a href="#loadavg">Loadavg</a></td>
<td>

The last reported loadavg statistics for the server.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>procs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The last reported number of processes running on the server.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>serverId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's id (a unique nickname or unqualified hostname).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sshHost</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's SSH hostname (deprecated).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's current runtime status ('up' or 'down').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the data for the server was last updated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>url</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The server's root URL.

</td>
</tr>
</tbody>
</table>

### Session

Complete information about a session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>active</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this is an active (non-archived) session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>api</strong></td>
<td valign="top"><a href="#apiparameters">ApiParameters</a>!</td>
<td>

API location and key information.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#sessionauth">SessionAuth</a></td>
<td>

Authorization information, if available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>campaign</strong></td>
<td valign="top"><a href="#campaigninfo">CampaignInfo</a>!</td>
<td>

Generation information.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>demo</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this was created as a demo session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's description.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>didCrash</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this session crashed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>didRestart</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this session was restarted.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>experiments</strong></td>
<td valign="top"><a href="#experiments">Experiments</a></td>
<td>

Designed experiments for current generation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The id for the server associated with the session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latestCompletedExperiments</strong></td>
<td valign="top"><a href="#experiments">Experiments</a></td>
<td>

Completed experiments from the previous generation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's name (unique for the associated user).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>params</strong></td>
<td valign="top"><a href="#sessionparameters">SessionParameters</a>!</td>
<td>

Current unvalidated or validated experimental space parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>path</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The filesytem path on the server associated with the session that contains the session's system and user data files.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>platformMode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Settings for the runtime platform (`development`, `test` or `production`).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>restartedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

The date and time that this session was last restarted.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>spaceTemplates</strong></td>
<td valign="top">[<a href="#experimentalspacetemplate">ExperimentalSpaceTemplate</a>!]!</td>
<td>

Experimental space parameter templates that can be used as examples.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>startedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

True if the campaign has completed (no additional experiments can be generated).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tag</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's (unique) tag.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tasks</strong></td>
<td valign="top">[<a href="#tasksummary">TaskSummary</a>]</td>
<td>

Non-archived tasks, active or completed, in this session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

The user profile associated with the session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The build version for the session, if available.

</td>
</tr>
</tbody>
</table>

### SessionAuth

Information about the access token for the session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>expirationTime</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

(TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

(TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The status of the the token ('active' or 'revoked').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>token</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The token.

</td>
</tr>
</tbody>
</table>

### SessionParameters

Information about the experimental space parameters for a PDT session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>designCost</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

If the experimental space has been validated, the cost in PDT credits for each design generation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>populationSize</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The experimental space's population size.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>replicates</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of replicates for the experimental space.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>space</strong></td>
<td valign="top"><a href="#experimentalspace">ExperimentalSpace</a>!</td>
<td>

The experimental space type and parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>validated</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the session parameters (including the space) were validated.

</td>
</tr>
</tbody>
</table>

### SessionSummary

Summary information about a session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>active</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this is an active (non-archived) session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>campaign</strong></td>
<td valign="top"><a href="#campaigninfo">CampaignInfo</a></td>
<td>

Generation information, if available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>demo</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this was created as a demo session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's description.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>host</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The id for the server associated with the session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's name (unique for the associated user).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>params</strong></td>
<td valign="top"><a href="#sessionparameters">SessionParameters</a></td>
<td>

Current unvalidated or validated experimental space parameters, if available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>path</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The filesytem path on the server associated with the session that contains the session's system and user data files.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tag</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's (unique) tag.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a></td>
<td>

The user profile associated with the session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The build version for the session, if available.

</td>
</tr>
</tbody>
</table>

### SpaceTaskResult

Result of a validate experimental space parameters task.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>campaign</strong></td>
<td valign="top"><a href="#campaigninfo">CampaignInfo</a>!</td>
<td>

Generation information.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#categorizederror">CategorizedError</a>]</td>
<td>

Errors encountered when validating the experimental space.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>params</strong></td>
<td valign="top"><a href="#sessionparameters">SessionParameters</a>!</td>
<td>

Current validated experimental space parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's type ('space', 'generate', or 'finalize').

</td>
</tr>
</tbody>
</table>

### Task

Information on a long-running task in a daptics session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>archived</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the task is no longer active and has been flagged as archived.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#categorizederror">CategorizedError</a>]</td>
<td>

Errors returned by a failed or canceled task.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>progress</strong></td>
<td valign="top"><a href="#taskprogress">TaskProgress</a></td>
<td>

Progress message reported by a currently executing task.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>result</strong></td>
<td valign="top"><a href="#taskresult">TaskResult</a></td>
<td>

The validated session parameters or generated experimental design result returned by a completed task.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>startedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

The date and time the task was started.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's status ('running', 'succeeded', 'failed', or 'canceled').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's type ('space', 'generate', or 'finalize').

</td>
</tr>
</tbody>
</table>

### TaskProgress

Progress information about a currently executing task.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A description of the last activity returned by the task.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

(TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>phase</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

(TBD)

</td>
</tr>
</tbody>
</table>

### TaskSummary

Summary information on a long-running task in a daptics session.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>sessionId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The session's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's status ('running', 'succeeded', 'failed', or 'canceled').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's type ('space', 'generate', or 'finalize').

</td>
</tr>
</tbody>
</table>

### TokenSent

Confirming information returned when a verification code was sent to an unverified user.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>sentAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The time when the code was delivered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sentTo</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td>

The email address(es) the code was delivered to.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tokenType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of token sent to the user.

</td>
</tr>
</tbody>
</table>

### Transaction

Information about a single pending, posted, or canceled financial transaction.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>amountInCents</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The amount of the transaction (debit as negative, credit as positive), in cents.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>amountInPdt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The amount of the transaction (debit as negative, credit as positive), in PDT credits.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>createdAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the transaction was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>gatewayTransactionId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The payment processor's transaction id, if any.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>memo</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A description of the transacation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remainingBalanceInCents</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The user account's remaining available balance, in cents, after this transaction.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remainingBalanceInPdt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The user account's remaining available balance, in PDT credits, after this transaction.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The id of the ('generate') task associated with the transaction, if any.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The transaction's id (a generated hash).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnKind</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The kind of transaction. (TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnStatus</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The disposition for the transaction ('authorized', 'posted', or 'canceled').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of transaction. (TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the transaction was last updated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>user</strong></td>
<td valign="top"><a href="#userprofile">UserProfile</a>!</td>
<td>

Profile and activity information for the associated user's account.

</td>
</tr>
</tbody>
</table>

### User

Full information for a user account.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The first line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr2</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The second line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr3</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The third line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>city</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's city.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>company</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's company.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's country code (4 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>currentBalanceInCents</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The currently available balance for the user's account, in cemts.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>currentBalanceInPdt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The currently available balance for the user's account, in PDT credits.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastLoginAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

The date and time that the user account last logged into a PDT session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>phone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's telephone number.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>regDate</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the user's account was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessions</strong></td>
<td valign="top">[<a href="#sessionsummary">SessionSummary</a>]!</td>
<td>

The sessions owned by the user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's state or province code (3 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's account status ('unverified', 'active', or 'disabled').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>suffix</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's suffix (`Jr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's title (`Mr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that data in the user's account was last updated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userLevel</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's permission level.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zip</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's postal code.

</td>
</tr>
</tbody>
</table>

### UserCreated

Confirming information returned when a user account was successfully created.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The new user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The new user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The new user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>promotionCode</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The promotion code applied to the new user account.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>regDate</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the new user's account was created.

</td>
</tr>
</tbody>
</table>

### UserProfile

Profile information for a user account.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The first line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr2</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The second line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr3</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The third line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>city</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's city.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>company</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's company.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's country code (4 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>phone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's telephone number.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>regDate</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the user's account was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's state or province code (3 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>suffix</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's suffix (`Jr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's title (`Mr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zip</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's postal code.

</td>
</tr>
</tbody>
</table>

### UserSummary

Profile and activity information for a user account.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The first line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr2</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The second line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr3</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The third line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>city</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's city.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>company</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's company.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's country code (4 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>currentBalanceInCents</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The currently available balance for the user's account, in cemts.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>currentBalanceInPdt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The currently available balance for the user's account, in PDT credits.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastLoginAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a></td>
<td>

The date and time that the user account last logged into a PDT session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>phone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's telephone number.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>regDate</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that the user's account was created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's state or province code (3 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's account status ('unverified', 'active', or 'disabled').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>suffix</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's suffix (`Jr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's title (`Mr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updatedAt</strong></td>
<td valign="top"><a href="#datetime">DateTime</a>!</td>
<td>

The date and time that data in the user's account was last updated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's id.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userLevel</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's permission level.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zip</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's postal code.

</td>
</tr>
</tbody>
</table>

## Inputs

### ChangePasswordInput

Input fields for changing the password on a user account.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's email address, required if changing via token authentication.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The cleartext password for the user account.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>passwordConfirmation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The cleartext password, again, for the user account.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>token</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The password change token, required if changing via token authentication.

</td>
</tr>
</tbody>
</table>

### DataFrameInput

Table data for experimental parameters or experimental responses (similar to a CSV file).

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>colHeaders</strong></td>
<td valign="top">[<a href="#string">String</a>!]!</td>
<td>

Column headers for the table.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[[<a href="#string">String</a>]!]!</td>
<td>

Data rows for the table. Each row is a list of strings. Numerical data must be expressed as a string, and a NULL value must be expressed as an empty string.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>index</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td>

Row names for the table (ignored).

</td>
</tr>
</tbody>
</table>

### ExperimentsInput

Input fields for submitting experimental responses to be validated to then to create the next design gneration.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>gen</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The current generation number. Use zero to submit initial experiments or just to proceed to the first design generation without any initial experiments.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>table</strong></td>
<td valign="top"><a href="#dataframeinput">DataFrameInput</a></td>
<td>

The experiments and their responses. Required if gen is greater than zero.

</td>
</tr>
</tbody>
</table>

### GenInfoInput

Input fields for updating a session's summary generation information.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>completed</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if the campaign has completed (no additional experiments can be generated).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>gen</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The generation number for the last-designed generation. -1 means experimental space parameters have not been validated.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>remaining</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of remaining generations in the session, if available.

</td>
</tr>
</tbody>
</table>

### NewNotificationInput

Input fields for a system notification.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The notification category (`bug`, `sales`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>details</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Descriptive details about the notifcation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The reply-to email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sessTag</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The associated session's tag.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The notification's source (`system`, `session`, `inquiry`).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targets</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The notification's target email groups, comma-delimited (`sales`, `support`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The associated user's account id.

</td>
</tr>
</tbody>
</table>

### NewSessionInput

Input fields for create a new PDT session.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>demo</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this is a demo session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A description for the session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>location</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

If provided, the id of the server on which the session will be created.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the session (unique for the user).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The id for the associated user account.

</td>
</tr>
</tbody>
</table>

### NewTransactionInput

Input fields for creating a new financial transaction.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>amountInCents</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The amount of the transaction (debit as negative, credit as positive), in cents.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>amountInPdt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The amount of the transaction (debit as negative, credit as positive), in PDT credits.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>memo</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

A description of the transaction.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paymentMethodNonce</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

If this transaction is a Braintree purchase, the payment method nonce.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

If this transaction is a design charge, the id of the associated 'generate' task.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnKind</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The kind of the transaction. (TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnStatus</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The desired status of the transaction ('authorized', or 'charged').

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txnType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The type of the transaction. (TBD)

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>userId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The id for the associated user account.

</td>
</tr>
</tbody>
</table>

### NewUserInput

Input fields for creating a new user account.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>password</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The cleartext password for the user account.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>passwordConfirmation</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The cleartext password, again, for the user account.

</td>
</tr>
</tbody>
</table>

### RuntimeInfoInput

Input fields for updating a session's runtime information.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>demo</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td>

True if this is a demo session.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The build version for the session, if available.

</td>
</tr>
</tbody>
</table>

### SessionParametersInput

Input fields for validating a session's experimental space parameters.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>populationSize</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The population size.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>replicates</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of replicates (zero or greater).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>space</strong></td>
<td valign="top"><a href="#spaceinput">SpaceInput</a>!</td>
<td>

The space type and definition of experimental parameters.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>willResetCampaign</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

True to discard all experiments and reset any existing validated experimental space parameters.

</td>
</tr>
</tbody>
</table>

### SpaceInfoInput

Input fields for updating a session's summary space definition information.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>designCost</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The cost in PDT credits for each design generation.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>gen</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The generation number (must be zero).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>populationSize</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The experimental space's population size.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>replicates</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of replicates for the experimental space.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>spaceType</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The space type, 'factorial' or 'mixture'.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalUnits</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

If a mixture space, the total number of volume units.

</td>
</tr>
</tbody>
</table>

### SpaceInput

Input fields for validating an experimental space.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>table</strong></td>
<td valign="top"><a href="#dataframeinput">DataFrameInput</a>!</td>
<td>

The experimental parameters, in a table.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>totalUnits</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

If a mixture space, the total number of volume units.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The space type, 'factorial' or 'mixture'.

</td>
</tr>
</tbody>
</table>

### TaskInput

Input fields for updating or archiving a task.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>archived</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td>

To archive this task, set the `archived` field to true.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>status</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

To cancel this task, set the `status` field to 'canceled'.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>taskId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The task's id.

</td>
</tr>
</tbody>
</table>

### UserProfileInput

Profile information for a user account.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The first line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr2</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The second line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>addr3</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The third line of the user's address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>city</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's city.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>company</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's company.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's country code (4 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>email</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's email address.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>firstName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's first name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>lastName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's last name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>phone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's telephone number.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>state</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's state or province code (3 characters maximum).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>suffix</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's suffix (`Jr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>title</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's title (`Mr.`, etc.).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zip</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The user's postal code.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The `Boolean` scalar type represents `true` or `false`.

### DateTime

The `DateTime` scalar type represents a date and time in the UTC
timezone. The DateTime appears in a JSON response as an ISO8601 formatted
string, including UTC timezone ("Z"). The parsed date and time string will
be converted to UTC and any UTC offset other than 0 will be rejected.

### Float

The `Float` scalar type represents signed double-precision fractional
values as specified by
[IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).

### Int

The `Int` scalar type represents non-fractional signed whole numeric values.
Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it is
represented in JSON as double-precision floating point numbers specified
by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).

### String

The `String` scalar type represents textual data, represented as UTF-8
character sequences. The String type is most often used by GraphQL to
represent free-form human-readable text.

