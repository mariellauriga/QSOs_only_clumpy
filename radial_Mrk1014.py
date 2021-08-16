from scipy.stats import *
import matplotlib.pyplot as plt
import scipy as sci
from pylab import *
import numpy as np
import math

plt.subplots_adjust(hspace=0.3)
plt.subplots_adjust(wspace=0.05)


#raperG, FdifG =sci.loadtxt('FC_stck_Mrk1383_combined.1',unpack=True)
#TARGET
rsc_tg,a,bsctg,Fdifsc_tg,c1,c2,flag =loadtxt('FC_stck_combined_mrk1014.fits.mag.1',unpack=True)
#STANDARD
rsc_std,a,bscstd,Fdifsc_std,c1,c2,flag =loadtxt('FC_stck_S20130101S7303.fits.mag.1',unpack=True)

stdev = loadtxt('psf-scaling/stdev.dat',unpack=True)

rsc_tg_mi,a,bsctg_mi,Fdifsc_tg_mi,c1,c2,flag = loadtxt('psf-scaling_minus_sigma/FC_stck_combined_mrk1014.fits.mag.1',unpack=True)
rsc_std_mi,a,bscstd_mi,Fdifsc_std_mi,c1,c2,flag = loadtxt('psf-scaling_minus_sigma/FC_stck_S20130101S7303.fits.mag.1',unpack=True)

rsc_tg_pl,a,bsctg_pl,Fdifsc_tg_pl,c1,c2,flag = loadtxt('psf-scaling_plus_sigma/FC_stck_combined_mrk1014.fits.mag.1',unpack=True)
rsc_std_pl,a,bscstd_pl,Fdifsc_std_pl,c1,c2,flag = loadtxt('psf-scaling_plus_sigma/FC_stck_S20130101S7303.fits.mag.1',unpack=True)




#Sersic component
#r_ser,a,b_ser,F_ser,c1,c2,flag = loadtxt('galfit-method/model_v2.fits.mag.1', unpack=True)


#nF_ser=(F_ser[1:]-F_ser[:-1])/(b_ser[1:]-b_ser[:-1])
#normb_ser=(F_ser[1]-F_ser[0])/(b_ser[1]-b_ser[0])
#normnFser=nF_ser/(normb_ser)

#nr_ser=((r_ser[1:]+r_ser[:-1])/2)*0.08

#Radial profile

plt.ylim(0,1.0)
nraper=((rsc_std[1:]+rsc_std[:-1])/2)*0.08


nFdifsc_tg=(Fdifsc_tg[1:]-Fdifsc_tg[:-1])/(bsctg[1:]-bsctg[:-1])
normb_sc_tg=(Fdifsc_tg[1]-Fdifsc_tg[0])/(bsctg[1]-bsctg[0])
normnFdifsc_tg=nFdifsc_tg/(normb_sc_tg)

nFdifsc_std=(Fdifsc_std[1:]-Fdifsc_std[:-1])/(bscstd[1:]-bscstd[:-1])
normb_sc_std=(Fdifsc_std[1]-Fdifsc_std[0])/(bscstd[1]-bscstd[0])
normnFdifsc_std=nFdifsc_std/(normb_sc_std)

#Incertidumbres
##%%%%%En el target%%%%%
##%%%%%%sky-sigma%%%%%%
bg_noise_sc_tg_mi=stdev
sky_transp_sc_tg_mi=Fdifsc_tg*0.06
flux_calib_sc_tg_mi=Fdifsc_tg*0.1
psf_var_mi=Fdifsc_tg*0.13
Fdifsc_tg_mi = (Fdifsc_tg - bg_noise_sc_tg_mi) - sky_transp_sc_tg_mi - flux_calib_sc_tg_mi - psf_var_mi

nFdifsc_tg_mi = (Fdifsc_tg_mi[1:]-Fdifsc_tg_mi[:-1])/(bsctg_mi[1:]-bsctg_mi[:-1])
normb_sc_tg_mi = (Fdifsc_tg_mi[1]-Fdifsc_tg_mi[0])/(bsctg_mi[1]-bsctg_mi[0])
normnFdifsc_tg_mi = nFdifsc_tg_mi/(normb_sc_tg_mi)


