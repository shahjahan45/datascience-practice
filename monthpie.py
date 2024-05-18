import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': list(range(1, 32)),
    'Daily Earning': [
        16440, 9430, 17406, 7064, 0, 8175, 20565, 9575, 7813, 0,
        0, 0, 9928, 10242, 26248, 11265, 13530, 23865, 0, 15590,
        12160, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
    'Target': [
        328278, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total earnings and remaining target
total_earning = df['Daily Earning'].sum()
target = df['Target'][0]  # Assuming the target is constant for all days
remaining_target = target - total_earning

# Create a pie chart
labels = ['Total Earning', 'Remaining Target']
sizes = [total_earning, remaining_target]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)  # Explode the "Total Earning" slice

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.title('Daily Earning and Remaining Target')

plt.show()
