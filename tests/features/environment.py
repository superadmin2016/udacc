import os
import sys
import tempfile
from app import create_app, db

def before_feature(context, feature):
    app = create_app('default')
    context.client = app.test_client()
    

