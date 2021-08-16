;+
; NAME:
;   NOISE_MASKV
;
; PURPOSE:
;
;   Some Gemini MICHELLE data suffers from a VERTICAL noise banding. This function 
;   models that noise and subtracts it off, returning a cleaned image. One can also 
;   return the noise model used in the subtraction. This function ONLY corrects these 
;   regular horizontal noise patterns. THIS FUNCTION ONLY WORKS IF A MAJORITY OF THE 
;   FIELD IS SKY EMISSION. If the field is taken up mostly by extended source emission,
;   then this function WILL LIKELY NOT WORK.
;
; AUTHOR:
;
;   James M. De Buizer
;   Gemini Observatory
;   Southern Operations Center
;   E-mail: jdebuizer@gemini.edu
;
; PROCEDURE:
;
;   Annotated in program.
;
; USAGE:
;
;  The calling procedure for this function at the IDL prompt will 
;  look something like this:
;
;      image=noise_maskv(array [,noisemodel=noisemodel])
;
; INPUT KEYWORD PARAMETERS:
;
;  array  - is the two-dimensional IDL array of the image containing the
;           horizontal noise pattern
;
; OPTIONAL INPUT PARAMETERS:
;
;  noisemodel - this will return the horizontal noise model that was subtracted off
;
; OUTPUT KEYWORD PARAMETERS
;
;  image  - is the final image after applying a correction for the horizontal
;           noise
;
; MAJOR FUNCTIONS and PROCEDURES:
;
;   None.
;
; MODIFICATION HISTORY:
;
;   Written by: J.M. De Buizer, Gemini Observatory, 2003 Oct.
;   October, 2006 - Modified by J.M. De Buizer:
;       Added noise model smoothing function so that final images do not contain
;       large numbers of exactly zero-value pixels
;   February, 2007 - Modified by J.M. De Buizer (Ver. 5):
;       Removed dependency on WDISP
;       Routine now passive rather than active
;       User can now output noise model using the optional "noisemodel" keyword 
;-

function noise_maskv, file, noisemodel=noisemodel

if not keyword_set(noisemodel)  then noisemodel = 0

; Chop the image up into 12 20x320 pixel subarrays.
mask=make_array(320, 20, 12, value=0.0)

for i=0, 11 do mask[*,*,i]=file[*, (i+(i*19)):(i+((i+1)*19))]

;Take the pixel by pixel median of each of the 12 subarrays to create a median 12x320 array.
t=make_array(320, 20, value=0.0)

for col=0,319 do begin
   for row=0, 19 do begin
     t[col,row]=median(mask[col,row,*])
  endfor
endfor

; Replicate this median array into a 320x240 array. This is the noise model for the image.
mask_almost_final=[[t],[t],[t],[t],[t],[t],[t],[t],[t],[t],[t],[t]]

; Apply a 1-pixel guassiian smooth so that there are no exactly zero values in final image
kern=replicate(0.0,320.0,240.0)
sig=1.0/(2.0*1.177)
sig2=sig*sig
i=indgen(320.0)
dx2=(i-159.75)^2.0
for j = 0, 240.0-1 do kern[i,j] = 1.0*exp( -(dx2 + (j-119.75)^2.0)/(2.0*sig2) )
f_im1=fft(mask_almost_final,1)
f_im2=fft(shift(kern, 160, 120),1)
noisemodel=float(fft(f_im1*f_im2,-1))

;Return cleaned image and noise model, if requested

return, file-noisemodel

end


























