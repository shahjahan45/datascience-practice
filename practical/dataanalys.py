# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('sales_data.csv')

# Display basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Data cleaning
df = df.dropna()  # Drop rows with missing values
df['date'] = pd.to_datetime(df['date'])  # Convert 'date' column to datetime

# Line plot for sales over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='sales')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Bar plot for sales by category
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='category', y='sales', estimator=sum)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

# Histogram of sales
plt.figure(figsize=(10, 6))
sns.histplot(df['sales'], bins=20, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
