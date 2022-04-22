from flask import Flask as F
from flask import *
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import sqlite3
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from waitress import serve


SECRET_KEY = os.urandom(32)

app = F(__name__)

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
is_reg = False
use = ''
author = ''

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


@app.route('/', methods=['POST', 'GET'])
def home():
    return page()


@app.route('/home', methods=['POST', 'GET'])
def page():
    if request.method == 'GET':
        return render_template('index.html', number=2)
    elif request.method == 'POST':
        return obsidian()


@app.route('/kamen/<ston>', methods=['POST', 'GET'])
def kamen(ston):
    con = sqlite3.connect('db/imag.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT img, opis, autor FROM img WHERE name == '""" + ston + """'""").fetchall()
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
    files = result[0][0]
    au = result[0][2]
    if au == '-':
        return f'''<!DOCTYPE html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <link href="https://fonts.googleapis.com/css?family=Oranienbaum&display=swap" rel="stylesheet" />
                      <link href="{url_for('assor', filename='main.css')}" type="text/css" rel="stylesheet" />
                      <title>''' + \
                      ston + \
                      '''</title>
                        <script>
                       function isEmail() {
                       print()
                       }
                      </script>
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
                      .test{text-align: right ;
                        height:500px;
                        width:500px;
                        }
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
                        background: #4B7460 url("static/images/backgr.png");
                        color: #fff;
                        }
                        </style>
                        <a href="/home" id="childinner">НА ГЛАВНУЮ</a>
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
                        files + \
                        '''" alt="здесь должна была быть картинка, но не нашлась">
                         </div>
                        <div id="child">
                        <img id="ccchildinner" src="/static/images/kod.png" alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                     </div> ''' + \
                     '\n' + \
                     spis + \
                     '\n' + \
                    '''
                    <div id=rig><input type="button" value="Печать" onclick="isEmail()"></div>
                    </body>
                  </html>'''
    else:
        return '''<!DOCTYPE html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <link href="https://fonts.googleapis.com/css?family=Oranienbaum&display=swap" rel="stylesheet" />
                      <link href="{url_for('assor', filename='main.css')}" type="text/css" rel="stylesheet" />
                      <title>''' + \
                      ston + \
                      '''</title>
                        <script>
                       function isEmail() {
                       print()
                       }
                      </script>
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
                      .test{text-align: right ;
                        height:500px;
                        width:500px;
                        }
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
                        <a href="/home" id="childinner">НА ГЛАВНУЮ</a>
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
                        files + \
                        '''" alt="здесь должна была быть картинка, но не нашлась">
                         </div>
                         <div id="chi">Автор: ''' + \
                         au + \
                         '''</div>
                        <div id="child">
                        <img id="ccchildinner" src="/static/images/kod.png" alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                     </div> ''' + \
                     '\n' + \
                     spis + \
                     '\n' + \
                    '''
                    <div id=rig><input type="button" value="Печать" onclick="isEmail()"></div>
                    </body>
                  </html>'''


@app.route('/registr', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        global author
        author = form.username.data
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        global author
        author = user.username
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('page'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form=form)


@app.route("/logout")
# @login_required
def logout():
    global is_reg
    is_reg = True
    logout_user()
    return redirect(url_for('page'))

# эта страница с ассортиментом камней
@app.route('/assor', methods=['POST', 'GET'])
def assor():
    con = sqlite3.connect('db/imag.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT name, img FROM img WHERE id > 0""").fetchall()
    sp = []
    for y in result:
        sp.append([y[0], y[1]])
    return render_template('index1.html', sp=sp)


@app.route('/joke', methods=['POST', 'GET'])
def shut():
    return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Ты попался на кликбейт!</title>
                          </head>
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
                                      .test{text-align: right ;
                                        height:500px;
                                        width:500px;
                                        }
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
                            body {
                            background: #306754 url("static/images/backgr.png");
                            color: #fff;
                            }
                            </style>
                            <h1>
                            <div id="chi">АХАХАХАХАХАХАХАХА</div>
                            </h1>
                            <h2>
                            <div id="chi">Нет никакой техподдержки!</div>
                            </h2>
                            <h3>
                            <div id="chi">Вернитесь и перепроверьте данные!</div>
                            </h3>
                            </body>
                        </html>'''


@app.route('/add_stone', methods=['POST', 'GET'])
@login_required
def add_stageobsidian():
    if request.method == 'GET':
        return '''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Добавить камень</title>
                              </head>
                              <style>
                                body {
                                background: #306754 url("/static/images/backgr.png");
                                color: #fff;
                                }
                                </style>
                                <a href="/home" id="childinner">НА ГЛАВНУЮ</a>
                                <h1>Анкета для камня</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <div class="form-group">
                                            <label for="about">Имя камня</label>
                                            <textarea class="form-control" id="about" rows="3" name="name"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Немного о камне</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" id="photo" name="file">
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записать камень</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        con = sqlite3.connect('db/imag.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT id FROM img WHERE id > 0""").fetchall()
        sp = []
        for y in result:
            x = y[0]
            sp.append(x)
        ids = int(sp[-1]) + 1
        name = request.form['name']
        opis = request.form['about']
        file = str(request.form['file'])
        #os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
        if name and opis and file:
            cortej = (ids,
                      name,
                      file,
                      opis,
                      author)
            cur.execute("""INSERT INTO img
                    VALUES(?, ?, ?, ?, ?);""", cortej)
            con.commit()
            return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Камень успешно добавлен!</title>
                      </head>
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
                                  .test{text-align: right ;
                                    height:500px;
                                    width:500px;
                                    }
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
                        body {
                        background: #306754 url("static/images/backgr.png");
                        color: #fff;
                        }
                        </style>
                        <a href="/home" id="childinner">НА ГЛАВНУЮ</a>
                        <img src="/static/images/molodec.jpg" alt="картинка не нашлась, но вы всё равно молодец">
                        <h1>
                        <div id="chi">Вы успешно добавлил камень!</div>
                            </h1>
                        <div id="cchildinner">
                        <a href="http://127.0.0.1:8080/assor" id="chi">Вы можете увидеть его в ассортименте</a>
                        </div>
                        <div id="cchildinner">
                        <a href="http://127.0.0.1:8080/kamen/''' + \
                        name + \
                            '''" id="chi">Или в его персональной странице</a>
                        </div>
                        </body>
                    </html>'''
        else:
            return '''<!doctype html>
                    <html lang="en">
                      <head>
                            <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                            <title>
                            Неккоректные данные!
                        </title>
                      </head>
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
                                  .test{text-align: right ;
                                    height:500px;
                                    width:500px;
                                    }
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
                        body {
                        background: #306754 url("static/images/backgr.png");
                        color: #fff;
                        }
                        </style>
                        <a href="/home" id="childinner">НА ГЛАВНУЮ</a>
                        <img src="/static/images/ohsi.png" alt="картинка не нашлась, но данные до сих пор неккоректные!">
                        <h1><div id=rig>Вы ввели неккоректные данные! Пожалуйста, вернитесь и перепроверьте: </div></h1>
                        <h2><div id=lef>1.Ввели ли вы имя камня</div></h2>
                        <h3><div id=rig>2.Ввели ли вы описание камня</div></h3>
                        <h4><div id=rig>3.Выбрали ли вы файл</div></h4>
                        <a href="http://127.0.0.1:8080/joke" id="chi">Вы не смогли добавить камень, хотя всё было правильно? напишите в техподдержку!</a>
                        </body>
                    </html>'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
