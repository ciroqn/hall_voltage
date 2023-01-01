# Importing libraries
import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

df = pd.read_csv("calibration_hall.csv", sep=",", header=2)

df 
