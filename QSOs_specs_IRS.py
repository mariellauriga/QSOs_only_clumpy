import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from matplotlib.patches import Ellipse, Polygon
import math
import scipy.optimize as optimization
from scipy.interpolate import interp1d
from scipy import interpolate

#f_ind=[10,20000]

#______________________________
#%%%%%%%%%%Constants%%%%%%%%%%%
#------------------------------
zIIZw136 = 0.063
zIZw1 = 0.0589
zMrk509 = 0.0344
zpg0003_199 = 0.0258
zpg0007_106 = 0.089
zpg0804_761 = 0.1
zpg0844_349 = 0.064
zpg0923_129 = 0.0292
zpg1211_143 = 0.0809
zpg1229_204 = 0.063
zpg1351_640 = 0.0882
zpg1411_442 = 0.09
zpg1426_015 = 0.086
zpg1440_356 = 0.079
zpg1448_273 = 0.0650
zpg1501_106 = 0.0364
zpg1534_580 = 0.0296
zpg1535_547 = 0.0389
zpg2214_139 = 0.066

c=3.e14 # um s^{-1}

x1=[6.2, 6.2]
x2=[6.7,6.7]
x3=[7.7,7.7]
x4=[8.3, 8.3]
x5=[8.6,8.6]
x6=[10.5,10.5]
x7=[10.7, 10.7]
x8=[11.3,11.3]
x9=[12.0,12.0]
x10=[12.7,12.7]
x11=[17.,17.]

y1=[0,500]


#_________________________________________________
#%%%%%%%%%%% Spectra%%%%%%%%%%%%%%%
#-------------------------------------------------
xnew = loadtxt('new_points.dat', unpack=True)
xnew2 = loadtxt('new_points2.dat', unpack=True)

xIIZw136, fIIZw136, eIIZw136 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/IIZw136/spitzer_IIZw136_2.dat', unpack=True)
xIIZw136 = xIIZw136/(1+zIIZw136)
yIIZw136 = interpolate.interp1d(xIIZw136, fIIZw136, kind='cubic')
yIIZw136 = yIIZw136(xnew)
eyIIZw136 = interpolate.interp1d(xIIZw136, eIIZw136, kind='cubic')
eyIIZw136 = eyIIZw136(xnew)

xIIZw136_cc, fIIZw136_cc, a,b = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/IIZw136/Spec_m1_stck_IIZw136.dat', unpack=True)
fIIZw136_cc = fIIZw136_cc*1000./1.25
eIIZw136_cc = 0.15*fIIZw136_cc
xIIZw136_cc = xIIZw136_cc/10000.
xIIZw136_cc = xIIZw136_cc/(1+zIIZw136)
yIIZw136_cc = interpolate.interp1d(xIIZw136_cc, fIIZw136_cc, kind='cubic')
yIIZw136_cc = yIIZw136_cc(xnew2)
eyIIZw136_cc= interpolate.interp1d(xIIZw136_cc, eIIZw136_cc, kind='cubic')
eyIIZw136_cc = eyIIZw136_cc(xnew2)


xIZw1, fIZw1, eIZw1 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/IZw1/spitzer_IZw1_2.dat', unpack=True)
xIZw1 = xIZw1/(1+zIZw1)
yIZw1 = interpolate.interp1d(xIZw1, fIZw1, kind='cubic')
yIZw1 = yIZw1(xnew)
eyIZw1 = interpolate.interp1d(xIZw1, eIZw1, kind='cubic')
eyIZw1 = eyIZw1(xnew)


xMrk509, fMrk509, emrk509 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/MRK0509/spitzer_mrk509_2.dat', unpack=True)
xMrk509 = xMrk509/(1+zMrk509)
yMrk509 = interpolate.interp1d(xMrk509, fMrk509, kind='cubic')
yMrk509 = yMrk509(xnew)
eyMrk509 = interpolate.interp1d(xMrk509, emrk509, kind='cubic')
eyMrk509 = eyMrk509(xnew)

