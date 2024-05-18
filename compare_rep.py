# import pandas as pd
# import matplotlib.pyplot as plt

# # Create a DataFrame from your data
# data = {
#     'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
#     'Actual': [502493, 390239, 364331, 226815, 306680, 366767, 207297, 273629, 263155, 319812, 286209, 355110],
#     'Target': [328278] * 12
# }

# df = pd.DataFrame(data)

# # Add a new column to indicate if the actual amount exceeds the target
# df['Exceeds_Target'] = df['Actual'] >= df['Target']

# # Plot the data
# plt.figure(figsize=(10, 6))

# # Plot actual amount
# plt.bar(df['Month'], df['Actual'], label='Actual', color=df['Exceeds_Target'].map({True: 'green', False: 'blue'}))

# # Plot target amount
# plt.plot(df['Month'], df['Target'], label='Target', color='red', linewidth=2, linestyle='--')

# plt.xlabel('Month')
# plt.ylabel('Amount')
# plt.title('Actual vs. Target Amounts')
# plt.xticks(rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from your data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Actual': [502493, 390239, 364331, 226815, 306680, 366767, 207297, 273629, 263155, 319812, 286209, 355110],
    'Target': [328278] * 12
}

df = pd.DataFrame(data)

# Add a new column to indicate if the actual amount exceeds the target
df['Exceeds_Target'] = df['Actual'] >= df['Target']

# Plot the data
plt.figure(figsize=(10, 6))

# Plot actual amount
bars = plt.bar(df['Month'], df['Actual'], label='Actual', color=df['Exceeds_Target'].map({True: 'green', False: 'red'}))

# Plot target amount
plt.plot(df['Month'], df['Target'], label='Target', color='red', linewidth=2, linestyle='--')

# Display actual amounts on top of each column
for bar, actual in zip(bars, df['Actual']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), actual, ha='center', va='bottom')

plt.xlabel('2023 Target Summary System')
plt.ylabel('Total Amount ')
plt.title('Actual Amount  vs. Target Amounts')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
