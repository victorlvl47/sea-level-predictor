import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

called_function_at_leat_once = False

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x_years = df['Year']
    y_sea_level = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x_years, y_sea_level,
                c=y_sea_level, cmap='viridis_r')
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Create first line of best fit
    lin_out = linregress(x_years, y_sea_level)
    min_year = np.min(x_years)
    proyected_year = 2050
    x_fit = np.linspace(min_year, proyected_year)
    y_fit = x_fit * lin_out[0] + lin_out[1]

    plt.plot(x_fit, y_fit, color="red", label='best fitted line')

    # Create second line of best fit


    # Add labels and title

    # FIX ME: Quick hack to call this functions once.
    global called_function_at_leat_once
    if not called_function_at_leat_once:
        plt.legend()
        plt.colorbar()
        called_function_at_leat_once = True

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()