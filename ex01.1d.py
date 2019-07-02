def f(x,y,x0,y0):
    return(((x-x0)**2+(y-y0)**2)**0.5)
import numpy as np
x=np.linspace(-2,2,5)
y=np.linspace(0,3,4)
x0=1
y0=2
xx,yy=np.meshgrid(x,y)
print(f(xx,yy,x0,y0))