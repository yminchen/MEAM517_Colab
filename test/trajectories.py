import numpy as np
from math import *

def x_d(t):
  return np.array([3*cos(t), 3*sin(t), atan(3*cos(t)/(9.81 - 3*sin(t))), -3*sin(t), 3*cos(t), (-3*(1 - 0.305810397553517*sin(t))**2*sin(t) + 0.09351999925184*(9.81 - 3*sin(t))*cos(t)**2)/((9.81 - 3*sin(t))*((1 - 0.305810397553517*sin(t))**2 + 0.09351999925184*cos(t)**2))])

def u_d(t):
  return np.array([5.0e-15*(1000000000000.0*sqrt((90000.0*sin(t)**2 - 588600.0*sin(t) + 90000.0*cos(t)**2 + 962361.0)/(90000.0*sin(t)**2 - 588600.0*sin(t) + 962361.0))*(981.0 - 300.0*sin(t))*(729000000000000.0*sin(t)**6 - 1.430298e+16*sin(t)**5 + 1.458e+15*sin(t)**4*cos(t)**2 + 1.169268615e+17*sin(t)**4 - 1.907064e+16*sin(t)**3*cos(t)**2 - 5.0980111614e+17*sin(t)**3 + 729000000000000.0*sin(t)**2*cos(t)**4 + 9.35414892e+16*sin(t)**2*cos(t)**2 + 1.25028723733335e+18*sin(t)**2 - 4.76766e+15*sin(t)*cos(t)**4 - 2.03920446456e+17*sin(t)*cos(t)**2 - 1.63537570643202e+18*sin(t) + 7.7951241e+15*cos(t)**4 + 1.6670496497778e+17*cos(t)**2 + 8.91279760005452e+17) - 83562883710976.0*sin(t)**5*cos(t) + 5.95957500000008e+28*sin(t)**4*cos(t) - 87960930222080.0*sin(t)**3*cos(t)**3 - 3.89756205000002e+29*sin(t)**3*cos(t) + 5.95957500000003e+28*sin(t)**2*cos(t)**3 + 3.94064967394918e+15*sin(t)**2*cos(t) - 3.89756205e+29*sin(t)*cos(t)**3 + 4.1676241244445e+30*sin(t)*cos(t) + 6.37251395174999e+29*cos(t)**3 - 6.81406544346676e+30*cos(t))/(729000000000000.0*sin(t)**6 - 1.430298e+16*sin(t)**5 + 1.458e+15*sin(t)**4*cos(t)**2 + 1.169268615e+17*sin(t)**4 - 1.907064e+16*sin(t)**3*cos(t)**2 - 5.0980111614e+17*sin(t)**3 + 729000000000000.0*sin(t)**2*cos(t)**4 + 9.35414892e+16*sin(t)**2*cos(t)**2 + 1.25028723733335e+18*sin(t)**2 - 4.76766e+15*sin(t)*cos(t)**4 - 2.03920446456e+17*sin(t)*cos(t)**2 - 1.63537570643202e+18*sin(t) + 7.7951241e+15*cos(t)**4 + 1.6670496497778e+17*cos(t)**2 + 8.91279760005452e+17), 5.0e-15*(1000000000000.0*sqrt((90000.0*sin(t)**2 - 588600.0*sin(t) + 90000.0*cos(t)**2 + 962361.0)/(90000.0*sin(t)**2 - 588600.0*sin(t) + 962361.0))*(981.0 - 300.0*sin(t))*(729000000000000.0*sin(t)**6 - 1.430298e+16*sin(t)**5 + 1.458e+15*sin(t)**4*cos(t)**2 + 1.169268615e+17*sin(t)**4 - 1.907064e+16*sin(t)**3*cos(t)**2 - 5.0980111614e+17*sin(t)**3 + 729000000000000.0*sin(t)**2*cos(t)**4 + 9.35414892e+16*sin(t)**2*cos(t)**2 + 1.25028723733335e+18*sin(t)**2 - 4.76766e+15*sin(t)*cos(t)**4 - 2.03920446456e+17*sin(t)*cos(t)**2 - 1.63537570643202e+18*sin(t) + 7.7951241e+15*cos(t)**4 + 1.6670496497778e+17*cos(t)**2 + 8.91279760005452e+17) + 83562883710976.0*sin(t)**5*cos(t) - 5.95957500000008e+28*sin(t)**4*cos(t) + 87960930222080.0*sin(t)**3*cos(t)**3 + 3.89756205000002e+29*sin(t)**3*cos(t) - 5.95957500000003e+28*sin(t)**2*cos(t)**3 - 3.94064967394918e+15*sin(t)**2*cos(t) + 3.89756205e+29*sin(t)*cos(t)**3 - 4.1676241244445e+30*sin(t)*cos(t) - 6.37251395174999e+29*cos(t)**3 + 6.81406544346676e+30*cos(t))/(729000000000000.0*sin(t)**6 - 1.430298e+16*sin(t)**5 + 1.458e+15*sin(t)**4*cos(t)**2 + 1.169268615e+17*sin(t)**4 - 1.907064e+16*sin(t)**3*cos(t)**2 - 5.0980111614e+17*sin(t)**3 + 729000000000000.0*sin(t)**2*cos(t)**4 + 9.35414892e+16*sin(t)**2*cos(t)**2 + 1.25028723733335e+18*sin(t)**2 - 4.76766e+15*sin(t)*cos(t)**4 - 2.03920446456e+17*sin(t)*cos(t)**2 - 1.63537570643202e+18*sin(t) + 7.7951241e+15*cos(t)**4 + 1.6670496497778e+17*cos(t)**2 + 8.91279760005452e+17)])