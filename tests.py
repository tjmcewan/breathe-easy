import pdb
from flask.ext.testing import LiveServerTestCase
import urllib2
import server


class RespiratorTests(LiveServerTestCase):
    def create_app(self):
        app = respirator.app
        app.config['TESTING'] = True
        return app

    # def test_manage_everything(self):
    #     # list spaces, delete all
    #     try:
    #         response = urllib2.urlopen(self.get_server_url() + '/spaces')
    #         pdb.set_trace()
    #     except Exception as e:
    #         print e
    #     # list users, delete all
    #     # create a space
    #     # create a user
    #     # subscribe user to space


    def test_space_not_found(self):
        try:
            response = urllib2.urlopen(self.get_server_url() + '/spaces/monkey')
        except urllib2.URLError, e:
            if not hasattr(e, "code"):
                raise
            response = e
            self.assertEqual(response.code, 404)

