from flask.ext.testing import LiveServerTestCase
import urllib2
import vcr
import respirator


class RespiratorTests(LiveServerTestCase):
    def create_app(self):
        app = respirator.app
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        with vcr.use_cassette('cassettes/workspaces.yaml'):
            try:
                response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey')
            except urllib2.URLError, e:
                if not hasattr(e, "code"):
                    raise
                response = e
                self.assertEqual(response.code, 404)

    def test_server_is_up_and_running_again(self):
        with vcr.use_cassette('cassettes/root.yaml'):
            response = urllib2.urlopen(self.get_server_url())
            self.assertEqual(response.code, 200)

    def test_server_is_up_and_running_again_again(self):
        with vcr.use_cassette('cassettes/root_again.yaml'):
            response = urllib2.urlopen(self.get_server_url())
            self.assertEqual(response.code, 200)
