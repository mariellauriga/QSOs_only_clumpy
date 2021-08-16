import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pylab
from scipy.stats import *
from scipy.special import erf
import QSOs_samp_sig as qso_sig
import QSOs_samp_f2 as qso_f2
import QSOs_samp_i as qso_i
import QSOs_samp_No as qso_No
import QSOs_samp_Pesc as qso_Pesc
import QSOs_samp_q as qso_q
import QSOs_samp_TauV as qso_TauV
import QSOs_samp_Y as qso_Y
import Seyfert1_samp_sig as Sy1_sig
import Seyfert1_samp_f2 as Sy1_f2
import Seyfert1_samp_i as Sy1_i
import Seyfert1_samp_No as Sy1_No
import Seyfert1_samp_Pesc as Sy1_Pesc
import Seyfert1_samp_q as Sy1_q
import Seyfert1_samp_TauV as Sy1_TauV
import Seyfert1_samp_Y as Sy1_Y

import HBLR_samp_sig as HBLR_sig
import HBLR_samp_f2 as HBLR_f2
import HBLR_samp_i as HBLR_i
import HBLR_samp_No as HBLR_No
import HBLR_samp_Pesc as HBLR_Pesc
import HBLR_samp_q as HBLR_q
import HBLR_samp_TauV as HBLR_TauV
import HBLR_samp_Y as HBLR_Y

import NHBLR_samp_sig as NHBLR_sig
import NHBLR_samp_f2 as NHBLR_f2
import NHBLR_samp_i as NHBLR_i
import NHBLR_samp_No as NHBLR_No
import NHBLR_samp_Pesc as NHBLR_Pesc
import NHBLR_samp_q as NHBLR_q
import NHBLR_samp_TauV as NHBLR_TauV
import NHBLR_samp_Y as NHBLR_Y


import boostrap as bs

#Sigma
sigma_qso = np.concatenate([qso_sig.samp_1, qso_sig.samp_2, qso_sig.samp_3, qso_sig.samp_4, qso_sig.samp_5, qso_sig.samp_6, qso_sig.samp_7, qso_sig.samp_8, qso_sig.samp_9, qso_sig.samp_10, qso_sig.samp_11,qso_sig.samp_12,qso_sig.samp_13,qso_sig.samp_14,qso_sig.samp_15,qso_sig.samp_16,qso_sig.samp_17,qso_sig.samp_18,qso_sig.samp_19])
sigma_Sy1 = np.concatenate([Sy1_sig.samp_1, Sy1_sig.samp_2, Sy1_sig.samp_3, Sy1_sig.samp_4, Sy1_sig.samp_5])
sigma_HBLR = np.concatenate([HBLR_sig.samp_1, HBLR_sig.samp_2, HBLR_sig.samp_3, HBLR_sig.samp_4, HBLR_sig.samp_5, HBLR_sig.samp_6, HBLR_sig.samp_7, HBLR_sig.samp_8, HBLR_sig.samp_9])
sigma_NHBLR = np.concatenate([NHBLR_sig.samp_1, NHBLR_sig.samp_2, NHBLR_sig.samp_3, NHBLR_sig.samp_4, NHBLR_sig.samp_5, NHBLR_sig.samp_6])
#Y
Y_qso = np.concatenate([qso_Y.samp_1, qso_Y.samp_2, qso_Y.samp_3, qso_Y.samp_4, qso_Y.samp_5, qso_Y.samp_6, qso_Y.samp_7, qso_Y.samp_8, qso_Y.samp_9, qso_Y.samp_10, qso_Y.samp_11,qso_Y.samp_12,qso_Y.samp_13,qso_Y.samp_14,qso_Y.samp_15,qso_Y.samp_16,qso_Y.samp_17,qso_Y.samp_18,qso_Y.samp_19])
Y_Sy1 = np.concatenate([Sy1_Y.samp_1, Sy1_Y.samp_2, Sy1_Y.samp_3, Sy1_Y.samp_4, Sy1_Y.samp_5])
Y_HBLR = np.concatenate([HBLR_Y.samp_1, HBLR_Y.samp_2, HBLR_Y.samp_3, HBLR_Y.samp_4, HBLR_Y.samp_5, HBLR_Y.samp_6, HBLR_Y.samp_7, HBLR_Y.samp_8, HBLR_Y.samp_9])
Y_NHBLR = np.concatenate([NHBLR_Y.samp_1, NHBLR_Y.samp_2, NHBLR_Y.samp_3, NHBLR_Y.samp_4, NHBLR_Y.samp_5, NHBLR_Y.samp_6])
#No
No_qso = np.concatenate([qso_No.samp_1, qso_No.samp_2, qso_No.samp_3, qso_No.samp_4, qso_No.samp_5, qso_No.samp_6, qso_No.samp_7, qso_No.samp_8, qso_No.samp_9, qso_No.samp_10, qso_No.samp_11,qso_No.samp_12,qso_No.samp_13,qso_No.samp_14,qso_No.samp_15,qso_No.samp_16,qso_No.samp_17,qso_No.samp_18,qso_No.samp_19])
No_Sy1 = np.concatenate([Sy1_No.samp_1, Sy1_No.samp_2, Sy1_No.samp_3, Sy1_No.samp_4, Sy1_No.samp_5])
No_HBLR = np.concatenate([HBLR_No.samp_1, HBLR_No.samp_2, HBLR_No.samp_3, HBLR_No.samp_4, HBLR_No.samp_5, HBLR_No.samp_6, HBLR_No.samp_7, HBLR_No.samp_8, HBLR_No.samp_9])
No_NHBLR = np.concatenate([NHBLR_No.samp_1, NHBLR_No.samp_2, NHBLR_No.samp_3, NHBLR_No.samp_4, NHBLR_No.samp_5, NHBLR_No.samp_6])
#q
q_qso = np.concatenate([qso_q.samp_1, qso_q.samp_2, qso_q.samp_3, qso_q.samp_4, qso_q.samp_5, qso_q.samp_6, qso_q.samp_7, qso_q.samp_8, qso_q.samp_9, qso_q.samp_10, qso_q.samp_11,qso_q.samp_12,qso_q.samp_13,qso_q.samp_14,qso_q.samp_15,qso_q.samp_16,qso_q.samp_17,qso_q.samp_18,qso_q.samp_19])
q_Sy1 = np.concatenate([Sy1_q.samp_1, Sy1_q.samp_2, Sy1_q.samp_3, Sy1_q.samp_4, Sy1_q.samp_5])
q_HBLR = np.concatenate([HBLR_q.samp_1, HBLR_q.samp_2, HBLR_q.samp_3, HBLR_q.samp_4, HBLR_q.samp_5, HBLR_q.samp_6, HBLR_q.samp_7, HBLR_q.samp_8, HBLR_q.samp_9])
q_NHBLR = np.concatenate([NHBLR_q.samp_1, NHBLR_q.samp_2, NHBLR_q.samp_3, NHBLR_q.samp_4, NHBLR_q.samp_5, NHBLR_q.samp_6])

