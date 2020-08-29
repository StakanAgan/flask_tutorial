from flask import Flask

app = Flask(__name__)

# for avoid cyclic import
from app import routes