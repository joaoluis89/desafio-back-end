# Aplicacao flask para webservice de retorno de feeds
# Author: Joao Pacheco
# Date: 02/02/2018

from flask_api import FlaskAPI
from flask_httpauth import HTTPBasicAuth
from flask import *
from crawler import *

app = Flask(__name__)
auth = HTTPBasicAuth()
response = CrawlerResponse()
app.config['JSON_AS_ASCII'] = False

users = {
    "globo": "globo",
    "danny": "farias",
    "alexandre": "prates",
    "andreia": "almeida"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return response.getResponse()

if __name__ == '__main__':
    app.run()
