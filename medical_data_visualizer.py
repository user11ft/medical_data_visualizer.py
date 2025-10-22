#Step 1: Import the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv('medical_examination.csv')

#Step 2: Add the overweight column

BMI = weight (kg) / (height (m))²

# Convert height to meters
height_m = df['height'] / 100

# Calculate BMI
bmi = df['weight'] / (height_m ** 2)

# Assign overweight column: 1 if BMI > 25, else 0
df['overweight'] = (bmi > 25).astype(int)

#Step 3: Normalize cholesterol and glucose

0 → good (normal), 1 → bad (above normal)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

#Step 4: Draw Categorical Plot
def draw_cat_plot():
    # Melt the dataset for categorical plot
    df_cat = pd.melt(
        df,
        id_vars='cardio',
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    # Group and count the occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig
    
    return fig

#Step 5: Clean data for Heat Map

Filter out invalid data:

df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

#Step 6: Draw Heat Map
def draw_heat_map():
    # Calculate correlation matrix
    corr = df_heat.corr()

    # Generate a mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmax=0.3,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .5}
    )

    return fig