#xpg0003_199, fpg0003_199, e = loadtxt('PG0003_199/silicates/spitzer_mrk335_2.dat', unpack=True)
#xpg0003_199 = xpg0003_199/(1+zpg0003_199)
#ypg0003_199 = interpolate.interp1d(xpg0003_199, fpg0003_199, kind='cubic')
#ypg0003_199 = ypg0003_199(xnew)

xpg0003_199_cc, fpg0003_199_cc, a,b = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG0003_199/Spec_m0_stck_MRK0335.dat', unpack=True)
fpg0003_199_cc = fpg0003_199_cc*1000.*1.67
epg0003_cc = fpg0003_199_cc*0.15
xpg0003_199_cc = xpg0003_199_cc*1.e-4
xpg0003_199_cc = xpg0003_199_cc/(1+zpg0003_199)
ypg0003_199_cc = interpolate.interp1d(xpg0003_199_cc, fpg0003_199_cc, kind='cubic')
ypg0003_199_cc = ypg0003_199_cc(xnew2)
eypg0003_199_cc = interpolate.interp1d(xpg0003_199_cc, epg0003_cc, kind='cubic')
eypg0003_199_cc = eypg0003_199_cc(xnew2)


xpg0007_106, fpg0007_106, epg0007 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG0007+106/spitzer_pg0007_106_2.dat', unpack=True)
xpg0007_106 = xpg0007_106/(1+zpg0007_106)
ypg0007_106 = interpolate.interp1d(xpg0007_106, fpg0007_106)
ypg0007_106 = ypg0007_106(xnew)
eypg0007_106 = interpolate.interp1d(xpg0007_106, epg0007)
eypg0007_106 = eypg0007_106(xnew)

xpg0804_761, fpg0804_761, epg0804 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG0804+761/spitzer_pg0804_761_2.dat', unpack=True)
xpg0804_761 = xpg0804_761/(1+zpg0804_761)
ypg0804_761 = interpolate.interp1d(xpg0804_761, fpg0804_761)
ypg0804_761 = ypg0804_761(xnew)
eypg0804_761 = interpolate.interp1d(xpg0804_761, epg0804)
eypg0804_761 = eypg0804_761(xnew)

xpg0804_761_cc, fpg0804_761_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG0804+761/cc_spec_pg0804+761_prom.dat', unpack=True)
fpg0804_761_cc = fpg0804_761_cc*1000.
epg0804_cc = 0.15*fpg0804_761_cc
xpg0804_761_cc = xpg0804_761_cc/10000.
xpg0804_761_cc = xpg0804_761_cc/(1+zpg0804_761)
ypg0804_761_cc = interpolate.interp1d(xpg0804_761_cc, fpg0804_761_cc)
ypg0804_761_cc = ypg0804_761_cc(xnew2)
eypg0804_761_cc = interpolate.interp1d(xpg0804_761_cc, epg0804_cc)
eypg0804_761_cc = eypg0804_761_cc(xnew2)

xpg0844_349, fpg0844_349, epg0844 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG0844+349/spitzer_pg0844_349_2.dat', unpack=True)
xpg0844_349 = xpg0844_349/(1+zpg0844_349)
ypg0844_349 = interpolate.interp1d(xpg0844_349, fpg0844_349)
ypg0844_349 = ypg0844_349(xnew)
eypg0844_349 = interpolate.interp1d(xpg0844_349, epg0844)
eypg0844_349 = eypg0844_349(xnew)

xpg0844_349_cc, fpg0844_349_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG0844+349/cc_spec_pg0844+349_prom.dat', unpack=True)
fpg0844_349_cc = fpg0844_349_cc*1000.
epg0844_cc = 0.15*fpg0844_349_cc
xpg0844_349_cc = xpg0844_349_cc/10000.
xpg0844_349_cc = xpg0844_349_cc/(1+zpg0844_349)
ypg0844_349_cc = interpolate.interp1d(xpg0844_349_cc, fpg0844_349_cc)
ypg0844_349_cc = ypg0844_349_cc(xnew2)
eypg0844_349_cc = interpolate.interp1d(xpg0844_349_cc, epg0844_cc)
eypg0844_349_cc = eypg0844_349_cc(xnew2)

