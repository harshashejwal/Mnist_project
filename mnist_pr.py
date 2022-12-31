from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
'''pickle_in=open('model1.pkl','rb')
model=pickle.load(pickle_in)'''

@app.route('/')
def home():
    return "hello"





if __name__=='__main__':
    app.run(debug=True)