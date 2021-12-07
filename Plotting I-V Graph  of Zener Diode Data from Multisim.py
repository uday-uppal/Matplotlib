import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Dataset
x=np.array([100,200,300,399.95,497.72,566.93,596.45,611.89,621.99,629.42,635.28,640.10,644.19,647.74,650.87])
y=np.array([667.68*pow(10,-12),23.208*pow(10,-9),1.0905*pow(10,-6),51.960*pow(10,-6),2.2774*pow(10,-3),33.073*pow(10,-3),103.55*pow(10,-3),188.11*pow(10,-3),278.01*pow(10,-3),370.58*pow(10,-3),464.72*pow(10,-3),559.90*pow(10,-3),655.81*pow(10,-3),752.26*pow(10,-3),849.13*pow(10,-3)])

#cubic_interploation_model = interp1d(x, y, kind = "cubic")

# Plotting the Graph
#X_=np.linspace(x.min(), x.max(), 500)
#Y_=cubic_interploation_model(X_)

#plt.plot(X_, Y_)
plt.plot(x,y)
plt.title("I-V Characteristic graph of Reverse Bias Zener Diode ")
plt.xlabel("V(Milli Volts)")
plt.ylabel("I(Milli Amperes)")
plt.show()
