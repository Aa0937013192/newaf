# -*- coding: UTF-8 -*-
import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input = np.array([[6.7, 195.65, 128.0876,16.21 ]])
    result = model.predict(input)
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues["M"]
    x2=insertValues["VS30"]
    x3=insertValues[ "r"]
    x4=insertValues["Depth"]

    input = np.array([[x1, x2, x3, x4]])
    # 進行預測
    result = model.predict(input)

    return jsonify({'result': str(result)})
