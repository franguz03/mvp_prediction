import joblib
import pandas as pd
from flask import Flask, render_template, request




app = Flask(__name__)

## load model and data
model=joblib.load('models/best_model_pipeline.pkl')

pred_features = ['Age','G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%',
                 '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB',
                 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year', 'W', 'L',
                 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']

## defining app and routes

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals(), pred_features=pred_features)

@app.route('/predict', methods=['POST'])
def predict():
    input_values = []
    for feature in pred_features:
        value = float(request.form[feature])
        input_values.append(value)
    
  
    result = model.predict([input_values])[0]

    return render_template('index.html', **locals(), pred_features=pred_features)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

