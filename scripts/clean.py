import pandas as pd

def clean_data(data):
    """Function is used to clean the cyber security dataset."""

    # Convert the 'Timestamp' column to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

    # Drop rows where the timestamp couldn't be parsed
    data = data.dropna(subset=['Timestamp'])

    # Extract year-month in "YYYY-MM" format
    data['YearMonth'] = data['Timestamp'].dt.to_period('M').astype(str)

    # Count events per month
    events_per_month = data['YearMonth'].value_counts().sort_index()

    return data, events_per_month