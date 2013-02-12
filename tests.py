import unittest
import breathe_easy
import flask

class BreatheEasyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = breathe_easy.app.test_client()

    def tearDown(self):
        pass

    def test_root_content(self):
        response = self.app.get('/')
        welcome_message = 'Welcome to Breathe Easy!  Take a deep breath and relax.'
        self.assertEqual(response.data, welcome_message)
        self.assertEqual(response.status_code, 200)

    def test_request_object(self):
        app = flask.Flask(__name__)
        with app.test_request_context('/workspaces'):
            self.assertEqual(flask.request.path, '/workspaces')


if __name__ == '__main__':
    unittest.main()
