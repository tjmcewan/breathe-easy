# TODO remove pdb
import pdb
import sys
import o2managementlib
from o2exceptions import *

class Mask():

    def __init__(self, api_key, oxygen_id, password):
        self.o2 = o2managementlib.O2AgentFactory().create_O2Agent(api_key)
        try:
            self.o2.login_api_user(oxygen_id, password)
        except O2Exception as error:
            print error.message
            sys.exit(1)

    # def find_user(self, oxygen_id):
    #     return self.o2.get_user_by_oxygen_id(oxygen_id)

    # def subscriptions_for_user(self, oxygen_id):
    #     # oxygen_id = self.find_user(oxygen_id)
    #     return self.o2.get_subscriptions_for_user(oxygen_id)


    def create_workspace(self, arg):
        pdb.set_trace()
        self.o2.create_space

    def show_workspace(self, space_name):
        try:
            workspace = self.o2.get_space_by_space_name(space_name)
        except O2SystemError as error:
            return { space_name: error.message }, 404

        attributes = {
            'id': workspace.get_space_id(),
            'name': workspace.get_name(),
            'description': workspace.get_description(),
            'owner_id': workspace.get_owner_oxygen_id(),
            'storage_name': workspace.get_storage_name(),
            'utilization': workspace.get_utilized(),
            'listed_in_space_directory': workspace.is_listed(),
            'writable_by_default': workspace.is_writable_by_default()
        }
        return dict(workspace=attributes)

    def update_workspace(self, arg):
        pass

    def subscriptions(self, arg):
        pass

    def create_subscription(self, arg):
        pass

    def subscription(self, arg):
        pass

    def destroy_subscription(self, arg):
        pass

    def subscriptions_for_user(self, arg):
        pass

