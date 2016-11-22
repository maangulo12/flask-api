#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.py
    ~~~~~~

    A Flask application with several Flask extensions.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