#TauV
TauV_qso = np.concatenate([qso_TauV.samp_1, qso_TauV.samp_2, qso_TauV.samp_3, qso_TauV.samp_4, qso_TauV.samp_5, qso_TauV.samp_6, qso_TauV.samp_7, qso_TauV.samp_8, qso_TauV.samp_9, qso_TauV.samp_10, qso_TauV.samp_11,qso_TauV.samp_12,qso_TauV.samp_13,qso_TauV.samp_14,qso_TauV.samp_15,qso_TauV.samp_16,qso_TauV.samp_17,qso_TauV.samp_18,qso_TauV.samp_19])
TauV_Sy1 = np.concatenate([Sy1_TauV.samp_1, Sy1_TauV.samp_2, Sy1_TauV.samp_3, Sy1_TauV.samp_4, Sy1_TauV.samp_5])
TauV_HBLR = np.concatenate([HBLR_TauV.samp_1, HBLR_TauV.samp_2, HBLR_TauV.samp_3, HBLR_TauV.samp_4, HBLR_TauV.samp_5, HBLR_TauV.samp_6, HBLR_TauV.samp_7, HBLR_TauV.samp_8, HBLR_TauV.samp_9])
TauV_NHBLR = np.concatenate([NHBLR_TauV.samp_1, NHBLR_TauV.samp_2, NHBLR_TauV.samp_3, NHBLR_TauV.samp_4, NHBLR_TauV.samp_5, NHBLR_TauV.samp_6])

#i
i_qso = np.concatenate([qso_i.samp_1, qso_i.samp_2, qso_i.samp_3, qso_i.samp_4, qso_i.samp_5, qso_i.samp_6, qso_i.samp_7, qso_i.samp_8, qso_i.samp_9, qso_i.samp_10, qso_i.samp_11,qso_i.samp_12,qso_i.samp_13,qso_i.samp_14,qso_i.samp_15,qso_i.samp_16,qso_i.samp_17,qso_i.samp_18,qso_i.samp_19])
i_Sy1 = np.concatenate([Sy1_i.samp_1, Sy1_i.samp_2, Sy1_i.samp_3, Sy1_i.samp_4, Sy1_i.samp_5])
i_HBLR = np.concatenate([HBLR_i.samp_1, HBLR_i.samp_2, HBLR_i.samp_3, HBLR_i.samp_4, HBLR_i.samp_5, HBLR_i.samp_6, HBLR_i.samp_7, HBLR_i.samp_8, HBLR_i.samp_9])
i_NHBLR = np.concatenate([NHBLR_i.samp_1, NHBLR_i.samp_2, NHBLR_i.samp_3, NHBLR_i.samp_4, NHBLR_i.samp_5, NHBLR_i.samp_6])

#f2
f2_qso = np.concatenate([qso_f2.samp_1, qso_f2.samp_2, qso_f2.samp_3, qso_f2.samp_4, qso_f2.samp_5, qso_f2.samp_6, qso_f2.samp_7, qso_f2.samp_8, qso_f2.samp_9, qso_f2.samp_10, qso_f2.samp_11,qso_f2.samp_12,qso_f2.samp_13,qso_f2.samp_14,qso_f2.samp_15,qso_f2.samp_16,qso_f2.samp_17,qso_f2.samp_18,qso_f2.samp_19])
f2_Sy1 = np.concatenate([Sy1_f2.samp_1, Sy1_f2.samp_2, Sy1_f2.samp_3, Sy1_f2.samp_4, Sy1_f2.samp_5])
f2_HBLR = np.concatenate([HBLR_f2.samp_1, HBLR_f2.samp_2, HBLR_f2.samp_3, HBLR_f2.samp_4, HBLR_f2.samp_5, HBLR_f2.samp_6, HBLR_f2.samp_7, HBLR_f2.samp_8, HBLR_f2.samp_9])
f2_NHBLR = np.concatenate([NHBLR_f2.samp_1, NHBLR_f2.samp_2, NHBLR_f2.samp_3, NHBLR_f2.samp_4, NHBLR_f2.samp_5, NHBLR_f2.samp_6])

