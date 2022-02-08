#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, make_response, request
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from config import DevelopentConfig, HostConfig

load_dotenv()

DBC = DevelopentConfig
HSC = HostConfig

app=Flask(__name__)
app.config.from_object(DBC)

app.secret_key = os.environ['KEY']
csrf = CSRFProtect()

@app.route('/')
def index():
    response = make_response( render_template("index.html") )
    response.set_cookie('log_user', 'True')
    log_user = request.cookies.get('log_user')
    print(log_user)
    return response

@app.route('/commands')
def commands():
    return render_template("commands.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/faq')
def faq():
    return render_template("team.html")

@app.route('/license')
def license():
    return render_template("license.html")

@app.route('/login')
def login():
    pass

def page_not_found(error):
    return render_template('404.html'), 404

if __name__=='__main__':
    app.register_error_handler(404, page_not_found)
    csrf.init_app(app)
    app.run(host="0.0.0.0", port=8101)