import unittest
from flask import current_app
#from .. app import app, db

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_app_test(self):
        self.assertTrue(1 == 1, 'Failed test test')
    
    def tearDown(self):
        pass