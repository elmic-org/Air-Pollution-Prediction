import numpy as np
import seaborn as sns
sns.set_theme()
import matplotlib.pyplot as plt

def year_air_pollution_plot(dataset, helpers=True, title=None):
    AQIs = dataset[:, 1]
    days_number = np.arange(AQIs.size)
    year = dataset[0][0][0:4]
    
    plt.plot(days_number, AQIs)

    if helpers:
        # regions
        plt.axhspan(0, 50, color='green', alpha=0.5)
        plt.axhspan(51, 100, color='yellow', alpha=0.5)
        plt.axhspan(101, 150, color='orange', alpha=0.5)
        plt.axhspan(151, 200, color='red', alpha=0.5)
        plt.axhspan(201, 300, color='purple', alpha=0.5)
        plt.axhspan(301, 500, color='brown', alpha=0.5)

        # month seperations
        month_days = 31
        offset = 0
        monthes = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar",
                   "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]
        for i in range(0, 12):
            if i == 6:
                month_days = 30
                offset = 6
            plt.axvspan(i*month_days+offset, (i+1)*month_days+offset, alpha=0.2)
            plt.text(i*month_days+offset+15.5, 400, monthes[i], ha='center', va='center', fontsize=10, color='black', rotation=90)

        # title
        if title:
            plt.title(title)
        else:
            plt.title(year)

        # x-y labels
        plt.xlabel("day")
        plt.ylabel("AQI")

        # turn off the grid
        plt.grid(False)
            