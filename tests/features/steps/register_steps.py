from flask_login import login_user, logout_user, login_required, current_user
from app.models import User

@given('I am logged in as "{username}"')
def login_as_user(context, username):
    with context.server.app_context(), context.server.test_request_context():        
        user = User.query.filter_by(email = username).first()
        login_user(user)
        assert current_user.email == username

@then(u'I should see the url to "{url_text}" from url "{request_url}"')
def user_should_see_url_text(context, url_text, request_url):
    page = context.client.get(request_url)
    assert str.encode(url_text) in page.data

@when(u'I click on registration link')
def click_on_registration_link(context):
    context.page = context.client.get('/auth/register', follow_redirects=True)

@then(u'I should see the registration page')
def should_see_registration_page(context):
    #Change this in future to lookup some unique string on the page
    assert context.page.status_code == 200