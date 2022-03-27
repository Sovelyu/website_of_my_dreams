from flask import Flask as F
from flask import *
import sqlite3

app = F(__name__)
@app.route('/', methods=['POST', 'GET'])
def page():
    if request.method == 'GET':
        return render_template('index.html', number=2)
    elif request.method == 'POST':
        return obsidian()

# эта страница с ассортиментом камней, я с ней пока работаю
@app.route('/assor', methods=['POST', 'GET'])
def assor():
    con = sqlite3.connect('imag.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT name, img FROM img WHERE id > 0""").fetchall()
    sp = []
    for y in result:
        sp.append([y[0], y[1]])
    return render_template('index1.html', sp=sp)

# форма не доделана, я её доделаю позже
@app.route('/registr', methods=['POST', 'GET'])
def form_sample():
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
                            <title>Пример формы</title>
                          </head>
                          <style>
                          #center {text-align: center;
                            font-size: 50px;
                            color: #2A084D;
                            font: Oranienbaum;}
                              </style>
                              </head>
                                <style>
                            body {
                              background-image: url("static/images/backgr.png")
                            }
                           </style>
                          <body>
                            <h1>Форма для становления доктором стоуном</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


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
                      <img src="/static/img/obsidian.jpg" alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
