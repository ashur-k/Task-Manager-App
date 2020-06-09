#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1> Indented Properly </h1>'


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )
