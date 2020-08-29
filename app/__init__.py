from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# for avoid cyclic import
from app import routes