# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

df = pd.read_csv("calibration_hall.csv", sep=",", header=2)

df 

# get data for average magnetic field strength (in mT) and coil current (in A) from calibration
with open("calibration_hall.csv", mode="r") as calib_points:
    avg_mag = df["Average"]
    coil_current = df["I_c / A"]
    
# convert to arrays
avg_mag_array = avg_mag.array
coil_current_array = coil_current.array

############# Plotting calibration data (i.e. mag. field strength vs varying coil currents ##############
# Sete plot parameters
plt.rcParams["figure.figsize"] = [12, 8]
plt.rcParams["axes.titlesize"] = 20
plt.rcParams["axes.labelsize"] = 16
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
plt.rcParams["legend.fontsize"] = 16

# setup
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.title("Magnetic field strength as a function of coil current")
plt.xlabel("Coil current / A")
plt.ylabel("Magnetic field strength / mT")

# Plot
plt.scatter(coil_current_array, avg_mag_array)
plt.show()