xpg0923_129, fpg0923_129, epg0923 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG0923+129/spitzer_pg0923_129_2.dat', unpack=True)
xpg0923_129 = xpg0923_129/(1+zpg0923_129)
ypg0923_129 = interpolate.interp1d(xpg0923_129, fpg0923_129)
ypg0923_129 = ypg0923_129(xnew)
eypg0923_129 = interpolate.interp1d(xpg0923_129, epg0923)
eypg0923_129 = eypg0923_129(xnew)

xpg1211_143, fpg1211_143, epg1211 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1211+143/spitzer_pg1211_143_2.dat', unpack=True)
xpg1211_143 = xpg1211_143/(1+zpg1211_143)
ypg1211_143 = interpolate.interp1d(xpg1211_143, fpg1211_143)
ypg1211_143 = ypg1211_143(xnew)
eypg1211_143 = interpolate.interp1d(xpg1211_143, epg1211)
eypg1211_143 = eypg1211_143(xnew)

xpg1211_143_cc, fpg1211_143_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1211+143/cc_spec_pg1211+143_prom.dat', unpack=True)
fpg1211_143_cc = fpg1211_143_cc*1000./1.12
epg1211_cc = 0.15*fpg1211_143_cc
xpg1211_143_cc = xpg1211_143_cc/10000.
xpg1211_143_cc = xpg1211_143_cc/(1+zpg1211_143)
ypg1211_143_cc= interpolate.interp1d(xpg1211_143_cc, fpg1211_143_cc)
ypg1211_143_cc = ypg1211_143_cc(xnew2)
eypg1211_143_cc= interpolate.interp1d(xpg1211_143_cc, epg1211_cc)
eypg1211_143_cc = eypg1211_143_cc(xnew2)


xpg1229_204, fpg1229_204, epg1229 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1229+204/spitzer_pg1229_204_2.dat', unpack=True)
xpg1229_204 = xpg1229_204/(1+zpg1229_204)
ypg1229_204 = interpolate.interp1d(xpg1229_204, fpg1229_204)
ypg1229_204 = ypg1229_204(xnew)
eypg1229_204 = interpolate.interp1d(xpg1229_204, epg1229)
eypg1229_204 = eypg1229_204(xnew)

xpg1229_204_cc, fpg1229_204_cc, a,b = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1229+204/Spec_m1_stck_PG1229+204.dat', unpack=True)
fpg1229_204_cc = fpg1229_204_cc*1000.
epg1229_cc = 0.15*fpg1229_204_cc
xpg1229_204_cc = xpg1229_204_cc/10000.
xpg1229_204_cc = xpg1229_204_cc/(1+zpg1229_204)
ypg1229_204_cc= interpolate.interp1d(xpg1229_204_cc, fpg1229_204_cc)
ypg1229_204_cc = ypg1229_204_cc(xnew2)
eypg1229_204_cc= interpolate.interp1d(xpg1229_204_cc, epg1229_cc)
eypg1229_204_cc = eypg1229_204_cc(xnew2)


xpg1351_640, fpg1351_640, epg1351 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1351+640/spitzer_pg1351_640_2.dat', unpack=True)
xpg1351_640 = xpg1351_640/(1+zpg1351_640)
ypg1351_640 = interpolate.interp1d(xpg1351_640, fpg1351_640)
ypg1351_640 = ypg1351_640(xnew)
eypg1351_640 = interpolate.interp1d(xpg1351_640, epg1351)
eypg1351_640 = eypg1351_640(xnew)


xpg1411_442, fpg1411_442, epg1411 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1411+442/spitzer_pg1411_442_2.dat', unpack=True)
xpg1411_442 = xpg1411_442/(1+zpg1411_442)
ypg1411_442 = interpolate.interp1d(xpg1411_442, fpg1411_442)
ypg1411_442 = ypg1411_442(xnew)
eypg1411_442 = interpolate.interp1d(xpg1411_442, epg1411)
eypg1411_442 = eypg1411_442(xnew)

