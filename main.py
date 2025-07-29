import pandas as pd 
import numpy as np
from graphs.graphs import plot_monthly_events, plot_number_of_attacks
from scripts.clean import clean_data

"""
Hypothesis of the dataset: 
1. A majority of cybersecurity attacks are DDos attacks. 
2. A majority of the attacks are located outside of the US specifically in Asia and then Europe. 
3. For malware attacks, these attacks are more common outside of the environment. 
4. There is a raise of attacks in the last 5 years. 
"""

# Load the dataset 
data = pd.read_csv('data/cybersecurity_attacks.csv')

#Get basic information about the dataset
print(data.info())

# Length of the dataset
print(f"Length of the dataset: {len(data)}")

# Check for missing values 
print(data.isnull().sum())

print(data.head())  # Display the first few rows of the dataset

#Clean the data before plotting
data, events_per_month = clean_data(data)

#Plot the number of cyber attacks per month
plot_monthly_events(events_per_month)

# Plot the number of attacks by type
plot_number_of_attacks(data)

