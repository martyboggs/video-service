from flask import Flask
import pkgutil
import re

app = Flask(__name__)


# from main import *

def find_routes():
  # sneaky import: find all the things with _routes in the routes package
  for _, p, _ in pkgutil.walk_packages(path=["./routes"], prefix="routes."):
    if re.match('^.*_routes$', p):
      print("Importing routes from " + p)
      yield p


for pkg in find_routes():
  __import__(pkg)
