PRO artificial_star,FWHM,Flux,art_star

;+
; NAME:
;       ARTIFICIAL_STAR
; PURPOSE:
;       To create an artificial star using a MOFFAT profile
; CALLING SEQUENCE:
;       artificial_star,FWHM,Flux,art_star
;
; INPUTS/OUTPUT:
;       FWHM    - Full-Width Half at Maximum (FWHM) in pixels of the 
;                 artificial star.
;                 
;       Flux 	- Total flux of the artificial star. The artificial star
;                 will have the flux input desired by the user. 
;
;		art_star - Output with the artificial star
;                  
;                 
; PROCEDURE:
;       An artificial star using a MOFFAT function with 1 free parameter, FWHM,   
;       is modeled. Note that the beta parameter of the Moffat function is 
;		assumed to be the typical value, 4.765.
; MODIFICATION HISTORY:
;       Written by Enrique Lopez-Rodriguez, University of Texas at San Antonio, 
;		28 August 2013.


r = FINDGEN(11)

;Typical value of beta is 4.765 based on Trujillo et al. (2001), MNRAS, 328, 977
bbeta = 4.765

alpha = FWHM/(2*SQRT(2^(1/bbeta)-1))

I_moffat = (1+((r-5)/alpha)^2)^(-bbeta)

I_moffat_2D = I_moffat # TRANSPOSE(I_moffat)

art_star = Flux * (I_moffat_2D/TOTAL(I_moffat_2D))

END