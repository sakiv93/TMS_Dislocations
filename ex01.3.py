import numpy as np
import matplotlib.pyplot as plt
b=0.5
def screw_stress_xy(x,y,x0,y0):
    return((-(y-y0)/b)/(2*np.pi*((x-x0)/b)**2+((y-y0)/b)**2))
x0=0
y0=0
#Co-ordinates of plot
x_start=-4
x_end=10
y_start=0
y_end=12
# Number of little rectangles
no_pixels_x=10
no_pixels_y=10
#pixel size
dx=(x_end-x_start)/no_pixels_x
dy=(y_end-y_start)/no_pixels_y
#co-ordinates of vertices.
xv=np.linspace(x_start,x_end,no_pixels_x+1)
yv=np.linspace(y_start,y_end,no_pixels_y+1)
#center points of pixels
xc=np.linspace(x_start+(dx/2),x_end-(dx/2),no_pixels_x)
yc=np.linspace(y_start+(dy/2),y_end-(dy/2),no_pixels_y)
#create 2D co-ordinate array
xv_2d,yv_2d=np.meshgrid(xv,yv)
xc_2d,yc_2d=np.meshgrid(xc,yc)
#get distance values for center points
values=screw_stress_xy(xc_2d,yc_2d,x0,y0)
print(xc_2d,yc_2d)
plt.pcolormesh(xv_2d,yv_2d,values)
plt.colorbar()
plt.show()