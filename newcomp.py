import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame from the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    '2023 Actual': [502493, 390239, 364331, 226815, 306680, 366767, 207297, 273629, 263155, 319812, 286209, 355110],
    '2022 Actual': [363765, 260850, 282606, 295719, 335052, 383278, 391424, 386748, 302620, 381005, 386464, 415024],
    'Target': [328278] * 12
}

df = pd.DataFrame(data)

# Convert 'Month' to categorical with correct order
df['Month'] = pd.Categorical(df['Month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

# Sort the DataFrame by month
df = df.sort_values('Month')

# Summarize the data
summary = df.groupby('Month', observed=False).sum().reset_index()

# Visualize the data
plt.figure(figsize=(10, 6))
bar_width = 0.25
index = summary.index

# Plot the bars for 2023 Actual
bars_2023_actual = plt.bar(index - bar_width, summary['2023 Actual'], width=bar_width, label='2023 Actual', color='green')

# Plot the bars for 2022 Actual
bars_2022_actual = plt.bar(index, summary['2022 Actual'], width=bar_width, label='2022 Actual', color='skyblue')

# Plot the bars for Target
bars_target = plt.bar(index + bar_width, summary['Target'], width=bar_width, label='Target', color='maroon')

# Mark the columns with a star if either 2023 Actual or 2022 Actual reaches or exceeds the target amount
for i in range(len(summary)):
    if summary.loc[i, '2023 Actual'] >= summary.loc[i, 'Target']:
        plt.plot(index[i] - bar_width / 2, summary.loc[i, '2023 Actual'], marker='*', markersize=12, color='red')
    elif summary.loc[i, '2022 Actual'] >= summary.loc[i, 'Target']:
        plt.plot(index[i], summary.loc[i, '2022 Actual'], marker='*', markersize=12, color='red')

# Display actual amount values on top of each column for 2023 Actual (vertical)
for bar, actual in zip(bars_2023_actual, summary['2023 Actual']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), actual, ha='center', va='bottom', color='black', rotation=90)

# Display actual amount values on top of each column for 2022 Actual (vertical)
for bar, actual in zip(bars_2022_actual, summary['2022 Actual']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), actual, ha='center', va='bottom', color='black', rotation=90)

# Add line chart for 2023 Actual
plt.plot(index, summary['2023 Actual'], color='green', marker='o', label='2023 Actual Line')

# Add line chart for 2022 Actual
plt.plot(index, summary['2022 Actual'], color='skyblue', marker='o', label='2022 Actual Line')

plt.xlabel('Month')
plt.ylabel('Amount (QAR)')
plt.title('Actual Earnings Comparison (2022 vs. 2023)')
plt.xticks(index, summary['Month'], rotation=45)
plt.legend()

# Hide the duplicate legend entries
handles, labels = plt.gca().get_legend_handles_labels()
unique_labels = list(set(labels))
plt.legend(handles=[handles[labels.index(label)] for label in unique_labels])

plt.tight_layout()
plt.show()
