import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "fcc-forum-pageviews.csv")

df = pd.read_csv(
    csv_path,
    parse_dates=["date"],
    index_col="date"
)

lower = df["value"].quantile(0.025)
upper = df["value"].quantile(0.975)

df = df[(df["value"] >= lower) & (df["value"] <= upper)]


def draw_line_plot():
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df_line.index, df_line["value"], color="red")

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig



def draw_bar_plot():
    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Promedio por año y mes
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_grouped.plot(kind="bar", figsize=(12, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        title="Months",
        labels=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    )

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_box = df.copy()

    df_box.reset_index(inplace=True)

    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig