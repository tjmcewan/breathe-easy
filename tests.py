import unittest
from flask.ext.testing import TestCase
import breathe_easy

class BreatheEasyTestCase(TestCase):

    def create_app(self):
        app = breathe_easy.app
        app.config['TESTING'] = True
        return app

    def test_root_path(self):
        response = self.client.get('/')
        welcome_message = 'Welcome to Breathe Easy!  Take a deep breath and relax.'
        assert welcome_message in response.data, '%s not found in %s' %(welcome_message, response.data)

if __name__ == '__main__':
    unittest.main()