xpg1411_442_cc, fpg1411_442_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1411+442/cc_spec_pg1411+442_prom.dat', unpack=True)
fpg1411_442_cc = fpg1411_442_cc*1000.*1.27
epg1411_cc = fpg1411_442_cc*0.15
xpg1411_442_cc = xpg1411_442_cc/10000.
xpg1411_442_cc = xpg1411_442_cc/(1+zpg1411_442)
ypg1411_442_cc= interpolate.interp1d(xpg1411_442_cc, fpg1411_442_cc)
ypg1411_442_cc = ypg1411_442_cc(xnew2)
eypg1411_442_cc= interpolate.interp1d(xpg1411_442_cc, epg1411_cc)
eypg1411_442_cc = eypg1411_442_cc(xnew2)

xpg1426_015, fpg1426_015, epg1426 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1426+015/spitzer_mrk1383_2.dat', unpack=True)
xpg1426_015 = xpg1426_015/(1+zpg1426_015)
ypg1426_015 = interpolate.interp1d(xpg1426_015, fpg1426_015)
ypg1426_015 = ypg1426_015(xnew)
eypg1426_015 = interpolate.interp1d(xpg1426_015, epg1426)
eypg1426_015 = eypg1426_015(xnew)

xpg1426_015_cc, fpg1426_015_cc, a,b = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1426+015/Spec_m1_stck_Mrk1383_OB71.dat', unpack=True)
fpg1426_015_cc = fpg1426_015_cc*1000./1.22
epg1426_cc = 0.15*fpg1426_015_cc
xpg1426_015_cc = xpg1426_015_cc/10000.
xpg1426_015_cc = xpg1426_015_cc/(1+zpg1426_015)
ypg1426_015_cc= interpolate.interp1d(xpg1426_015_cc, fpg1426_015_cc)
ypg1426_015_cc = ypg1426_015_cc(xnew2)
eypg1426_015_cc= interpolate.interp1d(xpg1426_015_cc, epg1426_cc)
eypg1426_015_cc = eypg1426_015_cc(xnew2)


xpg1440_356, fpg1440_356, epg1440 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1440+356/spitzer_mrk478_2.dat', unpack=True)
xpg1440_356 = xpg1440_356/(1+zpg1440_356)
ypg1440_356 = interpolate.interp1d(xpg1440_356, fpg1440_356)
ypg1440_356 = ypg1440_356(xnew)
eypg1440_356 = interpolate.interp1d(xpg1440_356, epg1440)
eypg1440_356 = eypg1440_356(xnew)

xpg1440_356_cc, fpg1440_356_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1440+356/cc_spec_mrk478_prom.dat', unpack=True)
fpg1440_356_cc = fpg1440_356_cc*1000.*1.49
epg1440_cc = 0.15*fpg1440_356_cc
xpg1440_356_cc = xpg1440_356_cc/10000.
xpg1440_356_cc = xpg1440_356_cc/(1+zpg1440_356)
ypg1440_356_cc = interpolate.interp1d(xpg1440_356_cc, fpg1440_356_cc)
ypg1440_356_cc = ypg1440_356_cc(xnew2)
eypg1440_356_cc = interpolate.interp1d(xpg1440_356_cc, epg1440_cc)
eypg1440_356_cc = eypg1440_356_cc(xnew2)

xpg1448_273, fpg1448_273, epg1448 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1448+273/spitzer_pg1448_273_2.dat', unpack=True)
xpg1448_273 = xpg1448_273/(1+zpg1448_273)
ypg1448_273 = interpolate.interp1d(xpg1448_273, fpg1448_273)
ypg1448_273 = ypg1448_273(xnew)
eypg1448_273 = interpolate.interp1d(xpg1448_273, epg1448)
eypg1448_273 = eypg1448_273(xnew)


