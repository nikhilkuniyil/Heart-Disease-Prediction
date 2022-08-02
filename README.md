# Heart Disease Prediction

## Overview<br/>
Heart Disease accounts for nearly 700,000 deaths annually in the US, which is approximately 1 in 5 deaths. The objective of this data project was to implement a machine learning model using logistic regression, to accurately predict whether a patient has heart disease or not depending on a set of select features:<br/>
• Age<br/>
• Sex<br/>
• Chest Pain Type (4 values)<br/>
• Blood Pressure<br/>
• Cholesterol Level<br/>
• Blood Sugar Level<br/>
• Resting ElectrocardiographicRresults (values 0,1,2)<br/>
• Maximum Heart Rate<br/>
• Exercise Induced Angina (values 1,0)<br/>
• ST depression induced by exercise relative to rest<br/>
• Slope of the peak exercise ST segment<br/>
• Number of major vessels (0-3) colored by flourosopy<br/>
• Thalassemia: 0 = normal; 1 = fixed defect; 2 = reversable defect<br/>

## Programming Languages / Libraries<br/>
• Python<br/>
• NumPy<br/>
• Pandas<br/>
• Scikit-learn<br/>
• Flask<br/>
• HTML<br/>

## Data<br/>
The dataset used can be found here:<br/>
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

## File Descriptions<br/>
### **'HeartDiseasePrediction.ipynb'**<br/>
• Jupyter notebook containing the logistic regression machine learning model predicting whether the patient has heart disease or not

### **'app.py'**<br/>
• Python file containing code implementing a flask application and integrating the ML model with the HTML frontend 

### **'heart.csv'**<br/>
• CSV file containing the heart disease prediction dataset used in the project

### **'index.html'**<br/>
• HTML file containing the app's frontend

### **'model.py'**<br/>
• Python file containing the code for the logistic regression predictive model
