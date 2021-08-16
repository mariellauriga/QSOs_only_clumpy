PRO contornos_ccam

;Targets
fits_read, 'FC_stck_combined_mrk1014.fits', target_sc
fits_read, 'FC_stck_S20130101S7303.fits', target_psf

;pixel scale in "/px
pxscale = 0.08
pyscale = 0.08
;size of the box to plot (tamaño de 0-2 en (Dx)")
Dx = 2.
Dx_px = 2./pxscale
Dy = 2.
Dy_py = 2./pyscale
;centroids of the object
xc = 160.37
yc = 122.45
xc_psf = 159.32
yc_psf = 119.02


;hace un vector de x_{0} a x_{f} conn una separacion pxscale
xx = stepvec(-Dx, Dx, pxscale)
yy = stepvec(-Dy, Dy, pyscale)

;object within a Dx x Dx boxmrk_plot, extrae una caja del frame original y del tamaño de Dx alrededor de las coordenadas xc y yc

target_sc =   target_sc[xc-Dx_px:xc+Dx_px, yc-Dy_py:yc+Dy_py]
target_psf = target_psf[xc_psf-Dx_px:xc_psf+Dx_px, yc_psf-Dy_py:yc_psf+Dy_py]

;contour levels
sigma_ori = 0.0598
sigma_ori_psf = 0.1205

SNR_ori_sc = max(target_sc)/sigma_ori
SNR_ori_psf = max(target_psf)/sigma_ori_psf

; contornos 
min_cont = 3
contour_step = 5
contour_step_psf = 300

level_target_sc = stepvec(min_cont*sigma_ori, SNR_ori_sc, contour_step)
level_target_psf = stepvec(min_cont*sigma_ori_psf, SNR_ori_psf, contour_step_psf)

;Convierte la imagen de DNs⁻1 a sigma
target_sc = target_sc/sigma_ori
target_psf = target_psf/sigma_ori_psf

;smoothing
;Usa una gausiana (la correlaciona con la imagen) para suavisarla.
target_sc = filter_image(target_sc,smooth=1)
target_psf = filter_image(target_psf,smooth=1)

;Otra cosa equivalente es el "binning" lo haces con congrid

;PLOT
;Cambia colores de la imagen (opciones del 1---8)
loadct,3
!p.multi=[0,2,1]
set_plot,'ps'

device,filename='mrk1014_contornos_ccam.eps',/landscape,/color,bits=16
!x.charsize = 1.8
!y.charsize = 1.8
!p.charsize=1.8

tvim, target_sc, xrange = xx, yrange = yy, xtitle = 'Offset (")', ytitle = 'Offset (")', title = 'PG 0157+002', range=[max(target_sc), 3*sigma_ori]
	contour,target_sc,xx,yy,/overplot,level=level_target_sc
	
tvim, target_psf, xrange = xx, yrange = yy, xtitle = 'Offset (")', ytitle = 'Offset (")', title = 'PSF', range=[max(target_psf), 3*sigma_ori_psf]
	contour,target_psf,xx,yy,/overplot,level=level_target_psf
		
		
		
		
device,/close

set_plot,'x'

STOP
END