#Pesc
Pesc_qso = np.concatenate([qso_Pesc.samp_1, qso_Pesc.samp_2, qso_Pesc.samp_3, qso_Pesc.samp_4, qso_Pesc.samp_5, qso_Pesc.samp_6, qso_Pesc.samp_7, qso_Pesc.samp_8, qso_Pesc.samp_9, qso_Pesc.samp_10, qso_Pesc.samp_11,qso_Pesc.samp_12,qso_Pesc.samp_13,qso_Pesc.samp_14,qso_Pesc.samp_15,qso_Pesc.samp_16,qso_Pesc.samp_17,qso_Pesc.samp_18,qso_Pesc.samp_19])
Pesc_Sy1 = np.concatenate([Sy1_Pesc.samp_1, Sy1_Pesc.samp_2, Sy1_Pesc.samp_3, Sy1_Pesc.samp_4, Sy1_Pesc.samp_5])
Pesc_HBLR = np.concatenate([HBLR_Pesc.samp_1, HBLR_Pesc.samp_2, HBLR_Pesc.samp_3, HBLR_Pesc.samp_4, HBLR_Pesc.samp_5, HBLR_Pesc.samp_6, HBLR_Pesc.samp_7, HBLR_Pesc.samp_8, HBLR_Pesc.samp_9])
Pesc_NHBLR = np.concatenate([NHBLR_Pesc.samp_1, NHBLR_Pesc.samp_2, NHBLR_Pesc.samp_3, NHBLR_Pesc.samp_4, NHBLR_Pesc.samp_5, NHBLR_Pesc.samp_6])

# find mean 95% CI and 100,000 bootstrap samples
low_sig_qso, high_sig_qso = bs.bootstrap(2162,sigma_qso, 10000, np.mean, 0.05)
low_sig_Sy1, high_sig_Sy1 = bs.bootstrap(2503,sigma_Sy1, 10000, np.mean, 0.05)
low_sig_HBLR, high_sig_HBLR = bs.bootstrap(2333,sigma_HBLR, 10000, np.mean, 0.05)
low_sig_NHBL, high_sig_NHBL = bs.bootstrap(2585,sigma_NHBLR, 10000, np.mean, 0.05)

low_Y_qso, high_Y_qso = bs.bootstrap(2162,Y_qso, 10000, np.mean, 0.05)
low_Y_Sy1, high_Y_Sy1 = bs.bootstrap(2503,Y_Sy1, 10000, np.mean, 0.05)
low_Y_HBLR, high_Y_HBLR = bs.bootstrap(2333,Y_HBLR, 10000, np.mean, 0.05)
low_Y_NHBL, high_Y_NHBL = bs.bootstrap(2585,Y_NHBLR, 10000, np.mean, 0.05)

low_q_qso, high_q_qso = bs.bootstrap(2162,q_qso, 10000, np.mean, 0.05)
low_q_Sy1, high_q_Sy1 = bs.bootstrap(2503,q_Sy1, 10000, np.mean, 0.05)
low_q_HBLR, high_q_HBLR = bs.bootstrap(2333,q_HBLR, 10000, np.mean, 0.05)
low_q_NHBL, high_q_NHBL = bs.bootstrap(2585,q_NHBLR, 10000, np.mean, 0.05)

low_No_qso, high_No_qso = bs.bootstrap(2162,No_qso, 10000, np.mean, 0.05)
low_No_Sy1, high_No_Sy1 = bs.bootstrap(2503,No_Sy1, 10000, np.mean, 0.05)
low_No_HBLR, high_No_HBLR = bs.bootstrap(2333,No_HBLR, 10000, np.mean, 0.05)
low_No_NHBL, high_No_NHBL = bs.bootstrap(2585,No_NHBLR, 10000, np.mean, 0.05)

low_TauV_qso, high_TauV_qso = bs.bootstrap(2162,TauV_qso, 10000, np.mean, 0.05)
low_TauV_Sy1, high_TauV_Sy1 = bs.bootstrap(2503,TauV_Sy1, 10000, np.mean, 0.05)
low_TauV_HBLR, high_TauV_HBLR = bs.bootstrap(2333,TauV_HBLR, 10000, np.mean, 0.05)
low_TauV_NHBL, high_TauV_NHBL = bs.bootstrap(2585,TauV_NHBLR, 10000, np.mean, 0.05)

low_i_qso, high_i_qso = bs.bootstrap(2162,i_qso, 10000, np.mean, 0.05)
low_i_Sy1, high_i_Sy1 = bs.bootstrap(2503,i_Sy1, 10000, np.mean, 0.05)
low_i_HBLR, high_i_HBLR = bs.bootstrap(2333,i_HBLR, 10000, np.mean, 0.05)
low_i_NHBL, high_i_NHBL = bs.bootstrap(2585,i_NHBLR, 10000, np.mean, 0.05)

low_f2_qso, high_f2_qso = bs.bootstrap(2162,f2_qso, 10000, np.mean, 0.05)
low_f2_Sy1, high_f2_Sy1 = bs.bootstrap(2503,f2_Sy1, 10000, np.mean, 0.05)
low_f2_HBLR, high_f2_HBLR = bs.bootstrap(2333,f2_HBLR, 10000, np.mean, 0.05)
low_f2_NHBL, high_f2_NHBL = bs.bootstrap(2585,f2_NHBLR, 10000, np.mean, 0.05)

