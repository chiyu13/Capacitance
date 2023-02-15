#%% Libraries, import whatever I need
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
from scipy.optimize import curve_fit
import scipy as sp


#%% data

time, voltage = np.array(np.loadtxt('Small Cap with 1kHz/1KHZ6.csv', skiprows = 1, delimiter = ',', unpack = 'true'))



#%% functions
def exponent(t, tau, t0):
    return v0*np.exp(-(t-t0)/(tau))


v0 = np.amax(voltage)
print(v0)

p0 = [470*10**(-7), time[36000]]

fit, cov = curve_fit(exponent, time[36500:60000], voltage[36500:60000], p0 = p0)
print(fit[0])
print(np.sqrt(np.diag(cov)))


#%% functions2
def exponent2(t, tau, t0):
    return v0*np.exp(-(t-t0)/(tau))



p02 = [470*10**(-7), time[90800]]
print(time[90800])

fit2, cov2 = curve_fit(exponent2, time[90800:112000], voltage[90800:112000], p0 = p02)
print(fit2[0])
print(np.sqrt(np.diag(cov2)))




#%% plotting data


#plt.plot(time, voltage, 'r.')
plt.plot(time, voltage, 'b.', label=("Oscilloscope output"), ms=3)
plt.plot(time[36500:60000], exponent(time[36500:60000], fit[0]), 'r.', ms=3)
plt.plot(time[90800:112000], exponent(time[90800:112000], fit2[0]), 'r.', label=("Curve fit"), ms=3)
#plt.plot(time[9000:32000], exponent3(time[9000:32000], *fit3[0]), 'r.', ms=0.5)
plt.xlim((-0.0013, 0.0015))
plt.title("Plot of voltage across the capacitor against time")
plt.ylabel("Voltage across the capacitor Vc (V)")
plt.xlabel("Time (s)")
#lgnd = plt.legend(loc = "upper right", fontsize=7, framealpha = 1)


plt.savefig("plot1.png", dpi = 700)
plt.show()
