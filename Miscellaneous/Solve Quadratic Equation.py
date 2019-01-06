a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
import math
if b**2-4*a*c<0:
    print ('This equation has no solution.')
else:
    x1=-b+math.sqrt(b**2-4*a*c)
    x2=-b-math.sqrt(b**2-4*a*c)
    print ('x1=',x1)
    print ('x2=',x2)
