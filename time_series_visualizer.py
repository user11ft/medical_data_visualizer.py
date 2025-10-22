# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file and parse dates
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by removing top 2.5% and bottom 2.5% of page views
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

# -----------------------------
# 1. Line Plot Function
# -----------------------------
def draw_line_plot():
    plt.figure(figsize=(15,5))
    plt.plot(df.index, df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.show()

# -----------------------------
# 2. Bar Plot Function
# -----------------------------
def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    
    # Group by Year and Month and calculate mean
    df_grouped = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()
    
    # Ensure months are in calendar order
    months_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
    df_grouped = df_grouped[months_order]
    
    # Plot
    df_grouped.plot(kind='bar', figsize=(15,7))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.show()

# -----------------------------
# 3. Box Plot Function
# -----------------------------
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.strftime('%b')
    df_box['Month_Num'] = df_box['date'].dt.month
    
    # Sort months properly
    df_box = df_box.sort_values('Month_Num')
    
    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(18,6))
    
    # Year-wise Box Plot (Trend)
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='Month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    plt.show()

# Example usage:
# draw_line_plot()
# draw_bar_plot()
# draw_box_plot()
