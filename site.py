from flask import Flask as F
from flask import *
from flask_login import LoginManager
import sqlite3


app = F(__name__)
@app.route('/', methods=['POST', 'GET'])
def page():
    if request.method == 'GET':
        return render_template('index.html', number=2)
    elif request.method == 'POST':
        return obsidian()


@app.route('/regist', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(username, password1, password2)
        return ' '

# эта страница с ассортиментом камней
@app.route('/assor', methods=['POST', 'GET'])
def assor():
    con = sqlite3.connect('imag.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT name, img FROM img WHERE id > 0""").fetchall()
    sp = []
    for y in result:
        sp.append([y[0], y[1]])
    return render_template('index1.html', sp=sp)


@app.route('/obsidian')
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
                  <body>
                    <img src="/static/img/obsidian.png" alt="здесь должна была быть картинка, но не нашлась">                  </body>
                </html>'''

if __name__ == '__main__':
    #db_session.global_init("db/users.db")
    app.run(port=8080, host='127.0.0.1')
