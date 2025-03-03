from unittest import result
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

##route to handle the home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=float(request.form.get('writing_score')),
            reading_score=float(request.form.get('reading_score')),
        ) 
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        # predict_pipeline.predict(pred_df)
        result = predict_pipeline.predict(pred_df)  # Store the prediction in a variable
        return render_template('home.html',results = result[0])
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)