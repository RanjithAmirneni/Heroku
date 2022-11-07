#This is going to be a python flask application where it can load your model, predict the result and give back result
#To anybody who is asking for the model.

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import joblib


app=Flask(__name__)

model =joblib.load("C:\\Users\\GS574NS\\my_projects\\DS_Model_Deployment\\pipe_pklfile.pkl")

@app.route('/')

def hi():
    return render_template('index.html')

@app.route('/hello')

def hello():
    return "Hello how are you"

@app.route('/predict',methods=['POST'])

def predict():
    print(request.form.values())
    inp = [ i for i in request.form.values()]
    test= {'experience':inp[0],
       'test_score':int(inp[1]),
       'interview_score':int(inp[2])
       }
    print(test)
    test_df= pd.DataFrame([test])
    res= model.predict(test_df)
    #return str(res[0])
    return render_template('index.html',prediction="Employee Salary Is :{} ".format(str(res[0])))


if __name__=="__main__":
  app.run(debug= True)