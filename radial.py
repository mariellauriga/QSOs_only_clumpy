from scipy.stats import ks_2samp
import matplotlib.pyplot as plt
import scipy as sci
import pylab as pl
import numpy as np
#raperG, FdifG =sci.loadtxt('FC_stck_Mrk1383_combined.1',unpack=True)
raper,a,b67,Fdif67_1,c1,c2,flag =sci.loadtxt('Mrk1014_add_redcvh.fits.mag.1',unpack=True)
raper,a,b69,Fdif69_1,c1,c2,flag =sci.loadtxt('FC_stck_S20130101S7303.fits.mag.1',unpack=True)


#derr67_1=6
#derr69_1=127

derr67_1=0.3
derr69_1=0.12


plt.plot(raper, Fdif67_1/Fdif67_1[5] ,color='green')
plt.plot(raper, Fdif69_1/Fdif69_1[5], 'k--',color='green')
plt.text(0.4,1.3,"r=0.4''", color='green')
plt.plot(raper, Fdif67_1/Fdif67_1[20], color='red')
plt.plot(raper, Fdif69_1/Fdif69_1[20], 'k--',color='red')
plt.text(1,1.1,"r=1.0''", color='red')
plt.plot(raper, Fdif67_1/Fdif67_1[30] ,color='blue')
plt.plot(raper, Fdif69_1/Fdif69_1[30], 'k--',color='blue')
plt.text(1.4,0.8,"r=1.4''", color='blue')
plt.xlabel("$r_{aperture}$ ('')")
plt.ylabel("Relative flux")
plt.text(0.4,0.8,"MRK 1014", color='black')
plt.text(1.1,1.5,"Not sky-sustraction", color='black')

#Radial profile
plt.figure()
plt.ylim(0,1.2)
nraper=((raper[1:]+raper[:-1])/2)*0.08

nFdif67_1=(Fdif67_1[1:]-Fdif67_1[:-1])/(b67[1:]-b67[:-1])
normb_67_1=(Fdif67_1[1]-Fdif67_1[0])/(b67[1]-b67[0])
normnFdif67_1=nFdif67_1/(normb_67_1)
err_67_1=(normnFdif67_1*derr67_1/(nFdif67_1*normb_67_1))*(nFdif67_1**(2)+normb_67_1**(2))**(1/2)
err_67_1=(2**(1/2))*derr67_1*normnFdif67_1
#print err_67_1


nFdif69_1=(Fdif69_1[1:]-Fdif69_1[:-1])/(b69[1:]-b69[:-1])
normb_69_1=(Fdif69_1[1]-Fdif69_1[0])/(b69[1]-b69[0])
normnFdif69_1=nFdif69_1/(normb_69_1)
err_69_1=(2**(1/2))*derr69_1*normnFdif69_1

plt.errorbar(nraper,normnFdif67_1,err_67_1,color='grey')
plt.plot(nraper,normnFdif67_1,color='black')
plt.errorbar(nraper,normnFdif69_1,err_69_1,color='red')
plt.xlabel("$r_{aperture}$ ('')", fontsize='20')
plt.ylabel("Relative flux", fontsize='20')
plt.text(0.4,0.8,"MRK 1014", color='black', fontsize='20' )
plt.text(0.8,0.4,"$Scale=2.772$ kpc/''", color='black', fontsize='20' )

plt.figure()
plt.plot(nraper,normnFdif67_1,color='blue')
plt.plot(-nraper,normnFdif67_1,color='blue')
plt.plot(nraper,normnFdif69_1,'k--',color='blue')
plt.plot(-nraper,normnFdif69_1,'k--',color='blue')

plt.plot(nraper,normnFdif67_1-normnFdif69_1, color='green')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1, color='green')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.9, color='red')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.9, color='red')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.8, color='orange')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.8, color='orange')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.7, color='purple')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.7, color='purple')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.6, color='green')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.6, color='green')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.5, color='red')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.5, color='red')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.4, color='orange')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.4, color='orange')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.3, color='purple')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.3, color='purple')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.2, color='green')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.2, color='green')
plt.plot(nraper,normnFdif67_1-normnFdif69_1*0.1, color='red')
plt.plot(-nraper,normnFdif67_1-normnFdif69_1*0.1, color='red')
plt.xlabel("$r_{aperture}$ ('')")
plt.ylabel("Relative flux")
plt.text(1.5,0.8,"MRK 1014", color='black')

#Test K-S
S_test=ks_2samp(normnFdif69_1,normnFdif69_1)
comp_test=ks_2samp(normnFdif69_1,normnFdif67_1)
print S_test
print comp_test

#PSF_Scaling segun Mason et al.

anFdif69_1=Fdif69_1/7724.863
bnFdif69_1=anFdif69_1*Fdif67_1
#for x in range(0,195):
#  print raper[x], bnFdif69_1[x], anFdif69_1[x]

plt.show()
