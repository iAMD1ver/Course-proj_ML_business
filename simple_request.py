import pandas as pd
import numpy as np
from urllib import request, parse
import urllib.request
import json

X_test = pd.read_csv("X_test.csv", index_col=[0])
y_test = pd.read_csv("y_test.csv", index_col=[0])

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100



def get_prediction(date, curs_y, WA_TOD_RATE, VALUE_TOD, WA_TOM_RATE, VALUE_TOM, Rate, value_x, value_y, Brent, t_1, t_2):
    body = {'date':date,
            "curs_y": curs_y,
            "WA_TOD_RATE": WA_TOD_RATE,
            "VALUE_TOD": VALUE_TOD,
            "WA_TOM_RATE": WA_TOM_RATE,
            "VALUE_TOM": VALUE_TOM,
            "Rate": Rate,
            " value_x": value_x,
            " value_y": value_y,
            "Brent": Brent,
            "t-1": t_1,
            "t-2": t_2}

    myurl = "http://127.0.0.1:5000/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

if __name__=='__main__':
    predictions = X_test.apply(lambda x: get_prediction(x.name, x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10]), axis=1, result_type='reduce')
    er_g = mean_absolute_percentage_error(y_true=y_test, y_pred=predictions)
    print('ошибка градиентного бустинга :  ', er_g, '%')