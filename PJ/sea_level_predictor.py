import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("epa-sea-level.csv")


def draw_plot():

    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue")

    # First regression (all data)
    slope, intercept, r, p, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = pd.Series(range(df["Year"].min(), 2051))

    ax.plot(
        years_extended,
        intercept + slope * years_extended,
        color="red"
    )

    # Second regression (from 2000)
    df_2000 = df[df["Year"] >= 2000]

    slope2, intercept2, r2, p2, std_err2 = linregress(
        df_2000["Year"],
        df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000 = pd.Series(range(2000, 2051))

    ax.plot(
        years_2000,
        intercept2 + slope2 * years_2000,
        color="green"
    )

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")

    return fig