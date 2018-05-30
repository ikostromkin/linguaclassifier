from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from werkzeug.contrib.fixers import ProxyFix
from models import *


from login.views import login_blueprint
from research.views import research_blueprint
from respondent.views import respondent_blueprint
from group.views import group_blueprint

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'wefilology'

login = LoginManager(app)
login.login_view = 'login.login'


app.register_blueprint(login_blueprint)
app.register_blueprint(research_blueprint, url_prefix='/research')
app.register_blueprint(respondent_blueprint, url_prefix='/respondent')
app.register_blueprint(group_blueprint, url_prefix='/group')


@login.user_loader
def load_user(user_id):
    try:
        return Users.get(id=user_id)
    except DoesNotExist:
        return False


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('research.all_research'))
    else:
        return render_template('index.html')


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