##%%%%%%sky+sigma%%%%%%
bg_noise_sc_tg_pl=stdev
sky_transp_sc_tg_pl=Fdifsc_tg*0.06
flux_calib_sc_tg_pl=Fdifsc_tg*0.1
psf_var_pl=Fdifsc_tg*0.13
Fdifsc_tg_pl = Fdifsc_tg + bg_noise_sc_tg_pl + sky_transp_sc_tg_pl + flux_calib_sc_tg_pl + psf_var_pl
nFdifsc_tg_pl=(Fdifsc_tg_pl[1:]-Fdifsc_tg_pl[:-1])/(bsctg_pl[1:]-bsctg_pl[:-1])
normb_sc_tg_pl=(Fdifsc_tg_pl[1]-Fdifsc_tg_pl[0])/(bsctg_pl[1]-bsctg_pl[0])
normnFdifsc_tg_pl=nFdifsc_tg_pl/(normb_sc_tg_pl)



##%%%%%En la STD%%%%%
##%%%%%%sky-sigma%%%%%%
bg_noise_sc_std_mi=Fdifsc_std_mi
sky_transp_sc_std_mi=Fdifsc_std_mi*0.06
flux_calib_sc_std_mi=Fdifsc_std_mi*0.1
Fdifsc_std_mi = bg_noise_sc_std_mi + sky_transp_sc_std_mi + flux_calib_sc_std_mi
nFdifsc_std_mi=(Fdifsc_std_mi[1:]-Fdifsc_std_mi[:-1])/(bscstd_mi[1:]-bscstd_mi[:-1])
normb_sc_std_mi=(Fdifsc_std_mi[1]-Fdifsc_std_mi[0])/(bscstd_mi[1]-bscstd_mi[0])
normnFdifsc_std_mi=nFdifsc_std_mi/(normb_sc_std_mi)
##%%%%%%sky+sigma%%%%%%
bg_noise_sc_std_pl=Fdifsc_std_pl
sky_transp_sc_std_pl=Fdifsc_std_pl*0.06
flux_calib_sc_std_pl=Fdifsc_std_pl*0.1
Fdifsc_std_pl =bg_noise_sc_std_pl + sky_transp_sc_std_pl + flux_calib_sc_std_pl
nFdifsc_std_pl=(Fdifsc_std_pl[1:]-Fdifsc_std_pl[:-1])/(bscstd_pl[1:]-bscstd_pl[:-1])
normb_sc_std_pl=(Fdifsc_std_pl[1]-Fdifsc_std_pl[0])/(bscstd_pl[1]-bscstd_pl[0])
normnFdifsc_std_pl=nFdifsc_std_pl/(normb_sc_std_pl)

plt.plot(nraper,normnFdifsc_tg,color='black', linewidth=1.5, label='PG 0157+002')
plt.fill_between(nraper,normnFdifsc_tg_mi,normnFdifsc_tg,color='grey')
plt.fill_between(nraper,normnFdifsc_tg_pl,normnFdifsc_tg,color='grey')

#plt.plot(nr_ser,normnFser, 'b--',linewidth=1.5, label='GALFIT model')


plt.plot(nraper,normnFdifsc_std,'k--',color='red',linewidth=1.5, label='PSF-star')
plt.fill_between(nraper,normnFdifsc_std_mi,normnFdifsc_std,color='pink')
plt.fill_between(nraper,normnFdifsc_std_pl,normnFdifsc_std,color='pink')



plt.legend(loc = 'best', numpoints=1)
plt.xlim(0,1.2)

tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)



plt.xlabel("$r_{aperture}$ ('')",fontsize='26')
plt.ylabel("Relative flux",fontsize='20')
#plt.text(0.5,0.7,"MRK 478", color='black',fontsize='18')





plt.show()