xpg1501_106, fpg1501_106, epg1501 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1501+106/spitzer_mrk841_2.dat', unpack=True)
xpg1501_106 = xpg1501_106/(1+zpg1501_106)
ypg1501_106 = interpolate.interp1d(xpg1501_106, fpg1501_106)
ypg1501_106 = ypg1501_106(xnew)
eypg1501_106 = interpolate.interp1d(xpg1501_106, epg1501)
eypg1501_106 = eypg1501_106(xnew)

xpg1501_106_cc, fpg1501_106_cc = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/PG1501+106/cc_spec_mrk841_prom.dat', unpack=True)
fpg1501_106_cc = fpg1501_106_cc*1000.*1.11
epg1501_cc = 0.15*fpg1501_106_cc
xpg1501_106_cc = xpg1501_106_cc/10000.
xpg1501_106_cc = xpg1501_106_cc/(1+zpg1501_106)
ypg1501_106_cc = interpolate.interp1d(xpg1501_106_cc, fpg1501_106_cc)
ypg1501_106_cc = ypg1501_106_cc(xnew2)
eypg1501_106_cc = interpolate.interp1d(xpg1501_106_cc, epg1501_cc)
eypg1501_106_cc = eypg1501_106_cc(xnew2)

xpg1534_580, fpg1534_580, epg1534 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1534+580/spitzer_pg1534_580_2.dat', unpack=True)
xpg1534_580 = xpg1534_580/(1+zpg1534_580)
ypg1534_580 = interpolate.interp1d(xpg1534_580, fpg1534_580)
ypg1534_580 = ypg1534_580(xnew)
eypg1534_580 = interpolate.interp1d(xpg1534_580, epg1534)
eypg1534_580 =eypg1534_580(xnew)


xpg1535_547, fpg1535_547, epg1535 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG1535+547/spitzer_pg1535_547_2.dat', unpack=True)
xpg1535_547 = xpg1535_547/(1+zpg1535_547)
ypg1535_547 = interpolate.interp1d(xpg1535_547, fpg1535_547)
ypg1535_547 = ypg1535_547(xnew)
eypg1535_547 = interpolate.interp1d(xpg1535_547, epg1535)
eypg1535_547 = eypg1535_547(xnew)

xpg2214_139, fpg2214_139, epg2214 = loadtxt('/home/mariela/piratas-project/QSOs/spitzer_spectrum/PG2214+139/spitzer_pg2214_139_2.dat', unpack=True)
xpg2214_139 = xpg2214_139/(1+zpg2214_139)
ypg2214_139 = interpolate.interp1d(xpg2214_139, fpg2214_139)
ypg2214_139 = ypg2214_139(xnew)
eypg2214_139 = interpolate.interp1d(xpg2214_139, epg2214)
eypg2214_139 = eypg2214_139(xnew)

xmr2251_cc, fmr2251_cc, a,b = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/MR2251_178/Spec_m1_stck_MR2251-178.dat', unpack=True)
fmr2251_cc = fmr2251_cc*1000.*1.11
emr2251_cc = 0.15*fmr2251_cc
xmr2251_cc = xmr2251_cc/10000.
xmr2251_cc = xmr2251_cc/(1+0.0640)
ymr2251_cc= interpolate.interp1d(xmr2251_cc, fmr2251_cc)
ymr2251_cc = ymr2251_cc(xnew2)
eymr2251_cc = interpolate.interp1d(xmr2251_cc, emr2251_cc)
eymr2251_cc = eymr2251_cc(xnew2)



xmrk509_visir, fmrk509_visir, emrk509_visr = loadtxt('/home/mariela/piratas-project/QSOs/SEDs/MRK0509/Pili_VISIR_MARK509.txt', unpack=True)
xmrk509_visir = xmrk509_visir*(1.e+6)/(1 + zMrk509)
fmrk509_visir = fmrk509_visir*(1.e+3)/1.4
emrk509_visr = emrk509_visr*(1.e+3)
coc = emrk509_visr/fmrk509_visir
emrk509_visr = emrk509_visr*coc
ymrk509_visir= interpolate.interp1d(xmrk509_visir, fmrk509_visir)
ymrk509_visir = ymrk509_visir(xnew2)
eymrk509_visir = interpolate.interp1d(xmrk509_visir, emrk509_visr)
eymrk509_visir = eymrk509_visir(xnew2)


