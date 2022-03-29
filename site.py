from flask import Flask as F
from flask import *
import sqlite3

app = F(__name__)
@app.route('/', methods=['POST', 'GET'])
def page():
    return render_template('index.html', number=2)


@app.route('/assor', methods=['POST', 'GET'])
def assor():
    con = sqlite3.connect('imag.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT name, img FROM img WHERE id > 0""").fetchall()
    sp = []
    for y in result:
        sp.append([y[0], y[1]])
    return render_template('index1.html', sp=sp)

@app.route('/vhod', methods=['POST', 'GET'])
def vhod():
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
                            <title>Вход</title>
                          </head>
                          <style>
                          #center {text-align: center;
                            font-size: 50px;
                            color: #FF99FF;
                            font: Oranienbaum;}
                              </style>
                              </head>
                                <style>
                            body {
                              background-image: url("static/images/backgr.png")
                            }
                           </style>
                           <style>
                          #cen {font-size: 50px;
                            color: #FF99FF;
                            font: Oranienbaum;}
                              </style>
                              </head>
                                <style>
                            body {
                              background-image: url("static/images/backgr.png")
                            }
                           </style>
                          <body>
                            <div id=center><h1>Форма для возвращения к доктору стоуну</h1></div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
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
                            <title>Регистрация</title>
                          </head>
                          <style>
                          #center {text-align: center;
                            font-size: 50px;
                            color: #FF99FF;
                            font: Oranienbaum;}
                              </style>
                              </head>
                                <style>
                            body {
                              background-image: url("static/images/backgr.png")
                            }
                           </style>
                           <style>
                          #cen {font-size: 50px;
                            color: #FF99FF;
                            font: Oranienbaum;}
                              </style>
                              </head>
                                <style>
                            body {
                              background-image: url("static/images/backgr.png")
                            }
                           </style>
                          <body>
                            <div id=center><h1>Форма для становления доктором стоуном</h1></div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <div id=center><h2>Укажите ваш возраст</h2></div>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>13</option>
                                          <option>14</option>
                                          <option>15</option>
                                          <option>16</option>
                                          <option>17</option>
                                          <option>18</option>
                                          <option>19</option>
                                          <option>20</option>
                                          <option>21</option>
                                          <option>22</option>
                                          <option>23</option>
                                          <option>24</option>
                                          <option>25</option>
                                          <option>26</option>
                                          <option>27</option>
                                          <option>28</option>
                                          <option>29</option>
                                          <option>30</option>
                                          <option>31</option>
                                          <option>32</option>
                                          <option>33</option>
                                          <option>34</option>
                                          <option>35</option>
                                          <option>36</option>
                                          <option>37</option>
                                          <option>38</option>
                                          <option>39</option>
                                          <option>40</option>
                                          <option>41</option>
                                          <option>42</option>
                                          <option>43</option>
                                          <option>44</option>
                                          <option>45</option>
                                          <option>46</option>
                                          <option>47</option>
                                          <option>48</option>
                                          <option>49</option>
                                          <option>50</option>
                                          <option>51</option>
                                          <option>52</option>
                                          <option>53</option>
                                          <option>54</option>
                                          <option>55</option>
                                          <option>56</option>
                                          <option>57</option>
                                          <option>58</option>
                                          <option>59</option>
                                          <option>60</option>
                                          <option>61</option>
                                          <option>62</option>
                                          <option>63</option>
                                          <option>64</option>
                                          <option>65</option>
                                          <option>66</option>
                                          <option>67</option>
                                          <option>68</option>
                                          <option>69</option>
                                          <option>70</option>
                                          <option>71</option>
                                          <option>72</option>
                                          <option>73</option>
                                          <option>74</option>
                                          <option>75</option>
                                          <option>76</option>
                                          <option>77</option>
                                          <option>78</option>
                                          <option>79</option>
                                          <option>80</option>
                                          <option>81</option>
                                          <option>82</option>
                                          <option>83</option>
                                          <option>84</option>
                                          <option>85</option>
                                          <option>86</option>
                                          <option>87</option>
                                          <option>88</option>
                                          <option>89</option>
                                          <option>90</option>
                                          <option>91</option>
                                          <option>92</option>
                                          <option>93</option>
                                          <option>94</option>
                                          <option>95</option>
                                          <option>96</option>
                                          <option>97</option>
                                          <option>98</option>
                                          <option>99</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <div id=center><h2>Немного о себе</h2></div>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <div id=cen><h2>Выбирите картинку для аватарки</h2></div>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <style>
                                          #cen {font-size: 50px;
                                            color: #FF99FF;
                                            font: Oranienbaum;}
                                              </style>
                                              </head>
                                                <style>
                                                body {
                                                  background-image: url("static/images/backgr.png")
                                                    }
                                       </style>
                                        <div id=center><h2>Укажите пол</h2></div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <div id=cen><h2>Мужской</h2></div>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <div id=cen><h2>Женский</h2></div>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <div id=cen><h2>Вы робот?</h2></div>
                                        <select class="form-control" id="classSelect" name="rob">
                                          <option>Да</option>
                                          <option>Нет</option>
                                        </select>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        ch = request.form['rob']
        return oshibka(ch)

@app.route('/osibka')
def oshibka(ch):
    if ch == 'Да':
        return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Вы робот :(</title>
                      </head>
                      <style>
                              #center {text-align: center;
                                font-size: 50px;
                                color: #FF3300;
                                font: Oranienbaum;}
                                  </style>
                                  </head>
                                    <style>
                                body {
                                  background-image: url("static/images/backgr.png")
                                }
                               </style>
                      <body>
                          <div id=center><h2>К сожалению, вы робот!</h2></div>
                          <img src="/static/images/ohsi.png" alt="здесь должна была быть картинка, но это не значит что вы не робот">
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
                        <title>Вы робот :(</title>
                      </head>
                      <style>
                              #center {text-align: center;
                                font-size: 50px;
                                color: #FFCCFF;
                                font: Oranienbaum;}
                                  </style>
                                  </head>
                                    <style>
                                body {
                                  background-image: url("static/images/backgr.png")
                                }
                               </style>
                      <body>
                          <div id=center><h2>Регистрация прошла успешно!</h2></div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