low_Pesc_qso, high_Pesc_qso = bs.bootstrap(2162,Pesc_qso, 10000, np.mean, 0.05)
low_Pesc_Sy1, high_Pesc_Sy1 = bs.bootstrap(2503,Pesc_Sy1, 10000, np.mean, 0.05)
low_Pesc_HBLR, high_Pesc_HBLR = bs.bootstrap(2333,Pesc_HBLR, 10000, np.mean, 0.05)
low_Pesc_NHBL, high_Pesc_NHBL = bs.bootstrap(2585,Pesc_NHBLR, 10000, np.mean, 0.05)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# make plots
y=(0,1)
#%%%%%%%%Sigma
perc_qso_sigma = np.percentile(sigma_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_sigma =(perc_qso_sigma[1]-perc_qso_sigma[0], perc_qso_sigma[1]-perc_qso_sigma[0])
xh_qso_sigma =(perc_qso_sigma[2]-perc_qso_sigma[1], perc_qso_sigma[2]-perc_qso_sigma[1]) 
xm_qso_sigma =(perc_qso_sigma[1],perc_qso_sigma[1]) 


perc_Sy1_sigma = np.percentile(sigma_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_sigma =(perc_Sy1_sigma[1], perc_Sy1_sigma[1]) 
xl_Sy1_sigma =(perc_Sy1_sigma[1]-perc_Sy1_sigma[0],perc_Sy1_sigma[1]-perc_Sy1_sigma[0]) 
xh_Sy1_sigma =(perc_Sy1_sigma[2]-perc_Sy1_sigma[1],perc_Sy1_sigma[2]-perc_Sy1_sigma[1]) 


perc_HBLR_sigma = np.percentile(sigma_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_sigma =(perc_HBLR_sigma[1],perc_HBLR_sigma[1]) 
xl_HBLR_sigma = (perc_HBLR_sigma[1]-perc_HBLR_sigma[0],perc_HBLR_sigma[1]-perc_HBLR_sigma[0])
xh_HBLR_sigma =(perc_HBLR_sigma[2]-perc_HBLR_sigma[1],perc_HBLR_sigma[2]-perc_HBLR_sigma[1]) 

perc_NHBLR_sigma = np.percentile(sigma_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_sigma =(perc_NHBLR_sigma[1],perc_NHBLR_sigma[1]) 
xl_NHBLR_sigma =(perc_NHBLR_sigma[1]-perc_NHBLR_sigma[0],perc_NHBLR_sigma[1]-perc_NHBLR_sigma[0]) 
xh_NHBLR_sigma =(perc_NHBLR_sigma[2]-perc_NHBLR_sigma[1],perc_NHBLR_sigma[2]-perc_NHBLR_sigma[1]) 

#%%%%%%%%%%%%%Y

perc_qso_Y = np.percentile(Y_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_Y =(perc_qso_Y[1]-perc_qso_Y[0],perc_qso_Y[1]-perc_qso_Y[0]) 
xh_qso_Y =(perc_qso_Y[2]-perc_qso_Y[1],perc_qso_Y[2]-perc_qso_Y[1]) 
xm_qso_Y =(perc_qso_Y[1],perc_qso_Y[1]) 

perc_Sy1_Y = np.percentile(Y_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_Y =(perc_Sy1_Y[1],perc_Sy1_Y[1]) 
xl_Sy1_Y =(perc_Sy1_Y[1]-perc_Sy1_Y[0],perc_Sy1_Y[1]-perc_Sy1_Y[0]) 
xh_Sy1_Y =(perc_Sy1_Y[2]-perc_Sy1_Y[1],perc_Sy1_Y[2]-perc_Sy1_Y[1]) 

perc_HBLR_Y = np.percentile(Y_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_Y =(perc_HBLR_Y[1],perc_HBLR_Y[1]) 
xl_HBLR_Y = (perc_HBLR_Y[1]-perc_HBLR_Y[0],perc_HBLR_Y[1]-perc_HBLR_Y[0])
xh_HBLR_Y = (perc_HBLR_Y[2]-perc_HBLR_Y[1],perc_HBLR_Y[2]-perc_HBLR_Y[1])

perc_NHBLR_Y = np.percentile(Y_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_Y =(perc_NHBLR_Y[1],perc_NHBLR_Y[1]) 
xl_NHBLR_Y = (perc_NHBLR_Y[1]-perc_NHBLR_Y[0],perc_NHBLR_Y[1]-perc_NHBLR_Y[0])
xh_NHBLR_Y = (perc_NHBLR_Y[2]-perc_NHBLR_Y[1],perc_NHBLR_Y[2]-perc_NHBLR_Y[1])

#%%%%%%%%%%%q

perc_qso_q = np.percentile(q_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_q =(perc_qso_q[1]-perc_qso_q[0],perc_qso_q[1]-perc_qso_q[0]) 
xh_qso_q =(perc_qso_q[2]-perc_qso_q[1],perc_qso_q[2]-perc_qso_q[1]) 
xm_qso_q =(perc_qso_q[1],perc_qso_q[1]) 

perc_Sy1_q = np.percentile(q_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_q =(perc_Sy1_q[1],perc_Sy1_q[1]) 
xl_Sy1_q = (perc_Sy1_q[1]-perc_Sy1_q[0],perc_Sy1_q[1]-perc_Sy1_q[0])
xh_Sy1_q = (perc_Sy1_q[2]-perc_Sy1_q[1],perc_Sy1_q[2]-perc_Sy1_q[1])

perc_HBLR_q = np.percentile(q_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_q = (perc_HBLR_q[1],perc_HBLR_q[1])
xl_HBLR_q = (perc_HBLR_q[1]-perc_HBLR_q[0],perc_HBLR_q[1]-perc_HBLR_q[0])
xh_HBLR_q = (perc_HBLR_q[2]-perc_HBLR_q[1],perc_HBLR_q[2]-perc_HBLR_q[1])

perc_NHBLR_q = np.percentile(q_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_q = (perc_NHBLR_q[1],perc_NHBLR_q[1])
xl_NHBLR_q = (perc_NHBLR_q[1]-perc_NHBLR_q[0],perc_NHBLR_q[1]-perc_NHBLR_q[0])
xh_NHBLR_q = (perc_NHBLR_q[2]-perc_NHBLR_q[1],perc_NHBLR_q[2]-perc_NHBLR_q[1])

#%%%%%%%%%%%%%%%TauV
perc_qso_TauV = np.percentile(TauV_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_TauV = (perc_qso_TauV[1]-perc_qso_TauV[0],perc_qso_TauV[1]-perc_qso_TauV[0])
xh_qso_TauV = (perc_qso_TauV[2]-perc_qso_TauV[1],perc_qso_TauV[2]-perc_qso_TauV[1])
xm_qso_TauV = (perc_qso_TauV[1],perc_qso_TauV[1])

perc_Sy1_TauV = np.percentile(TauV_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_TauV = (perc_Sy1_TauV[1],perc_Sy1_TauV[1]) 
xl_Sy1_TauV = (perc_Sy1_TauV[1]-perc_Sy1_TauV[0],perc_Sy1_TauV[1]-perc_Sy1_TauV[0])
xh_Sy1_TauV = (perc_Sy1_TauV[2]-perc_Sy1_TauV[1],perc_Sy1_TauV[2]-perc_Sy1_TauV[1])

perc_HBLR_TauV = np.percentile(TauV_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_TauV = (perc_HBLR_TauV[1],perc_HBLR_TauV[1])
xl_HBLR_TauV = (perc_HBLR_TauV[1]-perc_HBLR_TauV[0],perc_HBLR_TauV[1]-perc_HBLR_TauV[0])
xh_HBLR_TauV =  (perc_HBLR_TauV[2]-perc_HBLR_TauV[1],perc_HBLR_TauV[2]-perc_HBLR_TauV[1])

perc_NHBLR_TauV = np.percentile(TauV_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_TauV = (perc_NHBLR_TauV[1],perc_NHBLR_TauV[1])
xl_NHBLR_TauV = (perc_NHBLR_TauV[1]-perc_NHBLR_TauV[0],perc_NHBLR_TauV[1]-perc_NHBLR_TauV[0])
xh_NHBLR_TauV = (perc_NHBLR_TauV[2]-perc_NHBLR_TauV[1],perc_NHBLR_TauV[2]-perc_NHBLR_TauV[1])

#%%%%%%%%%%%%%%No
perc_qso_No = np.percentile(No_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_No = (perc_qso_No[1]-perc_qso_No[0],perc_qso_No[1]-perc_qso_No[0])
xh_qso_No = (perc_qso_No[2]-perc_qso_No[1],perc_qso_No[2]-perc_qso_No[1])
xm_qso_No = (perc_qso_No[1],perc_qso_No[1])

perc_Sy1_No = np.percentile(No_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_No =(perc_Sy1_No[1],perc_Sy1_No[1]) 
xl_Sy1_No = (perc_Sy1_No[1]-perc_Sy1_No[0],perc_Sy1_No[1]-perc_Sy1_No[0])
xh_Sy1_No = (perc_Sy1_No[2]-perc_Sy1_No[1],perc_Sy1_No[2]-perc_Sy1_No[1])

perc_HBLR_No = np.percentile(No_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_No = (perc_HBLR_No[1],perc_HBLR_No[1])
xl_HBLR_No = (perc_HBLR_No[1]-perc_HBLR_No[0],perc_HBLR_No[1]-perc_HBLR_No[0])
xh_HBLR_No = (perc_HBLR_No[2]-perc_HBLR_No[1],perc_HBLR_No[2]-perc_HBLR_No[1])

perc_NHBLR_No = np.percentile(No_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_No = (perc_NHBLR_No[1],perc_NHBLR_No[1]) 
xl_NHBLR_No = (perc_NHBLR_No[1]-perc_NHBLR_No[0],perc_NHBLR_No[1]-perc_NHBLR_No[0])
xh_NHBLR_No = (perc_NHBLR_No[2]-perc_NHBLR_No[1],perc_NHBLR_No[2]-perc_NHBLR_No[1])

#%%%%%%%%%%%%%%%i
perc_qso_i = np.percentile(i_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_i = (perc_qso_i[1]-perc_qso_i[0],perc_qso_i[1]-perc_qso_i[0])
xh_qso_i = (perc_qso_i[2]-perc_qso_i[1],perc_qso_i[2]-perc_qso_i[1])
xm_qso_i = (perc_qso_i[1],perc_qso_i[1])

perc_Sy1_i = np.percentile(i_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_i = (perc_Sy1_i[1],perc_Sy1_i[1])
xl_Sy1_i = (perc_Sy1_i[1]-perc_Sy1_i[0],perc_Sy1_i[1]-perc_Sy1_i[0])
xh_Sy1_i = (perc_Sy1_i[2]-perc_Sy1_i[1],perc_Sy1_i[2]-perc_Sy1_i[1])

perc_HBLR_i = np.percentile(i_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_i = (perc_HBLR_i[1],perc_HBLR_i[1])
xl_HBLR_i = (perc_HBLR_i[1]-perc_HBLR_i[0],perc_HBLR_i[1]-perc_HBLR_i[0])
xh_HBLR_i = (perc_HBLR_i[2]-perc_HBLR_i[1],perc_HBLR_i[2]-perc_HBLR_i[1])

perc_NHBLR_i = np.percentile(i_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_i = (perc_NHBLR_i[1],perc_NHBLR_i[1])
xl_NHBLR_i = (perc_NHBLR_i[1]-perc_NHBLR_i[0],perc_NHBLR_i[1]-perc_NHBLR_i[0])
xh_NHBLR_i = (perc_NHBLR_i[2]-perc_NHBLR_i[1],perc_NHBLR_i[2]-perc_NHBLR_i[1])

#%%%%%f2

perc_qso_f2 = np.percentile(f2_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_f2 = (perc_qso_f2[1]-perc_qso_f2[0],perc_qso_f2[1]-perc_qso_f2[0])
xh_qso_f2 = (perc_qso_f2[2]-perc_qso_f2[1],perc_qso_f2[2]-perc_qso_f2[1])
xm_qso_f2 = (perc_qso_f2[1],perc_qso_f2[1])

perc_Sy1_f2 = np.percentile(f2_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_f2 = (perc_Sy1_f2[1],perc_Sy1_f2[1])
xl_Sy1_f2 = (perc_Sy1_f2[1]-perc_Sy1_f2[0],perc_Sy1_f2[1]-perc_Sy1_f2[0])
xh_Sy1_f2 = (perc_Sy1_f2[2]-perc_Sy1_f2[1],perc_Sy1_f2[2]-perc_Sy1_f2[1])

perc_HBLR_f2 = np.percentile(f2_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_f2 = (perc_HBLR_f2[1],perc_HBLR_f2[1])
xl_HBLR_f2 = (perc_HBLR_f2[1]-perc_HBLR_f2[0],perc_HBLR_f2[1]-perc_HBLR_f2[0])
xh_HBLR_f2 = (perc_HBLR_f2[2]-perc_HBLR_f2[1],perc_HBLR_f2[2]-perc_HBLR_f2[1])

perc_NHBLR_f2 = np.percentile(f2_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_f2 = (perc_NHBLR_f2[1],perc_NHBLR_f2[1])
xl_NHBLR_f2 = (perc_NHBLR_f2[1]-perc_NHBLR_f2[0],perc_NHBLR_f2[1]-perc_NHBLR_f2[0])
xh_NHBLR_f2 = (perc_NHBLR_f2[2]-perc_NHBLR_f2[1],perc_NHBLR_f2[2]-perc_NHBLR_f2[1])

#%%%%%%%%%%%Pesc

perc_qso_Pesc = np.percentile(Pesc_qso, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xl_qso_Pesc = (perc_qso_Pesc[1]-perc_qso_Pesc[0],perc_qso_Pesc[1]-perc_qso_Pesc[0])
xh_qso_Pesc = (perc_qso_Pesc[2]-perc_qso_Pesc[1],perc_qso_Pesc[2]-perc_qso_Pesc[1])
xm_qso_Pesc = (perc_qso_Pesc[1],perc_qso_Pesc[1])

perc_Sy1_Pesc = np.percentile(Pesc_Sy1, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_Sy1_Pesc = (perc_Sy1_Pesc[1],perc_Sy1_Pesc[1])
xl_Sy1_Pesc = (perc_Sy1_Pesc[1]-perc_Sy1_Pesc[0],perc_Sy1_Pesc[1]-perc_Sy1_Pesc[0])
xh_Sy1_Pesc = (perc_Sy1_Pesc[2]-perc_Sy1_Pesc[1],perc_Sy1_Pesc[2]-perc_Sy1_Pesc[1])

perc_HBLR_Pesc = np.percentile(Pesc_HBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_HBLR_Pesc = (perc_HBLR_Pesc[1],perc_HBLR_Pesc[1])
xl_HBLR_Pesc = (perc_HBLR_Pesc[1]-perc_HBLR_Pesc[0],perc_HBLR_Pesc[1]-perc_HBLR_Pesc[0])
xh_HBLR_Pesc = (perc_HBLR_Pesc[2]-perc_HBLR_Pesc[1],perc_HBLR_Pesc[2]-perc_HBLR_Pesc[1])

perc_NHBLR_Pesc = np.percentile(Pesc_NHBLR, [50. - 50.*erf(1./np.sqrt(2.)), 50., 50. + 50.*erf(1./np.sqrt(2.))])
xm_NHBLR_Pesc = (perc_NHBLR_Pesc[1],perc_NHBLR_Pesc[1])
xl_NHBLR_Pesc = (perc_NHBLR_Pesc[1]-perc_NHBLR_Pesc[0],perc_NHBLR_Pesc[1]-perc_NHBLR_Pesc[0])
xh_NHBLR_Pesc = (perc_NHBLR_Pesc[2]-perc_NHBLR_Pesc[1],perc_NHBLR_Pesc[2]-perc_NHBLR_Pesc[1])

print "Sy1=", xm_Sy1_Pesc[0], xm_Sy1_Pesc[0]-xl_Sy1_Pesc[0],xh_Sy1_Pesc[0]-xm_Sy1_Pesc[0]

print "HBLR=",xm_HBLR_Pesc[0],xm_HBLR_Pesc[0]-xl_HBLR_Pesc[0],xh_HBLR_Pesc[0]-xm_HBLR_Pesc[0]
print "NHBLR=",xm_NHBLR_Pesc[0],xm_NHBLR_Pesc[0]-xl_NHBLR_Pesc[0],xh_NHBLR_Pesc[0]-xm_NHBLR_Pesc[0]


plt.figure()

plt.subplots_adjust(hspace=0.3)
plt.subplots_adjust(wspace=0.2)

plt.subplot(241)
plt.ylim(0,0.4)
pylab.hist(sigma_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3, label='QSOs present work')
pylab.hist(sigma_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2, label='Seyfert 1s (Ichikawa et al. 2015)')
pylab.hist(sigma_HBLR, 50, normed=1, histtype='stepfilled',color='pink', alpha=0.5,linewidth = 2, label='HBLR (Ichikawa et al. 2015)')
pylab.hist(sigma_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2, label='NHBLR (Ichikawa et al. 2015)')
plt.plot(xl_qso_sigma,y,'k--', linewidth = 2)
plt.plot(xh_qso_sigma,y,'k--', linewidth = 2)
plt.plot(xm_qso_sigma,y,'k-', linewidth = 3)
plt.plot(xm_Sy1_sigma,y,'b-', linewidth = 2)
plt.plot(xl_Sy1_sigma,y,'b--', linewidth = 2)
plt.plot(xh_Sy1_sigma,y,'b--', linewidth = 2)
plt.plot(xm_HBLR_sigma,y,'r-', linewidth = 2)
plt.plot(xl_HBLR_sigma,y,'r--', linewidth = 2)
plt.plot(xh_HBLR_sigma,y,'r--', linewidth = 2)
plt.plot(xm_NHBLR_sigma,y,'g-', linewidth = 2)


plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$\sigma_{Torus} [deg] $',fontsize=26)
plt.ylabel('Probability distribution function',fontsize=24)

f1 = open('MW-test/sigma_qso.dat','w+')
for i in range(0,len(sigma_qso)):
  print >>f1,sigma_qso[i]
f1.close()

f2 = open('MW-test/sigma_Sy1.dat','w+')
for i in range(0,len(sigma_Sy1)):
  print >>f2,sigma_Sy1[i]
f2.close()

plt.subplot(242)
plt.ylim(0,0.6)
pylab.hist(Y_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(Y_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(Y_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(Y_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_Y,y,'k--', linewidth = 2)
plt.plot(xh_qso_Y,y,'k--', linewidth = 2)
plt.plot(xm_qso_Y,y,'k-', linewidth = 3)
plt.plot(xm_Sy1_Y,y,'b-', linewidth = 2)
plt.plot(xl_Sy1_Y,y,'b--', linewidth = 2)
plt.plot(xh_Sy1_Y,y,'b--', linewidth = 2)
plt.plot(xm_HBLR_Y,y,'r-', linewidth = 2)
plt.plot(xl_HBLR_Y,y,'r--', linewidth = 2)
plt.plot(xh_HBLR_Y,y,'r--', linewidth = 2)
plt.plot(xm_NHBLR_Y,y,'g-', linewidth = 2)
plt.plot(xl_NHBLR_Y,y,'g--', linewidth = 2)
plt.plot(xh_NHBLR_Y,y,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$Y $',fontsize=24)

plt.subplot(243)
plt.ylim(0,0.9)
pylab.hist(No_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(No_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(No_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(No_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_No,y,'k--', linewidth = 2)
plt.plot(xh_qso_No,y,'k--', linewidth = 2)
plt.plot(xm_qso_No,y,'k-', linewidth = 3)
plt.plot(xm_Sy1_No,y,'b-', linewidth = 2)
plt.plot(xl_Sy1_No,y,'b--', linewidth = 2)
plt.plot(xh_Sy1_No,y,'b--', linewidth = 2)
plt.plot(xm_HBLR_No,y,'r-', linewidth = 2)
plt.plot(xl_HBLR_No,y,'r--', linewidth = 2)
plt.plot(xh_HBLR_No,y,'r--', linewidth = 2)
plt.plot(xm_NHBLR_No,y,'g-', linewidth = 2)
plt.plot(xl_NHBLR_No,y,'g--', linewidth = 2)
plt.plot(xh_NHBLR_No,y,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$N_{0} $',fontsize=24)

plt.subplot(244)
y1=(0,4)
plt.ylim(0,3.6)
pylab.hist(q_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(q_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(q_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(q_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_q,y1,'k--', linewidth = 2)
plt.plot(xh_qso_q,y1,'k--', linewidth = 2)
plt.plot(xm_qso_q,y1,'k-', linewidth = 3)
plt.plot(xm_Sy1_q,y1,'b-', linewidth = 2)
plt.plot(xl_Sy1_q,y1,'b--', linewidth = 2)
plt.plot(xh_Sy1_q,y1,'b--', linewidth = 2)
plt.plot(xm_HBLR_q,y1,'r-', linewidth = 2)
plt.plot(xl_HBLR_q,y1,'r--', linewidth = 2)
plt.plot(xh_HBLR_q,y1,'r--', linewidth = 2)
plt.plot(xm_NHBLR_q,y1,'g-', linewidth = 2)
plt.plot(xl_NHBLR_q,y1,'g--', linewidth = 2)
plt.plot(xh_NHBLR_q,y1,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$q $',fontsize=24)

plt.subplot(245)
plt.ylim(0,0.3)
pylab.hist(TauV_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(TauV_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(TauV_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(TauV_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_TauV,y,'k--', linewidth = 2)
plt.plot(xh_qso_TauV,y,'k--', linewidth = 2)
plt.plot(xm_qso_TauV,y,'k-', linewidth = 3)
plt.plot(xm_Sy1_TauV,y,'b-', linewidth = 2)
plt.plot(xl_Sy1_TauV,y,'b--', linewidth = 2)
plt.plot(xh_Sy1_TauV,y,'b--', linewidth = 2)
plt.plot(xm_HBLR_TauV,y,'r-', linewidth = 2)
plt.plot(xl_HBLR_TauV,y,'r--', linewidth = 2)
plt.plot(xh_HBLR_TauV,y,'r--', linewidth = 2)
plt.plot(xm_NHBLR_TauV,y,'g-', linewidth = 2)
plt.plot(xl_NHBLR_TauV,y,'g--', linewidth = 2)
plt.plot(xh_NHBLR_TauV,y,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$\tau_{V} $',fontsize=26)
plt.ylabel('Probability distribution function',fontsize=24)

plt.subplot(246)
plt.ylim(0,0.4)
pylab.hist(i_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(i_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(i_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(i_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_i,y,'k--', linewidth = 2)
plt.plot(xh_qso_i,y,'k--', linewidth = 2)
plt.plot(xm_qso_i,y,'k-', linewidth = 3)
plt.plot(xm_Sy1_i,y,'b-', linewidth = 2)
plt.plot(xl_Sy1_i,y,'b--', linewidth = 2)
plt.plot(xh_Sy1_i,y,'b--', linewidth = 2)
plt.plot(xm_HBLR_i,y,'r-', linewidth = 2)
plt.plot(xl_HBLR_i,y,'r--', linewidth = 2)
plt.plot(xh_HBLR_i,y,'r--', linewidth = 2)
plt.plot(xm_NHBLR_i,y,'g-', linewidth = 2)
plt.plot(xl_NHBLR_i,y,'g--', linewidth = 2)
plt.plot(xh_NHBLR_i,y,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$i [deg] $',fontsize=26)


plt.subplot(247)
plt.ylim(0,11)
y2=(0,12)
plt.xlim(0,1.1)
pylab.hist(Pesc_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(Pesc_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(Pesc_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(Pesc_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_Pesc,y2,'k--', linewidth = 2)
plt.plot(xh_qso_Pesc,y2,'k--', linewidth = 2)
plt.plot(xm_qso_Pesc,y2,'k-', linewidth = 3)
plt.plot(xm_Sy1_Pesc,y2,'b-', linewidth = 2)
plt.plot(xl_Sy1_Pesc,y2,'b--', linewidth = 2)
plt.plot(xh_Sy1_Pesc,y2,'b--', linewidth = 2)
plt.plot(xm_HBLR_Pesc,y2,'r-', linewidth = 2)
plt.plot(xl_HBLR_Pesc,y2,'r--', linewidth = 2)
plt.plot(xh_HBLR_Pesc,y2,'r--', linewidth = 2)
plt.plot(xm_NHBLR_Pesc,y2,'g-', linewidth = 2)
plt.plot(xl_NHBLR_Pesc,y2,'g--', linewidth = 2)
plt.plot(xh_NHBLR_Pesc,y2,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$P_{esc}$',fontsize=26)

plt.subplot(248)
plt.ylim(0,20)
y3=(0,25)
pylab.hist(f2_qso, 50, normed=1, histtype='stepfilled',color='black', linewidth = 3)
pylab.hist(f2_Sy1, 50, normed=1, histtype='stepfilled',color='LightBlue',alpha=0.5, linewidth = 2)
pylab.hist(f2_HBLR, 50, normed=1, histtype='stepfilled',color='pink',alpha=0.5, linewidth = 2)
pylab.hist(f2_NHBLR, 50, normed=1, histtype='stepfilled',color='LightGreen',alpha=0.5, linewidth = 2)
plt.plot(xl_qso_f2,y3,'k--', linewidth = 2)
plt.plot(xh_qso_f2,y3,'k--', linewidth = 2)
plt.plot(xm_qso_f2,y3,'k-', linewidth = 3)
plt.plot(xm_Sy1_f2,y3,'b-', linewidth = 2)
plt.plot(xl_Sy1_f2,y3,'b--', linewidth = 2)
plt.plot(xh_Sy1_f2,y3,'b--', linewidth = 2)
plt.plot(xm_HBLR_f2,y3,'r-', linewidth = 2)
plt.plot(xl_HBLR_f2,y3,'r--', linewidth = 2)
plt.plot(xh_HBLR_f2,y3,'r--', linewidth = 2)
plt.plot(xm_NHBLR_f2,y3,'g-', linewidth = 2)
plt.plot(xl_NHBLR_f2,y3,'g--', linewidth = 2)
plt.plot(xh_NHBLR_f2,y3,'g--', linewidth = 2)

plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.xlabel(r'$f_{2}$',fontsize=26)
plt.legend(loc = 'best', numpoints=1, prop={'size':20})
#plt.savefig('global_QSOs.png')
plt.show()