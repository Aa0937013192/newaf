# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[5.7, 195.65, 128.0876, 0.0005,161,12.837,30,99,202 ]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['M']
    x2=insertValues['Vs30']
    x3=insertValues[ 'r']
    x4=insertValues['PGA_r']
    x5=insertValues['theta']
    x6=insertValues['R']
    x7=insertValues['EL']
    x8=insertValues['phi_1']
    x9=insertValues['Z1.0']
    input = np.array([[x1, x2, x3, x4, x5, x6, x7, x8, x9]])
    # 進行預測
    result = model.predict(input)

    return jsonify({'result': str(result)})