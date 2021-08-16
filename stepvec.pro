FUNCTION stepvec,min,max,step
n=FLOOR(((max-min)/step)+1.0)
return,min+LINDGEN(n)*step
END
