from flask import Flask
app = Flask(__name__)

import breathe_easy.resources

import os
# from respirator import Respirator
import respirator

api_key = os.environ['OC_API_KEY']
oxygen_id = os.environ['OC_ID']
password = os.environ['OC_PASSWORD']
app.respirator = respirator.Respirator(api_key, oxygen_id, password)
