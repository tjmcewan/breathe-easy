import pdb
from flask.ext.testing import LiveServerTestCase
import urllib2
import respirator


class RespiratorTests(LiveServerTestCase):
    def create_app(self):
        app = respirator.app
        app.config['TESTING'] = True
        return app

    def test_manage_everything(self):
        # list spaces, delete all
        response = urllib2.urlopen(self.get_server_url() + '/workspaces')
        pdb.settrace()
        # list users, delete all
        # create a space
        # create a user
        # subscribe user to space


    # def space_not_found(self):
    #     try:
    #         response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey')
    #     except urllib2.URLError, e:
    #         if not hasattr(e, "code"):
    #             raise
    #         response = e
    #         self.assertEqual(response.code, 404)

