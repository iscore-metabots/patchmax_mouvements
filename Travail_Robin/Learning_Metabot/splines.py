import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

XS = np.linspace(-np.pi,np.pi, num=10, endpoint=True)
YS = np.cos(XS)

QS2 = interp1d(XS, YS, kind='cubic')
xnew = np.linspace(-np.pi, np.pi, num=20, endpoint=True)
plt.plot(XS, YS, 'o', xnew, QS2(xnew), '--')

plt.plot(XS,YS)
plt.show()

