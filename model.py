import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def predict(age, sex, chest_pain, blood_pressure, cholesterol, bloodsugar, ekg, heart_rate, angina, stdepression, slope, vessels, thal):
    heart = pd.read_csv('/Users/nikhilkuniyil/Desktop/heart_disease/heart.csv')

    X = heart.drop(columns='target')
    y = heart['target']

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    logr = LogisticRegression()
    logr.fit(X_train,y_train)

    heart_data = np.array((age, sex, chest_pain, blood_pressure, cholesterol, bloodsugar, ekg, heart_rate, angina, stdepression, slope, vessels, thal))

    input_reshape = heart_data.reshape(1,-1)

    scaled_data = scaler.fit_transform(input_reshape)
    prediction = logr.predict(scaled_data)[0]

    if prediction == 1:
        return "Patient has heart disease"
    else:
        return "Patient does not have heart disease"

    

