import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np

app=Flask(__name__)
modl=pickle.load(open('model5.pkl','rb'))

@app.route('/')
def home():
    return "hello world"

@app.route('/predict_api',methods=['POST'])

def predict_api():
    return "welcome to app"

if __name__=='__main__':
    app.run(debug=True)