PRO mrk_plot

fits_read,'Mrk1383_add_redcvh.fits',mrk_ori

;pixel scale in "/px
pxscale = 0.08
;size of the box to plot
Dx = 2.
Dx_px = 2./0.08
;centroids og the object
xc = 160.51
yc = 121.94

xx = stepvec(-Dx,Dx,pxscale)

;object within a Dx x Dx boxmrk_plot
mrk_ori = mrk_ori[xc-Dx_px:xc+Dx_px,yc-Dx_px:yc+Dx_px]

;contour levels
sigma_ori = 0.0550
SNR_ori = max(mrk_ori)/sigma_ori
level_mrk_ori = stepvec(5*sigma_ori,SNR_ori,3)

mrk_ori = mrk_ori/sigma_ori


;smoothing
mrk_ori=filter_image(mrk_ori,smooth=2)

;PLOT
loadct,3
!p.multi=[0,2,1]

set_plot,'ps'
device,filename='mrk1014.ps',/landscape,/color,bits=16

tvim,mrk_ori,xrange=xx,yrange=xx,xtitle='Offset (")',ytitle='Offset (")',title='MRK1014',range=[max(mrk_ori),3*sigma_ori]
	contour,mrk_ori,xx,xx,/overplot,level=level_mrk_ori
	
device,/close
set_plot,'x'

SPAWN,'ps2pdf mrk1014.ps mrk1014.pdf', dummy
;SPAWN,'xdg-open PG0007_106_a_19.pdf'

STOP
END
