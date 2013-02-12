from flask import Flask
app = Flask(__name__)

import breathe_easy.resources

import os
from respirator import Respirator

api_key = os.environ['O2_API_KEY']
oxygen_id = os.environ['O2_OXYGEN_ID']
password = os.environ['O2_PASSWORD']

app.respirator = Respirator(api_key, oxygen_id, password)
