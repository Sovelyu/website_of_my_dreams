from flask import Flask as F
from flask import *

app = F(__name__)
@app.route('/', methods=['POST', 'GET'])
def page():
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
                        <title>Обсидиан</title>
                      </head>
                      <body>
                        <div>
                                <form class="login_form" method="post">
                                    <button type="submit" class="btn btn-primary" name="but">Обсидиан</button>
                                </form>
                            </div>
                    </html>'''
    elif request.method == 'POST':
        return obsidian()


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
    app.run(port=8080, host='127.0.0.1')
