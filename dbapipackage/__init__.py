from flask import Flask

app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True

#app = application

from dbapipackage import db

from dbapipackage import routes



