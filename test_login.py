import argparse
import os
import sys

# Uncomment this, or use PYTHONPATH=./python_client
# sys.path.append(os.path.join(os.path.dirname(__file__), 'python_client'))

from daptics_client import DapticsClient

parser = argparse.ArgumentParser(description='Test Python API server connection and login.')
parser.add_argument('--server', metavar='URL', default='https://api.daptics.ai',
                    help='use a different API server URL')
parser.add_argument('email',  metavar='EMAIL', help='email address')
parser.add_argument('password',  metavar='PASSWORD', help='cleartext password')

args = parser.parse_args()

# Create a client object using the specified host URL
daptics = DapticsClient(args.server)

# Can set options any of these ways:
# daptics.set_options({'verify_ssl_certificates': True})
# daptics.set_option('verify_ssl_certificates', True)
daptics.options.update({'verify_ssl_certificates': True})

# Show the (default) runtime options used by the client object
print("Client options: ", daptics.options)


# The `connect` method will attempt to connect to the API server and
# obtain the GraphQL schema.
daptics.connect()

login_data = daptics.login(args.email, args.password)
if login_data is None or login_data['login'] is None:
    print(f'Login failed for {args.email}, password {args.password}')
    sys.exit(1)

user = login_data['login']['user']
token = login_data['login']['token']

print('Login succeeded')
print(f'The user data is {user}')
print(f'The access token is {token}')
