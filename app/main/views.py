# -*- encoding: utf-8 -*-

from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template("index.html")

