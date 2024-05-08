import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.head(5)
print(dalys_data.info())
dalys_data.iloc[0,3]
dalys_data.iloc[2,0:5]
dalys_data.iloc[0:2,:]
dalys_data.iloc[0:10:2,0:5]