import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pylab
from scipy.stats import *

samp_1 = np.loadtxt('Type-2/f2/f2_circinus_linear.dat', unpack=True)
samp_2 = np.loadtxt('Type-2/f2/f2_ic5063_linear.dat', unpack=True)
samp_3 = np.loadtxt('Type-2/f2/f2_mcg5-23-16_linear.dat', unpack=True)
samp_4 = np.loadtxt('Type-2/f2/f2_ngc1068_linear.dat', unpack=True)
samp_5 = np.loadtxt('Type-2/f2/f2_ngc2110_linear.dat', unpack=True)
samp_6 = np.loadtxt('Type-2/f2/f2_ngc3081_linear.dat', unpack=True)
samp_7 = np.loadtxt('Type-2/f2/f2_ngc5506_linear.dat', unpack=True)
samp_8 = np.loadtxt('Type-2/f2/f2_ngc7582_linear.dat', unpack=True)
samp_9 = np.loadtxt('Type-2/f2/f2_ngc7674_linear.dat', unpack=True)

