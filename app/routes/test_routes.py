from app.routes import app


@app.route('/test')
def test():
  return 'this is a test route'
