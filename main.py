import pandas as pd 
import numpy as np

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

# We see that the dataset has some missing values, we will drop them for now

"""
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