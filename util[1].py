import json
from copyreg import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_prices(location,sqft,bath, balcony, bhk):
    global x
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x_pred = np.zeros(len(__data_columns))
    x_pred[0] = sqft
    x_pred[1] = bath
    x_pred[2] = balcony
    x_pred[3] = bhk
    if loc_index >= 0:
        x_pred[loc_index] = 1


    return round(__model.predict([x]),2)

def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts..start")
    global __data_columns
    global __location

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    global  __model
    with open("./artifacts/banglore_home_price_model",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_prices(('1st Phase JP Nagar',1000,2,1,3)))