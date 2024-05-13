from flask import Flask

application = Flask(__name__, template_folder='templates')
application.config['DEBUG'] = True

app=application

from dbapipackage import db

from dbapipackage import routes



