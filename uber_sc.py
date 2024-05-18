import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dictionary with the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'],
    'Received_Amount': [
        [2693, 1003, 918, 422, 670, 685, 1269, 1363, 684, 1455, 1025, 494, 720],
        [470, 600, 1070, 226, 1760, 1820, 1040, 1585],
        [705, 446, 1055, 590, 1975, 653, 1935, 2098, 737, 1910, 874, 1010, 684],
        [1782, 475, 686, 3023, 1808, 1823, 246, 2128, 2637],
        [563, 1109, 623, 363, 2126, 2083, 2476, 2948],
        [600, 880, 159, 1065, 200, 1036, 1732, 2751, 1820, 2210, 2075, 102, 1474, 826, 2533],
        [326, 204, 184, 1801, 319, 690, 1734, 841, 1029],
        [1177, 190, 2542, 3012, 953, 554, 637, 1290, 2591, 240]
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the total received amount for each month
total_received_amount = [sum(month_data) for month_data in df['Received_Amount']]

# Plotting
plt.figure(figsize=(10, 6))

# Bar chart
plt.bar(df['Month'], total_received_amount, color='skyblue')
plt.title('Total Received Amount Per Month')
plt.xlabel('Month')
plt.ylabel('Total Received Amount')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
