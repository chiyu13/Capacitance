# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:19:20 2023

@author: USER
"""

#%% Libraries, import whatever I need
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
from scipy.optimize import curve_fit
import scipy as sp


#%% Raw data

freq = np.array([10000,
20000,
30000,
40000,
50000,
60000,
70000,
80000,
90000,
100000
])

rat = np.array([0.243882744,
0.480385234,
0.718540581,
0.955531935,
1.186607036,
1.41389061,
1.636644463,
1.863042387,
2.077398763,
2.295476584
])

err_rat = np.array([0.004,
0.009,
0.012,
0.015,
0.017,
0.021,
0.022,
0.024,
0.025,
0.028
])

#%% fitting


fit, cov = np.polyfit(freq, rat, 1, w = 1/err_rat, cov = 'TRUE')

p = np.poly1d(fit)
print(fit)
print(np.sqrt(cov))



#%% Plotting


plt.errorbar(freq, rat, yerr = err_rat, ls = 'none', linewidth = 1, capsize = 2.5)
plt.plot(freq, rat, 'bo')
plt.plot(freq, p(freq), 'r-')
plt.title("Frequency against the voltage ratio")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage ratio (dimensionless)")
plt.savefig("plot2", dpi = 700)
plt.show()


