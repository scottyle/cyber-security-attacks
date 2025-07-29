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
"""
1. Create a function to clean the data 
 a. For malware indicators, replace NaN with 'No Malware Indicators'
 b. For alerts/warnings, replace NaN with 'Warning'
 c. For proxy information, if Destination IP Address is a private IP address, replace with NaN, all others replace with 'No Proxy Information'
 
Missing values in the dataset 
Timestamp                     0
Source IP Address             0
Destination IP Address        0
Source Port                   0
Destination Port              0
Protocol                      0
Packet Length                 0
Packet Type                   0
Traffic Type                  0
Payload Data                  0
Malware Indicators        20000
Anomaly Scores                0
Alerts/Warnings           20067
Attack Type                   0
Attack Signature              0
Action Taken                  0
Severity Level                0
User Information              0
Device Information            0
Network Segment               0
Geo-location Data             0
Proxy Information         19851
Firewall Logs             19961
IDS/IPS Alerts            20050
Log Source                    0
"""

print(data.head())  # Display the first few rows of the dataset

#Clean the data before plotting
data, events_per_month = clean_data(data)

#Plot the number of cyber attacks per month
plot_monthly_events(events_per_month)

# Plot the number of attacks by type
plot_number_of_attacks(data)

