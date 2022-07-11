# -*- coding: UTF-8 -*-
import pickle
import gzip

#讀取Model
with open('./xgboost-1.pickle', 'rb') as f:
    xgboostModel = pickle.load(f)


def predict(input):
    pred=xgboostModel.predict(input)[0]
    print(pred)
    return pred
