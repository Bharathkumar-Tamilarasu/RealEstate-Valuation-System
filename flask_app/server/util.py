import pickle
import json
import os
import numpy as np

def artifacts_loader():
    global _model
    global _locations
    global _bhk
    global _bath
    global _all_columns

    abs_path =  os.path.abspath(__file__)

    # Loading the model
    model_path = os.path.join(abs_path,"../../../artifacts\House Price Prediction_Pickle.pickle")
    model_path_norm = os.path.normpath(model_path)

    with open(model_path_norm,"rb",) as f:
        _model = pickle.load(f)

    # Loading input parameters for form processing and prediction.
    input_path = os.path.join(abs_path,"../../../artifacts\prediction_input.json")
    input_path_norm = os.path.normpath(input_path)
    with open(input_path_norm,'rb') as f:
        _all_inputs = json.load(f)
    
    _locations = _all_inputs['locations']
    _bhk = _all_inputs['bhk']
    _bath = _all_inputs['bath']
    _all_columns = _all_inputs['all_columns']

def locations_loader():
    return _locations

# def estimate_price(bath, bhk, area, location):
def price_estimator(location, bath, bhk, areaSize):
    column_index = (_all_columns).index(location)
    x = [0] * (len(_all_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = areaSize
    x[column_index] = 1
    return round(_model.predict([x])[0], 0)
    
if __name__ == "__main__":
    pass
    

