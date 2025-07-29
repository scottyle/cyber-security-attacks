import matplotlib.pyplot as plt

def plot_monthly_events(events_per_month):
    """
    Plot the number of cyber attacks per month.
    Args:
        events_per_month (pd.Series): Series containing the count of events per month.
    Returns:
        Displays a bar chart of the number of cyber attacks per month.
    """
    
    plt.figure(figsize=(14, 6))
    plt.bar(events_per_month.index, events_per_month.values, color='steelblue')
    plt.title('Cyber Attacks Per Month')
    plt.xlabel('Year-Month')
    plt.ylabel('Number Of Attacks')
    plt.xticks(rotation=45, ha='right') 
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def plot_number_of_attacks(data):
    """
    Count the number of attacks by type and plot a pie chart.
    Args:
        data (pd.DataFrame): DataFrame containing the cyber attack data.
    Returns:
        Displays a pie chart of the distribution of cyber attacks by type.
    """

    attack_counts = data['Attack Type'].value_counts()
    # Plot the pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(attack_counts, labels=attack_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20c.colors)
    plt.title('Distribution of Cyber Attacks by Type')      
    plt.show()