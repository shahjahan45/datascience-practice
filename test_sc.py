# #Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

# full_health_data = pd.read_csv("data.csv", header=0, sep=",")

# x = full_health_data["Average_Pulse"]
# y = full_health_data["Calorie_Burnage"]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#  return slope * x + intercept

# mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.ylim(ymin=0, ymax=2000)
# plt.xlim(xmin=0, xmax=200)
# plt.xlabel("Average_Pulse")
# plt.ylabel ("Calorie_Burnage")
# plt.show()

# #Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read the data
full_health_data = pd.read_csv("data.csv", header=0, sep=",")

# Extract columns for analysis
x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

# Perform linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Define linear regression function
def myfunc(x):
    return slope * x + intercept

# Generate predicted values
mymodel = myfunc(x)

# Plot the data and regression line
plt.scatter(x, y)
plt.plot(x, mymodel, color='red')
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.title("Linear Regression Analysis")

# Save the plot as an image
plt.savefig("linear_regression_plot.png")

# Display the plot
plt.show()
