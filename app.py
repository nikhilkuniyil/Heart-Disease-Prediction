import numpy as np
from flask import Flask, request, jsonify, render_template
import model as m


app = Flask(__name__)


@app.route("/predict", methods = ['POST', 'GET'])

def predict():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chest_pain = request.form['chestpain']
        blood_pressure = request.form['bloodpressure']
        cholesterol = request.form['cholesterol']
        bloodsugar = request.form['bloodsugar']
        ekg = request.form['ekg']
        heart_rate = request.form['heartrate']
        angina = request.form['angina']
        stdepression = request.form['stdepression']
        slope = request.form['slope']
        vessels = request.form['vessels']
        thal = request.form['thal']
        
        heart_disease = m.predict(age, sex, chest_pain, blood_pressure, cholesterol, bloodsugar, ekg, heart_rate, angina, stdepression, slope, vessels, thal)
        return render_template('index.html', prediction_text = heart_disease)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
                               