xIZw1_visir, fIZw1_visir,eIZw1_visir= loadtxt('/home/mariela/piratas-project/QSOs/SEDs/IZw1/IZwicky1.txt', unpack=True)
fIZw1_visir = fIZw1_visir*1000.
eIZw1_visir = eIZw1_visir*1000.

xIZw1_visir = xIZw1_visir/(1+zIZw1)
yIZw1_visir= interpolate.interp1d(xIZw1_visir, fIZw1_visir)
yIZw1_visir = yIZw1_visir(xnew2)
eyIZw1_visir = interpolate.interp1d(xIZw1_visir, eIZw1_visir)
eyIZw1_visir = eyIZw1_visir(xnew2)

#Spitzer.....
yprom1 = ypg0007_106
yprom2 = ypg0923_129
yprom3 =  ypg1351_640 + ypg1448_273 + ypg1534_580 

yprom_4 = ypg2214_139+ypg1535_547


yprom_comunes_PAH = ypg0844_349 + ypg1426_015 + ypg1440_356 + yIZw1 + yMrk509 
yprom_comunes_noPAH = ypg0804_761+ypg1211_143+ypg1229_204+ypg1411_442+ypg1501_106+yIIZw136
y_prom_PAH = yprom_comunes_PAH/5
y_prom_noPAH = yprom_comunes_noPAH/6

ey_prom_PAH = eypg0844_349 + eypg1426_015 + eypg1440_356 + eyIZw1 + eyMrk509 
ey_prom_noPAH = eypg0804_761+eypg1211_143+eypg1229_204+eypg1411_442+eypg1501_106+eyIIZw136
ey_prom_PAH = ey_prom_PAH/5
ey_prom_noPAH = ey_prom_noPAH/6


#Nuclerares
ycc_noPAH = ypg0804_761_cc + ypg1211_143_cc + ypg1229_204_cc + ypg1411_442_cc + ypg1501_106_cc + yIIZw136_cc 

#ypg0003_199_cc 
ycc_PAH =  ypg0844_349_cc + ypg1426_015_cc + ypg1440_356_cc 


eycc_PAH = ( eypg0844_349_cc + eypg1426_015_cc + eypg1440_356_cc+eyIZw1_visir+eymrk509_visir)/5
eycc_noPAH = (eypg0804_761_cc + eypg1211_143_cc + eypg1229_204_cc + eypg1411_442_cc + eypg1501_106_cc + eyIIZw136_cc)/6

ycc_PAH = (ycc_PAH+yIZw1_visir+ymrk509_visir)/5
ycc_noPAH = ycc_noPAH/6 

plt.subplot(121)

plt.fill_between(xnew, y_prom_PAH, y_prom_PAH+ey_prom_PAH, color='LightBlue')
plt.fill_between(xnew, y_prom_PAH, y_prom_PAH-ey_prom_PAH, color='LightBlue')
plt.plot(xnew, y_prom_PAH, '--',linewidth = 4,color='blue',label='IRS/Spitzer QSOs PAHs')

plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH+ey_prom_noPAH, color='LightGreen')
plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH-ey_prom_noPAH, color='LightGreen')
plt.plot(xnew, y_prom_noPAH, '--',linewidth = 4,color='green',label='IRS/Spitzer QSOs no-PAHs')
#plt.plot(xnew, 1.42*y_prom_noPAH, '--',linewidth = 4,color='green')

plt.fill_between(xnew2, ycc_PAH, ycc_PAH + eycc_PAH, color='LightBlue')
plt.fill_between(xnew2, ycc_PAH, ycc_PAH - eycc_PAH, color='LightBlue')
plt.plot(xnew2, ycc_PAH,linewidth=4,color='blue', label='Nuclear spectrum QSOs PAHs')

