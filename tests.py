import urllib2
from flask.ext.testing import TestCase, LiveServerTestCase
import breathe_easy


class BreatheEasyUnitTests(TestCase):

    def create_app(self):
        app = breathe_easy.app
        app.config['TESTING'] = True
        return app

    def test_root_content(self):
        response = self.client.get('/')
        welcome_message = 'Welcome to Breathe Easy!  Take a deep breath and relax.'
        assert welcome_message in response.data, '%s not found in %s' %(welcome_message, response.data)


class BreatheEasyIntegrationTests(LiveServerTestCase):

    def create_app(self):
        app = breathe_easy.app
        app.config['TESTING'] = True
        return app

    def test_root_response_code(self):
        """make sure we get the proper response code"""
        response = urllib2.urlopen(self.get_server_url())
        assert response.code == 200
