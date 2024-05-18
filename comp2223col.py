# import pandas as pd
# import matplotlib.pyplot as plt

# # Create DataFrame from the provided data
# data = {
#     'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
#     '2023 Actual': [502493, 390239, 364331, 226815, 306680, 366767, 207297, 273629, 263155, 319812, 286209, 355110],
#     '2022 Actual': [363765, 260850, 282606, 295719, 335052, 383278, 391424, 386748, 302620, 381005, 386464, 415024],
#     'Target': [328278] * 12
# }

# df = pd.DataFrame(data)

# # Sort the DataFrame by month
# df['Month'] = pd.Categorical(df['Month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
# df = df.sort_values('Month')

# # Summarize the data
# summary = df.groupby('Month', observed=False).sum().reset_index()

# # Check if actual amounts exceed the target amounts for both years
# exceed_target_2023 = all(summary['2023 Actual'] >= summary['Target'])
# exceed_target_2022 = all(summary['2022 Actual'] >= summary['Target'])

# # Visualize the data
# plt.figure(figsize=(10, 6))
# bar_width = 0.25
# index = summary.index

# # Plot the bars for 2023 Actual
# bars_2023_actual = plt.bar(index - bar_width, summary['2023 Actual'], width=bar_width, label='2023 Actual', color='green')

# # Plot the bars for 2022 Actual
# bars_2022_actual = plt.bar(index, summary['2022 Actual'], width=bar_width, label='2022 Actual', color='red')

# # Plot the bars for Target
# bars_target = plt.bar(index + bar_width, summary['Target'], width=bar_width, label='Target', color='purple')

# # Mark the columns if actual amounts reach or exceed the target amounts
# if exceed_target_2023:
#     for i in range(len(summary)):
#         plt.text(index[i] - bar_width / 2, summary.loc[i, 'Target'] + 1000, '*', ha='center', va='bottom', color='blue', fontsize=16)
        
# if exceed_target_2022:
#     for i in range(len(summary)):
#         plt.text(index[i], summary.loc[i, 'Target'] + 1000, '*', ha='center', va='bottom', color='orange', fontsize=16)

# # Display actual amount values on top of each column (vertical)
# for bar, actual in zip(bars_2023_actual, summary['2023 Actual']):
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), actual, ha='center', va='bottom', color='black', rotation=90)

# for bar, actual in zip(bars_2022_actual, summary['2022 Actual']):
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), actual, ha='center', va='bottom', color='black', rotation=90)

# plt.xlabel('Month')
# plt.ylabel('Amount (QAR)')
# plt.title('Actual Earnings Comparison (2022 vs. 2023)')
# plt.xticks(index, summary['Month'], rotation=45)  # Set x-axis ticks to show all months
# plt.xlim(-0.5, 11.5)  # Adjust x-axis limit to include all months
# plt.legend()

# # Hide the duplicate legend entries
# handles, labels = plt.gca().get_legend_handles_labels()
# unique_labels = list(set(labels))
# plt.legend(handles=[handles[labels.index(label)] for label in unique_labels])

# plt.tight_layout()
# plt.show()
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

# Summarize the data
summary = df.groupby('Month').sum().reset_index()

# Visualize the data
plt.figure(figsize=(10, 6))
bar_width = 0.25
index = summary.index

# Plot the bars for 2023 Actual
bars_2023_actual = plt.bar(index - bar_width, summary['2023 Actual'], width=bar_width, label='2023 Actual', color='skyblue')

# Plot the bars for 2022 Actual
bars_2022_actual = plt.bar(index, summary['2022 Actual'], width=bar_width, label='2022 Actual', color='orange')

# Plot the bars for Target
bars_target = plt.bar(index + bar_width, summary['Target'], width=bar_width, label='Target', color='green')

# Mark the columns with a star if actual reaches target
for i in range(len(summary)):
    if summary.loc[i, '2023 Actual'] >= summary.loc[i, 'Target']:
        plt.plot(index[i] - bar_width / 2, summary.loc[i, 'Target'], marker='*', markersize=12, color='red')

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
