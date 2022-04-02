from flask import Flask as F
from flask import *
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import sqlite3
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = os.urandom(32)

app = F(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique = True, index = True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.route('/home', methods=['POST', 'GET'])
def page():
    if request.method == 'GET':
        return render_template('index.html', number=2)
    elif request.method == 'POST':
        return obsidian()


@app.route('/kamen/<ston>', methods=['POST', 'GET'])
def kamen(ston):
    con = sqlite3.connect('db/site.db')
    cur = con.cursor()
    result = cur.execute("""SELECT img, opis, autor FROM img WHERE name == '""" + ston + "'").fetchall()
    spis = []
    buk = ''
    for y in range(len(result[0][1])):
        buk += result[0][1][y]
        if y % 30 == 0 and y != 0:
            buk = '<div id="lef">' + buk +'</div>'
            spis.append(buk)
            buk = ''
    num = result[0][1][len(result[0][1]) // 30 * 30:]
    num = '<div id="lef">' + num + '</div>'
    spis.append(num)
    spis = '\n'.join(spis)
    return f'''<!DOCTYPE html>
              <html lang="en">
                <head>
                  <meta charset="utf-8">
                  <link href="https://fonts.googleapis.com/css?family=Oranienbaum&display=swap" rel="stylesheet" />
                  <link href="{url_for('assor', filename='main.css')}" type="text/css" rel="stylesheet" />
                  <title>''' + \
                  ston + \
                  '''</title>
                  <style>
                  #mom {display: table;
                  width: 500px;}
                  #center {text-align: center;
                    font-size: 50px;
                    color: #2A084D;
                    font: Oranienbaum;}
                  #cen {text-align: left ;
                    font-size: 50px;
                    color: #2A084D;
                    font: Oranienbaum;}
                  #rig {text-align: right ;
                    font-size: 50px;
                    color: #2A084D;
                    font: Oranienbaum;}
                  #lef {text-align: left ;
                    font-size: 50px;
                    color: #2A084D;
                    font: Oranienbaum;}
                  #child {display: table-cell;}
                  #cchildinner {
                    margin-top: 180px;
                    margin-left: 220px;
                    }
                     #ccchildinner {
                      margin-left: 100px;
                    }
                  #chi {text-align: right;
                    font-size: 50px;
                    color: #2A084D;
                    font: Oranienbaum;
                    padding-left: 300px;
                    padding-bottom: 20px;}
                  #chi {margin-left: 30px;}

                  </style>
                </head>
                    <style>
                    body {
                    background: #306754 url("static/images/backgr.png");
                    color: #fff;
                    }
                    </style>
                  <div class="mom">
                  <div id="child">
                    <div id="chi">КАМЕННЫЙ</div>
                  </div>
                  <div id="child">
                    <img id="chi" src="/static/images/logo.png" alt="здесь должна была быть картинка, но не нашлась">
                  </div>
                  <div id="child">
                    <div id="chi">МИР</div>
                  </div>
                  </div>
                  <div class="mom">
                    <div id="child">
                    <img id="cchildinner" src="/static/images/''' + \
                    result[0][0] + \
                    '''" alt="здесь должна была быть картинка, но не нашлась">
                     </div>
                    <div id="child">
                    <img id="ccchildinner" src="/static/images/kod.png" alt="здесь должна была быть картинка, но не нашлась">
                    </div>
                 </div> ''' + \
                 '\n' + \
                 spis + \
                 '\n' + \
                '''</body>
              </html>'''

#вот тут короче регистрация но пока что она всех в базу добавляет надо вот сделать чтоб она не добавляла тех кто там уже есть
#дааа вот если успею сегодня сделаю
@app.route('/registr', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('page'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('page'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form=form)


@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('page'))

# эта страница с ассортиментом камней
@app.route('/assor', methods=['POST', 'GET'])
def assor():
    con = sqlite3.connect('db/site.db')
    cur = con.cursor()
    result = cur.execute("""SELECT name, img FROM img WHERE id > 0""").fetchall()
    sp = []
    for y in result:
        sp.append([y[0], y[1]])
    return render_template('index1.html', sp=sp)


@app.route('/add_stone')
def obsidian():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <title>Обсидиан</title>
                  </head>
                  <style>
                    body {
                    background: #306754 url("static/images/backgr.png");
                    color: #fff;
                    }
                    </style>
                    <div>СКОРО ЗДЕСЬ БУДЕТ ЗАГРУЗКА КАМНЕЙ, НО ЭТО УЖЕ ЗАВТРА</div>
                    </body>
                </html>'''


if __name__ == '__main__':
    #db_session.global_init("db/users.db")
    app.run(port=8080, host='127.0.0.1')
