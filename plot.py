# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

################# Part I: Calibration (finding mag. field strength at different coil current measurements) ####################

df = pd.read_csv("calibration_hall.csv", sep=",", header=2)

df 

# get data for average magnetic field strength (in mT) and coil current (in A) from calibration
with open("calibration_hall.csv", mode="r") as calib_points:
    avg_mag = df["Average"]  # or calib_points["Average"] - doesn't matter...
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


############### Part II: Hall voltage (finding R_H, which is the gradient ################

# Averaging readings for V_0 (when I_c is zero) in order calculate Hall voltage
v0_sum = -23.96-23.85-23.87
v0_avg = float("{:.2f}".format(v0_sum/3))

print("The average of v0 is", v0_avg)

# Finding Hall voltage for each measurment where I_c ranges from 0 - 10 A and the transverse current is 10 A
df_hall = pd.read_csv("hall_voltage.csv", sep=",", header=2)

# check
df_hall

################ Prepare data to plot V_H against variables (i.e. magnetic field strength as measured in calibration part) #################

# Hall voltage in volts
vh_yaxis = df_hall["V_h"]*10**-6

# magnetic field strength in Teslas
bstrength_T = df_hall["B / mT"]*10**-3

# we want to find gradient of graph, R_H, so we find the variable, x, which consists of a range of terms i.e. ( I_t * B ) / t
def x_axis(B):
    # Only variable here is the vary mag. field strength which is dependent on coil current (measured in Part I
    # transverse current at a constant 10 A
    I_t = 10
    # thickness of sample i.e. 50 micrometres
    t = 50*10**-6
    return (I_t*B)/t

find_x_axis = x_axis(bstrength_T)

best_fit = linregress(find_x_axis, vh_yaxis)

print("************************************")
print(f"Gradient: {best_fit.slope} +/- {best_fit.stderr}")
print(f"Intercept: {best_fit.intercept} +/- {best_fit.intercept}")
print(f"R-squared value: {best_fit.rvalue**2}")
print("************************************")

ylin = best_fit.slope*find_x_axis + best_fit.intercept

plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.title("Hall voltage as a function of transverse current and magnetic field strength")
plt.xlabel("x")
plt.ylabel("Hall voltage / V")

plt.scatter(find_x_axis.array, vh_yaxis.array, label="raw data")
plt.plot(find_x_axis, ylin, color="red", label="linear fit")
plt.legend()
plt.show()
