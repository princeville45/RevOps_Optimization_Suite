import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_deal_closure(days_in_pipeline, historical_data):
    """
    Predicts the probability of deal closure using Linear Regression.
    Features: days_in_pipeline, interaction_count.
    Target: close_date_offset.
    """
    X = historical_data[['days', 'interactions']]
    y = historical_data['close_offset']
    
    model = LinearRegression()
    model.fit(X, y)
    
    prediction = model.predict(np.array([[days_in_pipeline, 5]]))
    return prediction[0]
