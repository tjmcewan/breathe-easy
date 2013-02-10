from behave import *

import breathe_easy

@given('we have our app bootstrapped')
def impl(context):
    assert bool(breathe_easy.app) is True

@when('we hit the index page')
def step(context):
    context.browser.get('http://127.0.0.1:8000/')

@then('we get a successful response')
def step(context):
    assert context.failed is False
