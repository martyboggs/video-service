from flask import Blueprint

test_api = Blueprint('test_api', __name__)

@test_api.route('')
def test():
  return 'this is a test route'
