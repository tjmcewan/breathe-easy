import os
import unittest
import breathe_easy

class BreatheEasyTestCase(unittest.TestCase):

    def setUp(self):
        breathe_easy.app.config['TESTING'] = True
        self.app = breathe_easy.app.test_client()

    def tearDown(self):
        pass

    def test_root_path(self):
        response = self.app.get('/')
        assert 'Welome to Breathe Easy!  Take a deep breath and relax.' in response.data

if __name__ == '__main__':
    unittest.main()
