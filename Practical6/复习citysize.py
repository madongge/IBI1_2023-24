import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#creat a dictionary
Activity={
    'Sleeping':8,
    'Classes':6,
    'Studying':3.5,
    'TV':2,
    'Music':1,
    'Other':3.5
          }
total_hour=24
print('dictionary containing the information')
activities = list(Activity.keys())
time_spent = list(Activity.values())
plt.figure(figsize=(10, 8))
plt.title('Average Day of a University Student')
plt.pie(time_spent, labels=activities)
plt.axis('equal')
plt.show()