plt.fill_between(xnew2, ycc_noPAH, ycc_noPAH + eycc_noPAH, color='LightGreen')
plt.fill_between(xnew2, ycc_noPAH, ycc_noPAH - eycc_noPAH, color='LightGreen')
plt.plot(xnew2, ycc_noPAH,linewidth=4,color='green', label='Nuclear spectrum QSOs no-PAHs')

#plt.plot(xnew2, ycc_total, linewidth=4, color='red', label='CC/GTC all QSOs')

plt.plot(x3, y1, 'k--', color='grey')
text(7.8,250,r"PAH",color='grey',fontsize=14)
plt.plot(x6, y1, 'k--', color='grey')
plt.plot(x8, y1, 'k--', color='grey')
text(11.35,250,r"PAH",color='grey',fontsize=14 )
text(9.5,250,r"[SIV]",color='grey',fontsize=14 )


plt.legend(loc = 'best', numpoints=1, prop={'size':20})
tick_params(axis='x', labelsize=22)
tick_params(axis='y', labelsize=22)

plt.ylabel(r" $f_{\nu}$ (mJy)",fontsize=26)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=26)


plt.subplot(122)
ln12 = np.where(xnew == 11.0)
y_prom_PAH = y_prom_PAH/y_prom_PAH[ln12]
y_prom_noPAH = y_prom_noPAH/y_prom_noPAH[ln12]
ey_prom_PAH = ey_prom_PAH/(y_prom_PAH)
ey_prom_noPAH = ey_prom_noPAH/(y_prom_noPAH)

#plt.fill_between(xnew, y_prom_PAH, y_prom_PAH+ey_prom_PAH, color='LightBlue')
#plt.fill_between(xnew, y_prom_PAH, y_prom_PAH-ey_prom_PAH, color='LightBlue')
plt.plot(xnew, y_prom_PAH, '--',linewidth = 4,color='blue',label='IRS/Spitzer QSOs PAHs')

#plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH+ey_prom_noPAH, color='LightGreen')
#plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH-ey_prom_noPAH, color='LightGreen')
plt.plot(xnew, y_prom_noPAH, '--',linewidth = 4,color='green',label='IRS/Spitzer QSOs no-PAHs')
#plt.plot(xnew, 1.42*y_prom_noPAH, '--',linewidth = 4,color='green')

ln12 = np.where(xnew2 == 11.0)
ycc_PAH = ycc_PAH/ycc_PAH[ln12]
ycc_noPAH = ycc_noPAH/ycc_noPAH[ln12]
eycc_PAH = eycc_PAH/(ycc_PAH)
eycc_noPAH = eycc_noPAH/(ycc_noPAH)

#plt.fill_between(xnew2, ycc_PAH, ycc_PAH + eycc_PAH, color='LightBlue')
#plt.fill_between(xnew2, ycc_PAH, ycc_PAH - eycc_PAH, color='LightBlue')
plt.plot(xnew2, ycc_PAH,linewidth=4,color='blue', label='Nuclear spectrum QSOs PAHs')

#plt.fill_between(xnew2, ycc_noPAH, ycc_noPAH + eycc_noPAH, color='LightGreen')
#plt.fill_between(xnew2, ycc_noPAH, ycc_noPAH - eycc_noPAH, color='LightGreen')
plt.plot(xnew2, ycc_noPAH,linewidth=4,color='green', label='Nuclear spectrum QSOs no-PAHs')

#plt.plot(xnew2, ycc_total, linewidth=4, color='red', label='CC/GTC all QSOs')

plt.plot(x3, y1, 'k--', color='grey')
text(7.8,250,r"PAH",color='grey',fontsize=14)
plt.plot(x6, y1, 'k--', color='grey')
plt.plot(x8, y1, 'k--', color='grey')
text(11.35,250,r"PAH",color='grey',fontsize=14 )
text(9.5,250,r"[SIV]",color='grey',fontsize=14 )


