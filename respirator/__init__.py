from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

import respirator.resources

import os
from mask import Mask

api_key = os.environ['O2_API_KEY']
oxygen_id = os.environ['O2_OXYGEN_ID']
password = os.environ['O2_PASSWORD']

app.config['ADMIN_ACCOUNT'] = os.environ.get('O2_ADMIN_ACCOUNT', 'pimms_')

# if app.config.get('TESTING') == True:
#     app.mask = Mask()
# else:
app.mask = Mask(api_key, oxygen_id, password)
