import unittest
#from app import app
from app import create_app, db
from app.models import User
from unittest.case import skip

class UserModelTestCase(unittest.TestCase):
    
    def setUp(self):
        app = create_app('default')
        self.app = app.test_client()
        self.app.testing = True
    
    def test_password_setter(self):
        u = User(password = 'cat')
        self.assertTrue(u.password_hash is not None, 'Password hash is null')
        
    def test_password_getter(self):
        u = User(password = 'cat')
        with self.assertRaises(AttributeError):
            u.password
            
    def test_password_verification(self):
        u = User(password = 'cat')
        self.assertTrue(u.verify_password('cat'), 'Password did not match')
        self.assertFalse(u.verify_password('cat2'), 'Password is not correct')
        
    def test_password_salts_are_random(self):
        u = User(password = 'cat')
        u2 = User(password = 'cat')
        self.assertFalse(u.password_hash == u2.password_hash, 'Password salts should be random.')
        
    
    def test_login_incorrect(self):
        rv2 = self.app.post('/auth/login', data=dict(
                                                    email='udac.dev@gmail.com',
                                                    password='admin2'
                                                ), follow_redirects=True)
        assert b'Invalid username or password' in rv2.data
    
    def test_login_correct(self):
        rv2 = self.app.post('/auth/login', data=dict(
                                                    email='udac.dev@gmail.com',
                                                    password='admin'
                                                ), follow_redirects=True)
        assert b'admin' in rv2.data