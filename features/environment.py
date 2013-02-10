import logging
import threading
from wsgiref import simple_server
from selenium import webdriver

from breathe_easy import app

def before_all(context):
    selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)

    context.server = simple_server.make_server('127.0.0.1', 8000, app)
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    context.browser = webdriver.Firefox()

def after_all(context):
    context.server.shutdown()
    context.thread.join()
    context.browser.quit()

def before_feature(context, feature):
    pass
