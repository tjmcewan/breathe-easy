# import urllib2
# from flask.ext.testing import TestCase, LiveServerTestCase
# import breathe_easy


# class BreatheEasyUnitTests(TestCase):

#     def create_app(self):
#         app = breathe_easy.app
#         app.config['TESTING'] = True
#         return app

#     def test_root_content(self):
#         response = self.client.get('/')
#         welcome_message = 'Welcome to Breathe Easy!  Take a deep breath and relax.'
#         self.assertEqual(response.data, welcome_message)

#     def test_workspaces_resource(self):
#         response = self.client.get("/workspaces")
#         self.assertEqual(response.json, dict(success=True))

#     def test_favicon(self):
#         response = self.client.get("/favicon.ico")
#         self.assertEqual(response.headers.get('content-type'), 'image/x-icon')


# class BreatheEasyIntegrationTests(LiveServerTestCase):

#     def create_app(self):
#         app = breathe_easy.app
#         app.config['TESTING'] = True
#         return app

#     def test_root_response_code(self):
#         """make sure we get the proper response code"""
#         response = urllib2.urlopen(self.get_server_url())
#         assert response.code == 200
