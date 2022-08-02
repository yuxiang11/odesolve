# odesolve.py
#
# Author: Yuxiang Sun
# Date:   30/07/2022
# Description: This is the main py file odesolve
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

def euler(f, x, t, h):
    """Perform one step of the Euler method"""
    pass


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass
