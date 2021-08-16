pro add_reduction_hv
close, /all
; Script to clean RedCan image. 
;You need the de Buizer IDL tools and Enrique IDL routine to create the artifitial star.

; Mariela Martinez

Mrk1383_comb=readfits('FC_stck_Mrk1383_combined.fits')
;#Vertical reduce
Mrk1383_v=noise_maskv(Mrk1383_comb ,noisemodel=noisemodel)

writefits, 'Mrk1383_add_redcv.fits', Mrk1383_v

writefits, 'Mrk1383_noise_model_v.fits', noisemodel

;#Horizontal reduce

Mrk1383_out_hv=noise_maskh(Mrk1383_v ,noisemodel=noisemodel)

writefits, 'Mrk1383_add_redc_hv.fits',Mrk1383_out_hv

writefits, 'Mrk1383_noise_model_hv.fits', noisemodel

;# Creatting the artificaial star
;Artifitial star for a S/N=5
;Flujo escalado y FWHM de la imagen original
;Flujo en una apertura de 9 pixels para Mrk1383
artificial_star,6.16,18.04,art_star

writefits, 'art_star_sn_5.fits',art_star

;#Adding an artificial star to flux calibrated image
Mrk1383_comb[176:186,101:111]=Mrk1383_comb[176:186,101:111]+art_star
Mrk1383_v_art=noise_maskv(Mrk1383_comb ,noisemodel=noisemodel)
writefits, 'Mrk1383_comb_v_artstar.fits',Mrk1383_v_art
Mrk1383_hv_art=noise_maskh(Mrk1383_v_art ,noisemodel=noisemodel)
writefits, 'Mrk1383_comb_hv_artstar_sn5.fits',Mrk1383_hv_art