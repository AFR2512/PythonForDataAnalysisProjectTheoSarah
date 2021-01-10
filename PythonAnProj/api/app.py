# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:12:31 2021

@author: Sarah
"""

from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'C:\\Users\\salom\\Documents\\Python\\api.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')