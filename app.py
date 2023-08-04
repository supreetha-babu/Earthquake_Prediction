# Author: Pooja Pedgaonkar
# Import 
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

# Flask app
app = Flask(__name__)

# Load model
model=pickle.load(open('C:/Users/welcome/Downloads/Earthquake-Prediction-main/Earthquake-Prediction-main/model.pkl','rb'))

# To str
def to_str(var):
     return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/prediction' , methods=['POST','GET'])
def prediction():
    data1 = int(float(request.form['a']))
    data2 = int(float(request.form['b']))
    data3 = int(float(request.form['c']))
    print(data1,data2,data3)
    arr = np.array([[data1, data2, data3]])
    output= model.predict(arr)

    if output<4:
        return render_template('prediction.html',p=to_str(output), q=' No ')
    elif output>=4 & output<6:
        return render_template('prediction.html',p=to_str(output), q= ' Low ')
    elif output>=6 & output<8:
        return render_template('prediction.html',p=to_str(output), q=' Moderate ')
    elif output>=8 & output<9:
        return render_template('prediction.html',p=to_str(output), q=' High ')
    elif output>=9:
        return render_template('prediction.html',p=to_str(output), q=' Very High ')
    
    else :
        return render_template('prediction.html',p=' N.A.', q= ' Undefined ')



if __name__ == "__main__":
    app.run(debug=True)