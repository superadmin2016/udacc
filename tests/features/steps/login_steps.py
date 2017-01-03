from behave import *

@given(u'flask is setup')
def flask_setup(context):     
    assert context.client
    

#@given(u'i login with "{username}" and "{password}" ')
@when(u'I login with "{username}" and "{password}"')
def login(context, username, password):
    context.page = context.client.post('/auth/login', data=dict(
         email = username,
         password = password
        ), follow_redirects = True)
    assert context.page
    

@then(u'i should see the alert "{message}"')
def logged_in(context, message):
    #print(str(context.page.data, 'utf-8'))
    assert str.encode(message) in context.page.data