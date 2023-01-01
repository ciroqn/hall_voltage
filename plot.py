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


