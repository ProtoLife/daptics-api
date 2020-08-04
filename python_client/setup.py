import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='daptics_client',
    version='0.12.0',
    author='Peter Zingg',
    author_email='peter@daptics.ai',
    description='Python client for the daptics API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ProtoLife/daptics-api',
    packages=['daptics_client', 'phoenix', 'syncasync'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Framework :: AsyncIO',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.5',
    install_requires=[
        'requests', 'gql', 'async_timeout', 'websockets'
    ]
)
