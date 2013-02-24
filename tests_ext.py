# import vcr
# # import cassette
# import yaml
# TODO remove pdb
# import pdb
# import requests
import urllib2
# import unittest
from flask.ext.testing import LiveServerTestCase
import respirator


# class RespiratorUnitTests(TestCase):
#     def create_app(self):
#         app = respirator.app
#         app.debug = True
#         app.config['TESTING'] = True
#         self.admin_account = app.config['ADMIN_ACCOUNT']

#         # self.session
#         return app

#     def test_root_content(self):
#         response = self.client.get('/')
#         welcome_message = 'Welcome to Respirator!  Take a deep breath and relax.'
#         self.assertEqual(response.data, welcome_message)
#         self.assertEqual(response.status_code, 200)


#     def test_favicon(self):
#         response = self.client.get("/favicon.ico")
#         self.assertEqual(response.headers.get('content-type'), 'image/x-icon')


class BreatheEasyIntegrationTests(LiveServerTestCase):
    def create_app(self):
        app = respirator.app
        app.debug = True
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        # self.admin_account = app.config['ADMIN_ACCOUNT']

        # self.session
        return app

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_server_is_up_and_running_again(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_server_is_up_and_running_again_again(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_workspaces(self):
        print "test method 1 called"
    #     url = 'http://localhost:9292/request'
    #     # payload = {'some': 'data'}
    #     headers = {'NOX_URL': 'http://localhost:5000/'}

    #         # 'content-type': 'application/json',
    #     # r = requests.post(url, data=json.dumps(payload), headers=headers)
    #     response = requests.get(url, headers=headers)
    #     # with cassette.play("tests/vcr_cassettes/responses.yaml"):
    #         # response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey')
    #         # response = urllib2.urlopen(self.get_server_url() + '/')
    #     # assert 'Example Domains' in response.read()

    #     # with vcr.use_cassette('tests/vcr_cassettes/workspaces_get.yaml'):
    #         # response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey').read()
    #     # response = urllib2.urlopen(self.get_server_url() + '/').read()
    #     # pdb.set_trace()
    #     print response.__dict__
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.body, 'Welcome to Respirator!  Take a deep breath and relax.')


    def test_workspaces_again(self):
        # with cassette.play("tests/vcr_cassettes/responses.yaml"):
            # response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey')
            # response = urllib2.urlopen(self.get_server_url() + '/')
        # assert 'Example Domains' in response.read()

        # with vcr.use_cassette('tests/vcr_cassettes/example.yaml'):
        #     response = urllib2.urlopen('http://www.iana.org/domains/example')
            # response = urllib2.urlopen(self.get_server_url() + '/workspaces/monkey').read()
        # print response.headers
        print "test method 2 called"
        # pdb.set_trace()
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.body, 'Welcome to Respirator!  Take a deep breath and relax.')




        # pdb.set_trace()
        # workspace_attributes = { 'workspace': {
        #     'name': 'monkey',
        #     'description': 'silly monkey',
        #     'owner': self.admin_account,
        #     'capacity': 1,
        #     'listed': False,
        #     'writable_by_default': True
        # }}
        # session = requests.Session()
        # session.headers.update({'Content-type': 'application/json'})
    # workspace_attributes = {'name': 'thing'}
    # url = self.get_server_url() + '/workspaces'
    # print url
    # response = urllib2.post(url, data=workspace_attributes)

    # self.assertEqual(response.status_code, 201)
    # self.assertEqual(response.headers.get('content-type'), 'application/json')
    # self.assertEqual(response.json, workspace_attributes)


#     def create_app(self):
#         respirator.app.debug = True
#         respirator.app.config['TESTING'] = True
#         return respirator.app

#     def test_root_response_code(self):
#         """make sure we get the proper response code"""
#         response = requests.get(self.get_server_url())
#         self.assertEqual(response.code, 200)


# if __name__ == '__main__':
#     unittest.main()
