#!/usr/bin/env python

import os, sys, inspect
for subfolder in ["../../sdk", "../../sdk/gen-py"]:
  abs_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], subfolder)))
  sys.path.append(abs_path)

import o2managementlib
from o2exceptions import *


# Please request an admin api key from support.oxygencloud.company
api_key = os.environ['OC_API_KEY']

# Create an O2Agent using the O2AgentFactory
o2factory = o2managementlib.O2AgentFactory()
o2 = o2factory.create_O2Agent(api_key)

# Your credentials
oxygenId = os.environ['OC_ID']
password = os.environ['OC_PASSWORD']

# Login. You must be a user with admin privileges.
# This example also shows how to handle O2Exception errors.

# All O2Agent methods throw O2Exception, so use try/except on each call
# For all O2Exception reason codes, please see documentation
try:
  o2.login_api_user(oxygenId, password)
except O2Exception as e:
  print e.message
  if e.reason_code == 4:
    print 'An error occured. Invalid API Key.' # for all O2Exception reason codes, see documentation
    sys.exit(1)
  elif e.reason_code == 26:
    print 'An error occured. Invalid credentials.' # for all O2Exception reason codes, see documentation
    sys.exit(1)
  else:
    print 'Something else happened. Reason Code: ' + str(e.reason_code)
    sys.exit(1)

# whoami
me = o2.get_user_info()

# User's information is represented as an O2UserInfo object.
# You can retrieve user information by calling O2UserInfo methods
# as specified in the documentation.
print me
print me.get_oxygen_id()
print me.get_display_name()

# # Create a new user
# o2.create_user('NEW USER OXYGEN ID', 'NEW USER EMAIL', 'NEW USER OPTIONAL CORPORATE ID', 'NEW USER FIRST NAME', 'NEW USER LAST NAME')

# # Get all users in your company. returns [O2UserInfo]
# o2.get_all_users()

# # Disable a user by their Oxygen ID
# o2.disable_user('OXYGEN ID')

# # Enable a user by their Oxygen ID
# o2.enable_user('OXYGEN ID')

# # Delete a user by their Oxygen ID
# o2.delete_user('OXYGEN ID')
