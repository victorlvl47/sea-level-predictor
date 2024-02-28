import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

called_colorbar = False

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
                c=df['CSIRO Adjusted Sea Level'], cmap='viridis_r')
    # FIX ME: Quick hack call colorbar() once.
    global called_colorbar
    if not called_colorbar:
        plt.colorbar()
        called_colorbar = True

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()