plt.legend(loc = 'best', numpoints=1, prop={'size':20})
tick_params(axis='x', labelsize=22)
tick_params(axis='y', labelsize=22)

plt.ylabel(r" $f_{\nu}$ (mJy)",fontsize=26)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=26)


plt.ylim(0,2)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

plt.figure()


plt.plot(xIZw1, fIZw1, label='IZw1')
plt.plot(xpg0804_761, fpg0804_761, label='PG 0804+761')
plt.plot(xpg0923_129, fpg0923_129, label='PG 0923+129')
plt.plot(xpg1229_204, fpg1229_204, label='PG 1229+204')
plt.plot(xpg1351_640, fpg1351_640, label='PG 1351+640')
#plt.plot(xpg1411_442, fpg1411_442, label='PG 1411+442')
plt.plot(xpg1426_015, fpg1426_015, label='PG 1426+015')
plt.plot(xpg1440_356, fpg1440_356, label='PG 1440+356')
plt.plot(xpg1448_273, fpg1448_273, label='PG 1448+273')
plt.plot(xpg1501_106, fpg1501_106, label='PG 1501+106')
plt.plot(xpg1534_580, fpg1534_580, label='PG 1534+580')
plt.plot(xpg2214_139, fpg2214_139, label='PG 2214+139')

plt.xlim(5,35)

tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)

plt.xlabel('Wavelength ($\mu$m)',fontsize=18)
plt.ylabel(r'$f_{\nu}$ (mJy)',fontsize=18)


plt.figure()
plt.plot(xIIZw136, fIIZw136, label='IIZw136')
plt.plot(xMrk509, fMrk509, label='MRK 509')
#plt.plot(xpg0003_199, fpg0003_199, label='PG 0003+199')
plt.plot(xpg0007_106, fpg0007_106, label='PG 0007+106')
plt.plot(xpg1211_143, fpg1211_143, label='PG 1211+143')
plt.plot(xpg1535_547, fpg1535_547, label='PG 1535+547')
plt.plot(xpg0844_349, fpg0844_349, label='PG 0844+349')

#plt.legend( loc='best')
plt.xlim(5,35)

tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)

plt.xlabel('Wavelength ($\mu$m)',fontsize=18)
plt.ylabel(r'$f_{\nu}$ (mJy)',fontsize=18)


plt.figure()

plt.fill_between(xnew, y_prom_PAH, y_prom_PAH+ey_prom_PAH, color='LightBlue')
plt.fill_between(xnew, y_prom_PAH, y_prom_PAH-ey_prom_PAH, color='LightBlue')
plt.plot(xnew, y_prom_PAH, '--',linewidth = 4,color='blue',label='IRS/Spitzer QSOs clear PAHs')

#plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH+ey_prom_noPAH, color='LightGreen')
#plt.fill_between(xnew, y_prom_noPAH, y_prom_noPAH-ey_prom_noPAH, color='LightGreen')
plt.plot(xnew, 50+y_prom_noPAH, '--',linewidth = 4,color='green',label='IRS/Spitzer QSOs no-clear PAHs')


plt.plot(xnew2, yIZw1_visir, label='PG 0050+124 VISIR/VLT')
plt.plot(xnew2, ymrk509_visir, label='MRK 509 VISIR/VLT')
plt.plot(xnew2, ymr2251_cc, color='red', label='MR 2251+178 CC/GTC')

plt.plot(x3, y1, 'k--', color='grey')
text(7.8,250,r"PAH",color='grey',fontsize=14)
plt.plot(x6, y1, 'k--', color='grey')
plt.plot(x8, y1, 'k--', color='grey')
text(11.35,250,r"PAH",color='grey',fontsize=14 )
text(9.5,250,r"[SIV]",color='grey',fontsize=14 )


plt.legend(loc = 'best', numpoints=1, prop={'size':20})
tick_params(axis='x', labelsize=22)
tick_params(axis='y', labelsize=22)

plt.ylabel(r" $f_{\nu}$ (mJy)",fontsize=26)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=26)




plt.show()