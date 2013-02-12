# Respirator


A web service wrapper for the Oxygen Cloud Management SDK

### Dependencies

1. An OxygenCloud api key, admin username, and password set as environment variables: `O2_API_KEY`, `O2_OXYGEN_ID`, `O2_PASSWORD`
2. Python 2.7
3. `pip install -r requirements.txt`

### Usage

`python server.py`

or with [Foreman](https://github.com/ddollar/foreman):

1. `gem install foreman`
2. `foreman start`

### Testing

`python tests.py`

or with colour:

1. `pip install nose rednose`
2. `nosetests --red-nose`
