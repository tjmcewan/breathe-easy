import sys
import o2managementlib
from o2exceptions import *

class Respirator():

    def __init__(self, api_key, oxygen_id, password):
        self.o2 = o2managementlib.O2AgentFactory().create_O2Agent(api_key)
        try:
            self.o2.login_api_user(oxygen_id, password)
        except O2Exception as e:
            print e.message
            if e.reason_code == 4:
                print 'An error occured. Invalid API Key.'
                sys.exit(1)
            elif e.reason_code == 26:
                print 'An error occured. Invalid credentials.'
                sys.exit(1)
            else:
                print 'Something else happened. Reason Code: ' + str(e.reason_code)
                sys.exit(1)

    def find_user(self, oxygen_id):
        return self.o2.get_user_by_oxygen_id(oxygen_id)

    def subscriptions_for_user(self, oxygen_id):
        # oxygen_id = self.find_user(oxygen_id)
        return self.o2.get_subscriptions_for_user(oxygen_id)
