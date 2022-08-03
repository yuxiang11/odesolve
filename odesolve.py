# odesolve.py
#
# Author: Yuxiang Sun
# Date:   30/07/2022
# Description: This is the main py file odesolve
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

import numpy as np      # array is needed for odesolve

def euler(f, x, t, h):
    """Perform one step of the Euler method"""
    return x + f(x, t) * h


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    k1 = f(x, t)
    k2 = f(x + k1 * h / 2, t + h / 2)
    k3 = f(x + k2 * h / 2, t + h / 2)
    k4 = f(x + k3 * h, t + h)
    return x + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    while t1 < t2:
        # If the stepsize does not evenly divide the interval,
        # then the last step uses t2 instead of using t1 + hmax
        h = hmax if t1 + hmax < t2 else t2-t1
        # If the method is rk4 then use rk4 else use euler
        x1 = rk4(f, x1, t1, h) if method == rk4 else euler(f, x1, t1, h)
        t1 += h
    return x1  # This x1 is actually the final x2


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    result = []
    for i in t:
        result.append(solveto(f, X0[0], 0, i, hmax, method))    # X0[0] is used because X0 is an array
    return np.array(result)


