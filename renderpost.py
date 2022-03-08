import requests
import psycopg2
from flask import Flask, render_template, request, redirect
from appcreator import app

# === Рендер стрниц c методом POST ===

connect = psycopg2.connect(database = 'auth', user = 'postgres', password = 'qwerty', host = '127.0.0.1', port = '5432')
cursor = connect.cursor()

@app.route('/', methods = ['POST', 'GET'])
def index():
    try:
        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM auth WHERE login=%s AND password=%s", (str(login), str(password)))
            fetch = list(cursor.fetchall())
            return render_template('account.html', usr=fetch[0][1], lgn=fetch[0][2], psw=fetch[0][3])
    except Exception as e:
        print(e)
        return redirect('./errbadlogin')
    return render_template('index.html', template_folder = './templates', static_folder = './static')
    

@app.route('/reg', methods = ['POST','GET'])
def reg():
    try:
        if request.method == 'POST':
            username = request.form.get('reg_username')
            login = request.form.get('reg_login')
            password = request.form.get('reg_password')
            print(username)
            print(login)
            print(password)
            if username == '':
                return redirect('./errvoidusr')
            if login == '':
                return redirect('./errvoidlgn')
            if password == '':
                return redirect('./errvoidpsw')
            cursor.execute("INSERT INTO auth(name, login, password)VALUES(%s, %s, %s )",(str(username), str(login), str(password)))
            connect.commit()
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')
    return render_template('reg.html', template_folder = './templates', static_folder = './static')

# === Рендер стрниц c методом POST ===