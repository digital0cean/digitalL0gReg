from flask import Flask, render_template, request
from appcreator import app

# === Рендер стрниц без метода POST ===

@app.route('/errbadlogin', methods = ['GET'])
def errbadlogin():
    return render_template('errbadlogin.html', template_folder = './templates', static_folder = './static')

@app.route('/errvoidusr', methods = ['GET'])
def errusr():
    return render_template('errvoidusr.html', template_folder = './templates', static_folder = './static')

@app.route('/errvoidlgn', methods = ['GET'])
def errlgn():
    return render_template('errvoidlgn.html', template_folder = './templates', static_folder = './static')

@app.route('/errvoidpsw', methods = ['GET'])
def errpsw():
    return render_template('errvoidpsw.html', template_folder = './templates', static_folder = './static')

# === Рендер стрниц без метода POST ===