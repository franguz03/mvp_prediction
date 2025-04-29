import joblib
import pandas as pd

## test using new data, 2024 season

model=joblib.load('models/best_model_pipeline.pkl')
to_predict=pd.read_csv('data/to_predict_2024.csv')
features=to_predict[['Age','G', 'GS', 'MP', 'FG', 'FGA',
       'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA',
       'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS',
        'Year', 'W', 'L',
       'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']]

predictions=model.predict(features)

df = pd.DataFrame({
    'Player': to_predict['Player'],
    'Predictions': predictions
})

print(df.sort_values(by='Predictions', ascending=False).head(10))
