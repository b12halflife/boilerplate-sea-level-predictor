import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # first scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],color='green')

    # line plot (1880-2050)
    garis1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_a = np.arange(df['Year'].min(),2050,1)
    y_a = x_a* garis1.slope + garis1.intercept

    plt.plot(x_a,y_a,color='red', label='1880-2050')

    # Create second line of best fit
    potong =df[df['Year']>= 2000]

    garis2 = linregress(potong['Year'],potong['CSIRO Adjusted Sea Level'])
    x_b = np.arange(2000,2050,1)
    y_b = x_b* garis2.slope + garis2.intercept

    plt.plot(x_b,y_b,color='blue', label='2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()