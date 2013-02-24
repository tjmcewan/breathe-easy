# import unittest
# import respirator
# import flask

# class RespiratorTestCase(unittest.TestCase):

#     def setUp(self):
#         respirator.app.debug = True
#         self.app = respirator.app.test_client()

#     def tearDown(self):
#         pass

#     # def test_root_content(self):
#     #     response = self.app.get('/')
#     #     welcome_message = 'Welcome to Respirator!  Take a deep breath and relax.'
#     #     self.assertEqual(response.data, welcome_message)
#     #     self.assertEqual(response.status_code, 200)

#     # def test_request_object(self):
#     #     app = flask.Flask(__name__)
#     #     with app.test_request_context('/workspaces'):
#     #         self.assertEqual(flask.request.path, '/workspaces')
#     #         self.assertEqual(flask.request.headers['Content-Type'], 'application/json')

#     def test_json_output(self):
#         response = self.app.get('/workspaces/monkey')
#         # self.assertEqual(response.data, dict(success=True))
#         self.assertEqual(response.status_code, 404)

#     def test_json_output_2(self):
#         response = self.app.get('/workspaces/thing')
#         # self.assertEqual(response.data, dict(success=True))
#         self.assertEqual(response.status_code, 404)

#     def test_json_output_3(self):
#         response = self.app.get('/workspaces/else')
#         # self.assertEqual(response.data, dict(success=True))
#         self.assertEqual(response.status_code, 404)

#     def test_json_output_4(self):
#         response = self.app.get('/workspaces/what')
#         # self.assertEqual(response.data, dict(success=True))
#         self.assertEqual(response.status_code, 404)


# if __name__ == '__main__':
#     unittest.main()
