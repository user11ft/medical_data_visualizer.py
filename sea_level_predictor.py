# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Read CSV file
df = pd.read_csv('epa-sea-level.csv')

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

# -----------------------------
# Line of Best Fit (All Data)
# -----------------------------
slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Generate x values from first year to 2050
x_all = np.arange(df['Year'].min(), 2051)
y_all = intercept_all + slope_all * x_all

plt.plot(x_all, y_all, 'r', label='Best Fit (All Data)')

# -----------------------------
# Line of Best Fit (2000 Onwards)
# -----------------------------
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

x_recent = np.arange(2000, 2051)
y_recent = intercept_recent + slope_recent * x_recent

plt.plot(x_recent, y_recent, 'green', label='Best Fit (2000-Present)')

# -----------------------------
# Labels and Title
# -----------------------------
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
