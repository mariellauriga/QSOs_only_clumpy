import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as sci
from scipy.stats import ks_2samp
#Curva de crecimiento
sx,sy = loadtxt('stadar.dat',unpack=True)
gx,gy = loadtxt('galaxy.dat',unpack=True)
#Flujos diferenciales
asx,df_s=loadtxt('standar_diferential_flux.dat',unpack=True)
agx,df_g=loadtxt('diferential_flux_galxy_clean.dat',unpack=True)

nsx=0.08*sx
ngx=0.08*gx

asx,df_s=0.08*asx,df_s
agx,df_g=0.08*agx,df_g 

s_faper20=8052.978
s_faper15=7724.014
s_faper13=7483.449
s_faper11=7126.203
s_faper9=6564.486
s_faper7=5632.375
s_faper3=2114.015

g_faper20=33.86465
g_faper15=37.4197
g_faper13=36.33251
g_faper11=35.99854
g_faper9 =32.26028
g_faper7 =27.8485
g_faper3= 10.27811

#Incertidumbre
#galaxia
sqrootG = 0.10
#estrella
sqrootS = 0.06

nsy=sy/s_faper3
ngy=gy/g_faper3

 #Estadistica
#Test Kolmogorov-Smirnov Stand
KS_std=ks_2samp(df_s,df_s)
KS_galaxy=ks_2samp(df_s,df_g)

print 'STD=', KS_std
print 'Galaxia=', KS_galaxy

#plt.figure()
#plt.errorbar(nsx,nsy,nsy*sqrootS,color='r')
#plt.errorbar(ngx,ngy,ngy*sqrootG,color='b')
#plt.xlabel("r$_{aperture}$ (arcsec)",fontsize=14)
#plt.ylabel(r"Normalized Flux",fontsize=12)
#text(0.6,0.6, r'Relative to r = 3 pixel (0.24")', color='k',fontsize=14)
plt.figure()
#plt.ylim(-0.4,1.2)
#plt.xlim(0.2,2.5)
plt.errorbar(asx,df_s,df_s*sqrootS,color='r')
plt.errorbar(agx,df_g,sqrootG,color='b')
plt.ylabel('Relative differencial flux')
plt.xlabel('radius(")')
text(1.5,0.6, r'MRK 1014', color='k',fontsize=14)
plt.show()










