import pdb
import os
import sys
import inspect

for subfolder in ["sdk"]:
    parent = os.path.split(inspect.getfile( inspect.currentframe() ))[0]
    abs_path = os.path.realpath(os.path.abspath(os.path.join(parent, subfolder)))
    sys.path.append(abs_path)

import o2managementlib
from o2exceptions import *

class Mask():

    def __init__(self, api_key, oxygen_id, password, testing):
        self.o2 = o2managementlib.O2AgentFactory().create_O2Agent(api_key)
        try:
            if testing == False:
                self.o2.login_api_user(oxygen_id, password)
        except O2Exception as error:
            print error.message
            sys.exit(1)

    # def find_user(self, oxygen_id):
    #     return self.o2.get_user_by_oxygen_id(oxygen_id)

    # def subscriptions_for_user(self, oxygen_id):
    #     # oxygen_id = self.find_user(oxygen_id)
    #     return self.o2.get_subscriptions_for_user(oxygen_id)


    def create_space(self, space_name):
        attributes = [
            space_name,
            'description goes here',
            'tim@mcewan.it',
            '',
            0,
            True,
            True
        ]
        space = self.o2.create_space(*attributes)
        attributes = self.get_space_attributes(space)
        return {'space': attributes}

    def create_user(self, attributes):
        try:
            ordered_attributes = [
                attributes['oxygen_id'],
                attributes['email'],
                attributes.get('corporate_user_name', ''),
                attributes['first_name'],
                attributes['last_name'],
                attributes.get('password', '')
            ]
        except KeyError as error:
            return {'missing_key': error}, 400

        try:
            user = self.o2.create_user(*ordered_attributes)
        except O2InvalidInputError as error:
            return {attributes['oxygen_id']: error.message}, 400

        attributes = self.get_user_attributes(user)
        return {'user': attributes}, 200

    def show_space(self, space_name):
        try:
            space = self.o2.get_space_by_space_name(space_name)
        except O2SystemError as error:
            return {space_name: error.message}, 404

        attributes = self.get_space_attributes(space)
        return {'space': attributes}, 200

    def delete_space(self, space_name):
        try:
            space = self.o2.get_space_by_space_name(space_name)
        except O2SystemError as error:
            return {space_name: error.message}

        space_id = space.get_space_id()
        try:
            result = self.o2.delete_space(space_id)
        except O2SystemError as error:
            return {space_name: error.message}

        return {'result': result}


    def update_space(self, arg):
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

    def get_space_attributes(self, space):
        return {
            'id': space.get_space_id(),
            'name': space.get_name(),
            'description': space.get_description(),
            'owner_id': space.get_owner_oxygen_id(),
            'storage_name': space.get_storage_name(),
            'utilization': space.get_utilized(),
            'listed_in_space_directory': space.is_listed(),
            'writable_by_default': space.is_writable_by_default()
        }

    def get_user_attributes(self, user):
        return {
            'oxygen_id': user.get_oxygen_id(),
            'first_name': user.get_first_name(),
            'last_name': user.get_last_name(),
            'display_name': user.get_display_name(),
            'email': user.get_email(),
            'external?': user.is_external(),
            'deleted?': user.is_deleted(),
            'disabled?': user.is_disabled(),
            'last_login': user.get_last_login_date_time(),
            'external_id': user.get_external_id(),
            'not_yet_activated?': user.is_not_activated()
        }
