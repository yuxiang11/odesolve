"""
Created on Fri Aug  5 13:57:05 2022

@author: Yuxiang Sun
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from odesolve import solveto, rk4

def f(X, t):
    return X

x0 = 1
H = np.linspace(0.00001, 0.1, 20000)  # array of step size

Xt = []     # for euler
for h in H:
    Xt.append(math.e - solveto(f, x0, 0, 1, h))

X2t = []    # for rk4
for h in H:
    X2t.append(math.e - solveto(f, x0, 0, 1, h, rk4))

plt.xlabel('h')
plt.ylabel('error')
plt.xscale("log")       # this set the x-axis to log style
plt.yscale("log")       # this set the y-axis to log style
plt.plot(H, Xt, '.')
plt.plot(H, X2t, '.')
plt.legend(["Euler", "RK4"], loc="upper left")
plt.title("Comparison of errors for Euler and RK4")
plt.savefig('coe.pdf')      # title is Comparison Of Errors

plt.show()