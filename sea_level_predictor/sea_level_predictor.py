import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import os


def draw_plot():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "epa-sea-level.csv")

    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # ===============================
    res = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = np.arange(df["Year"].min(), 2051)
    line = res.slope * years_extended + res.intercept

    ax.plot(years_extended, line, "r")


    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = np.arange(2000, 2051)
    line_recent = res_recent.slope * years_recent + res_recent.intercept

    ax.plot(years_recent, line_recent, "g")

    # Etiquetas
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return fig