from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Loading the model
model = joblib.load('/content/models/saas_resolution_model.pkl')

@app.post("/predict")
def predict(data: dict):
    # Create the DataFrame
    df = pd.DataFrame([data])
    
    # Fill missing columns with defaults to match model requirements
    df['day_of_week'] = 0
    df['priority_numeric'] = 1
    df['channel'] = 'email'
    df['category'] = 'general'
    df['raw_text'] = data.get('text', '')
    df['hour_of_day'] = 12
    df['sla_limit'] = 24
    df['sentiment_numeric'] = 0.5
    
    # Run prediction
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
