import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

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

# Convert the 'Timestamp' column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

# Drop rows where the timestamp couldn't be parsed
data = data.dropna(subset=['Timestamp'])

# Extract year-month in "YYYY-MM" format
data['YearMonth'] = data['Timestamp'].dt.to_period('M').astype(str)

# Count events per month
events_per_month = data['YearMonth'].value_counts().sort_index()

# Plot the bar graph
plt.figure(figsize=(14, 6))
plt.bar(events_per_month.index, events_per_month.values, color='steelblue')
plt.title('Cyber Attacks Per Month')
plt.xlabel('Year-Month')
plt.ylabel('Number Of Attacks')
plt.xticks(rotation=45, ha='right') 
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# Count the number of attacks by type
attack_counts = data['Attack Type'].value_counts()
# Plot the pie chart
plt.figure(figsize=(10, 8))
plt.pie(attack_counts, labels=attack_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
plt.title('Distribution of Cyber Attacks by Type')      
plt.show()
