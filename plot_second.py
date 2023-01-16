# for second dataset (prefer)

# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

df = pd.read_csv("hall_csv_second.csv", sep=",", header=1)

df

########### calibration ##########

# Set plot parameters
plt.rcParams["figure.figsize"] = [12, 8]
plt.rcParams["axes.titlesize"] = 20
plt.rcParams["axes.labelsize"] = 16
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
plt.rcParams["legend.fontsize"] = 16

# setup
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.title("Magnetic field as a function of coil current")
plt.xlabel("Coil current / A")
plt.ylabel("Magnetic field strength / mT")

# Plot calibration data
plt.scatter(df['Coil Current / A'], df['B Avg / mT'])
plt.show()


