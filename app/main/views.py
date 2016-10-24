__author__ = 'yooner'
from flask import render_template
from . import main

@main.route('/')
def index():
    lista = [1, 2, 3, 4, 5]
    #return render_template('index.html', lista=lista)
    return render_template('extend.html')