from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open("model.pkl",'rb'))

@app.route('/')
def home():
    return render_template('index.html',result=None)

@app.route('/predict',methods=['POST'])
def prediction():
    area=float(request.form['area'])
    prediction=model.predict([[area]])
    return render_template('index.html',result=f'Predicted Price :₹{int(prediction[0])}') 


if __name__=='__main__':
    app.run(debug=True)
