import sys
import o2managementlib
from o2exceptions import *

class Mask():

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

    # def find_user(self, oxygen_id):
    #     return self.o2.get_user_by_oxygen_id(oxygen_id)

    # def subscriptions_for_user(self, oxygen_id):
    #     # oxygen_id = self.find_user(oxygen_id)
    #     return self.o2.get_subscriptions_for_user(oxygen_id)


    def create_workspace(self, arg):
        pass

    def show_workspace(self, space_name):
        try:
            space_info = self.o2.get_space_by_space_name(space_name)
        except O2SystemError as error:
            return { space_name: error.message }

        workspace_info = {}
        workspace_info['id'] = space_info.get_space_id()
        workspace_info['name'] = space_info.get_name()
        workspace_info['description'] = space_info.get_description()
        workspace_info['owner_id'] = space_info.get_owner_oxygen_id()
        workspace_info['storage_name'] = space_info.get_storage_name()
        workspace_info['utilization'] = space_info.get_utilized()
        workspace_info['listed_in_space_directory'] = space_info.is_listed()
        workspace_info['writable_by_default'] = space_info.is_writable_by_default()

        workspace_info = {
            'id': space_info.get_space_id(),
            'name': space_info.get_name(),
            'description': space_info.get_description(),
            'owner_id': space_info.get_owner_oxygen_id(),
            'storage_name': space_info.get_storage_name(),
            'utilization': space_info.get_utilized(),
            'listed_in_space_directory': space_info.is_listed(),
            'writable_by_default': space_info.is_writable_by_default()
        }

        mapping = [
            ('id', 'get_space_id'),
            ('name', 'get_name'),
            ('description', 'get_description'),
            ('owner_id', 'get_owner_oxygen_id'),
            ('storage_name', 'get_storage_name'),
            ('utilization', 'get_utilized'),
            ('listed_in_space_directory', 'is_listed'),
            ('writable_by_default', 'is_writable_by_default')
        ]

        workspace_info = {}
        for key, value in mapping:
            workspace_info[key] = getattr(space_info, value)()

        return dict(workspace=workspace_info)

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

