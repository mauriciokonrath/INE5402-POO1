# -*- coding: utf -8 -*
cv, ce, cs, fv, fe, fs = input().split()
cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

c = cv * 3 + ce  
f = fv * 3 + fe  

if c == f:
       
    if cs > fs:
        print('C')
    elif cs < fs:
        print('F')
    elif cs == fs:
        print('=')
     
elif c > f:
    print ('C')
    
elif c < f:
    print('F')
  

    

    
