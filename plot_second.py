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

######### hall voltage ###########

# Hall voltage in volts
vh_yaxis = df["V_H / muV"]*10**-6

# alternative data: drop last row since current showed 9.7 A and not 10.0 A (not used here)
vh_yaxis_drop = vh_yaxis.drop(20, axis="index")

# magnetic field strength in Teslas
bstrength_T = df["B / mT"]*10**-3

# drop last row for reason above (not used here)
bstrength_T_drop = bstrength_T.drop(20, axis="index")

# we want to find gradient of graph, so we find the variable, x, which consists of a range of terms
def x_axis(B):
    # transverse current at a constant 10 A
    I_t = 10
    # thickness of sample 
    t = 50*10**-6
    return (I_t*B)/t

find_x_axis = x_axis(bstrength_T)

best_fit = linregress(find_x_axis, vh_yaxis)

print("************************************")
print(f"Gradient: {best_fit.slope} +/- {best_fit.stderr:.4f}")
print(f"Intercept: {best_fit.intercept} +/- {best_fit.intercept:.4f}")
print(f"R-squared value: {best_fit.rvalue**2}")
print("************************************")

ylin = best_fit.slope*find_x_axis + best_fit.intercept

plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.title(r"$ V_{H}$  against  $\frac{I_{T} \times B}{t}$")
plt.xlabel(r"$\frac{I_{T} \times B}{t}$ / $\frac{AT}{m}$")
plt.ylabel("Hall voltage / V")

plt.scatter(find_x_axis.array, vh_yaxis.array, label="Data points")
plt.plot(find_x_axis, ylin, color="red", label="Best fit")
plt.legend()
plt.show()

