import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pylab
from scipy.stats import *

import boostrap_mm6 as par

#$$CALIBRADORES
test_MW = kruskal(par.sigma_qso,par.sigma_qso)
test_ks_2samp = ks_2samp(par.sigma_qso,par.sigma_qso)
z_stat_c, p_val_c = ranksums(par.Pesc_qso, par.Pesc_qso)
print  '&&&&&&&&&&&&CALIBRADORES&&&&&&&&&&&&&&&&&&&&&&&'
print  'Test-KS2samp=',test_ks_2samp, 'Test-MW=',test_MW 
print "MWW RankSum P CALIBRADOR =", p_val_c 
#$$%^^&^&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#$$TEST

plt.figure('Cumulative')
plt.ylim(0,1)
cumPDF_qso, bins_qso, patchest_qso = pylab.hist(par.f2_qso, 2000, normed=1,cumulative='True',histtype='step',label='QSOs')
cumPDF_Sy, bins_Sy, patchest_Sy = pylab.hist(par.f2_HBLR, 2000, normed=1,cumulative='True',histtype='step',label='Sy1')

print bins_qso
print bins_Sy

print  '&&&&&&&&&&&&Mann-Whitnny&&&&&&&&&&&&&&&&&&&&&&&'

test_MW_par = kruskal(cumPDF_qso,cumPDF_Sy)
z_stat, p_val = ranksums(cumPDF_qso,cumPDF_Sy)  
u,pv = mannwhitneyu(cumPDF_qso,cumPDF_Sy)
print "MWW  =", test_MW_par,p_val  
print "MWW  =",u, pv
print  '&&&&&&&&&&&&Mann-Whitnny(Bins)&&&&&&&&&&&&&&&&&&&&&&&'
test_MW_par = kruskal(bins_qso,bins_Sy)
z_stat, p_val = ranksums(bins_qso,bins_Sy)  
u,pv = mannwhitneyu(bins_qso,bins_Sy)
print "MWW  =", test_MW_par,p_val  
print "MWW  =",u, pv


plt.show()

#plt.clf()
