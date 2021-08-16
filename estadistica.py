import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pylab
from scipy.stats import *

import boostrap_mm6 as par

#$$CALIBRADORES
test_MW = kruskal(par.sigma_qso,par.sigma_qso)
test_ks_2samp = ks_2samp(par.sigma_qso,par.sigma_qso)
print  '&&&&&&&&&&&&CALIBRADORES&&&&&&&&&&&&&&&&&&&&&&&'
print  'Test-KS2samp=',test_ks_2samp, 'Test/MW=',test_MW 

#$$%^^&^&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#$$TEST


test_ks2_par = ks_2samp(par.sigma_qso, par.sigma_Sy1)
#test_MW_par = mannwhitneyu(par.i_Sy1, par.i_NHBLR,use_continuity=True)
test_MW_par = kruskal(par.Pesc_qso, par.Pesc_Sy1)

z_stat_c, p_val_c = ranksums(par.Pesc_qso, par.Pesc_qso)
z_stat, p_val = ranksums(par.Pesc_qso, par.Pesc_Sy1)  
print  '&&&&&&&&&&&&Mann-Whitnny&&&&&&&&&&&&&&&&&&&&&&&'
print "MWW RankSum P CALIBRADOR =", p_val_c 
print "MWW RankSum P for treatments 1 and 2 =", p_val  

plt.figure('Cumulative')
plt.ylim(0,1)
#pylab.hist(par.f2_qso, 50, normed=1,cumulative='True',histtype='step',label='QSOs')
cumPDF_qso, bins_qso, patchest_qso = pylab.hist(par.sigma_qso, 50, normed=1,cumulative='True',histtype='step',label='QSOs')
cumPDF_Sy, bins_Sy, patchest_Sy = pylab.hist(par.sigma_Sy1, 50, normed=1,cumulative='True',histtype='step',label='Sy1')

#Distancias criticas
m_qso=2162.
n_Sy1=2503.
n_HBLR=2333.
n_NHBLR=2585.

Dcrit_qso_Sy_p80 = 1.07*np.sqrt((m_qso+n_Sy1)/(m_qso*n_Sy1))

Dcrit_qso_Sy_p99 = 1.63*np.sqrt((m_qso+n_Sy1)/(m_qso*n_Sy1))

print  '&&&&&&&&&&&&TESTS&&&&&&&&&&&&&&&&&&&&&&&'
print  'QSOs Vs Seyfert1 '
print  'Parametro '
print  'KS=', test_ks2_par, 'MW=', test_MW_par


print 'QSO-Sy1 = ', 1.63*np.sqrt((m_qso+n_Sy1)/(m_qso*n_Sy1))
print 'QSO-HBLR = ', 1.63*np.sqrt((m_qso+n_HBLR)/(m_qso*n_HBLR))
print 'QSO-NHBLR = ', 1.63*np.sqrt((m_qso+n_NHBLR)/(m_qso*n_NHBLR))

#Make plots
#plt.xlabel(r'$f_{2}$',fontsize=26)
#plt.xlabel(r'$P{esc} $',fontsize=26)
#plt.xlabel(r'$\sigma_{Torus} [deg] $',fontsize=26)
#plt.xlabel(r'$Y$',fontsize=26)
#plt.xlabel(r'$N_{0}  $',fontsize=26)
#plt.xlabel(r'$q$',fontsize=26)
#plt.xlabel(r'$\tau_{V}  $',fontsize=26)
#plt.xlabel(r'$i$',fontsize=26)
plt.xlabel(r'Parametro',fontsize=26)
plt.ylabel(r'Cumulative PDF',fontsize=26)

plt.legend(loc = 'best', numpoints=1, prop={'size':20})


print max(abs(cumPDF_Sy-cumPDF_qso))

plt.show()

plt.clf()
