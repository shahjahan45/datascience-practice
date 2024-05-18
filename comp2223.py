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
plt.plot(summary['Month'], summary['2023 Actual'], marker='o', label='2023 Actual')
plt.plot(summary['Month'], summary['2022 Actual'], marker='o', label='2022 Actual')
plt.plot(summary['Month'], summary['Target'], marker='o', label='Target')
plt.xlabel('Month')
plt.ylabel('Amount (QAR)')
plt.title('Actual Earnings Comparison (2022 vs. 2023)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
