import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def linear_regression_trend_analysis(data):
    """
    Perform linear regression to predict the number of cyber attacks per month over time.
    """
    # Convert timestamp to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Extract Year-Month
    data['Month'] = data['Timestamp'].dt.to_period('M').astype(str)
    
    # Count attacks per month
    monthly_attacks = data.groupby('Month').size().reset_index(name='AttackCount')
    
    # Convert month to numeric values (e.g., 0, 1, 2, ...) for regression
    monthly_attacks['MonthIndex'] = np.arange(len(monthly_attacks))

    # X = month index (time), y = attack count
    X = monthly_attacks[['MonthIndex']]
    y = monthly_attacks['AttackCount']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predictions
    monthly_attacks['Predicted'] = model.predict(X)
    
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_attacks['Month'], monthly_attacks['AttackCount'], label='Actual', marker='o')
    plt.plot(monthly_attacks['Month'], monthly_attacks['Predicted'], label='Predicted', linestyle='--')
    plt.xticks(rotation=45)
    plt.xlabel('Year-Month')
    plt.ylabel('Attack Count')
    plt.title('Cyber Attacks Trend Over Time (Linear Regression)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def multivariate_linear_regression_analysis(data):

    # Ensure Timestamp is datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Extract month and year
    data['Month'] = data['Timestamp'].dt.to_period('M').astype(str)

    # Group by month
    monthly_data = data.groupby('Month').agg({
        'Anomaly Scores': 'mean',     # average anomaly score per month
        'Timestamp': 'count'          # count of attacks per month
    }).reset_index()

    # Rename columns for clarity
    monthly_data.columns = ['Month', 'AvgAnomalyScore', 'AttackCount']

    # Convert month to numeric values (e.g., 0, 1, 2, ...) for regression subce month index is represented as a string 
    monthly_data['MonthIndex'] = np.arange(len(monthly_data))

    # Prepare independent vars and y dependent var
    X = monthly_data[['MonthIndex', 'AvgAnomalyScore']]
    y = monthly_data['AttackCount']

    # Train multivariate linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict attack counts
    monthly_data['PredictedAttackCount'] = model.predict(X)

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Month'], monthly_data['AttackCount'], marker='o', label='Actual Attacks')
    plt.plot(monthly_data['Month'], monthly_data['PredictedAttackCount'], linestyle='--', label='Predicted Attacks')
    plt.xticks(rotation=45)
    plt.xlabel('Year-Month')
    plt.ylabel('Number of Attacks')
    plt.title('Multivariate Linear Regression: Predicting Cyber Attacks')
    plt.legend()
    plt.tight_layout()
    plt.show()


def multivariate_linear_regression_analysis_2_variables(data):

    # Convert Timestamp to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Extract month-year as string
    data['Month'] = data['Timestamp'].dt.to_period('M').astype(str)

    # Group by Month and Protocol
    monthly_data = data.groupby(['Month', 'Protocol']).agg({
        'Anomaly Scores': 'mean',
        'Timestamp': 'count'
    }).reset_index()

    # Rename
    monthly_data.columns = ['Month', 'Protocol', 'AvgAnomalyScore', 'AttackCount']

    # Create MonthIndex
    unique_months = monthly_data['Month'].unique()
    month_index_map = {month: i for i, month in enumerate(sorted(unique_months))}
    monthly_data['MonthIndex'] = monthly_data['Month'].map(month_index_map)

    # One-hot encoding of 'Protocol'
    protocol_dummies = pd.get_dummies(monthly_data['Protocol'], prefix='Protocol')

    # Combine with the rest of the data
    X = pd.concat([
        monthly_data[['MonthIndex', 'AvgAnomalyScore']],
        protocol_dummies
    ], axis=1)

    y = monthly_data['AttackCount']

    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    monthly_data['PredictedAttackCount'] = model.predict(X)

    # Optional: Show predictions vs actuals per month + protocol (aggregated)
    agg = monthly_data.groupby('Month')[['AttackCount', 'PredictedAttackCount']].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(agg['Month'], agg['AttackCount'], marker='o', label='Actual Attacks')
    plt.plot(agg['Month'], agg['PredictedAttackCount'], linestyle='--', label='Predicted Attacks')
    plt.xticks(rotation=45)
    plt.xlabel('Year-Month')
    plt.ylabel('Attack Count')
    plt.title('Multivariate Regression with Protocol, Time, Anomaly Score')
    plt.legend()
    plt.tight_layout()
    plt.show()