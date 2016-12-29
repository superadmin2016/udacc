import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    
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