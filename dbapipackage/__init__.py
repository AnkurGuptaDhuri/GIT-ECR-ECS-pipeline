from flask import Flask

application = Flask(__name__, template_folder='templates')

app = application

app.config['DEBUG'] = True

from dbapipackage import db

from dbapipackage import routes



