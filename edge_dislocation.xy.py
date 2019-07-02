import numpy as np
import matplotlib.pyplot as plt
def edge_stress_xy(x,y,shear_modulus,burgers_vector,poissons_ratio):
    D=shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    stress_xy=D*x*(x**2-y**2)/(x**2+y**2)**2
    return stress_xy
def edge_stress_xx(x,y,shear_modulus,burgers_vector,poissons_ratio):
    D=shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    stress_xx=-D*y*(3*x**2+y**2)/(x**2+y**2)**2
    return stress_xx
def edge_stress_yy(x,y,shear_modulus,burgers_vector,poissons_ratio):
    D=shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    stress_yy=D*y*(x**2-y**2)/(x**2+y**2)**2
    return stress_yy
def edge_stress_zz(x,y,shear_modulus,burgers_vector,poissons_ratio):
    stress_zz=poissons_ratio*(edge_stress_xx(x,y,shear_modulus,burgers_vector,poissons_ratio)+edge_stress_yy(x,y,shear_modulus,burgers_vector,poissons_ratio))
    return stress_zz
shear_modulus=90e9 # Pa
burgers_vector=0.25e-9 #m
poissons_ratio=0.3
#Co-ordinates of plot
x_start=-100e-9
x_end=100e-9
y_start=-100e-9
y_end=100e-9
# Number of little rectangles
no_pixels_x=50
no_pixels_y=50
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
x0=50e-9
y0=50e-9


#get stress values for center points
##stress=edge_stress_xy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
#plt.pcolormesh(xv_2d,yv_2d,stress)
#fig,ax=plt.subplots(figsize=(15,10))  #to set figsize or zoom
##im=plt.imshow(stress,origin='lower',extent=(x_start,x_end,y_start,y_end),aspect='equal',vmin=-0.1e9,cmap='RdBu')
##plt.colorbar();
#For lines display
##cs=plt.contour(xc_2d,yc_2d,stress,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
#For values display
##plt.clabel(cs, fmt='%1.1e'); 


sigma_xx=edge_stress_xx(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
sigma_yy=edge_stress_yy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
sigma_zz=edge_stress_zz(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
sigma_xy=edge_stress_xy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
fig,ax=plt.subplots(nrows=2,ncols=3,figsize=(15,10))
print(sigma_xx)
#Dictonories
im_kwargs={'origin':'lower','extent':(x_start,x_end,y_start,y_end),'aspect':'equal','vmin':-0.1e9,'cmap':'YlOrRd_r'}
ax[0][0].imshow(sigma_xx, **im_kwargs)
cs=ax[0][0].contour(xc_2d,yc_2d,sigma_xx,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[0][0].clabel(cs, fmt='%1.1e'); 
ax[0][1].imshow(sigma_yy, **im_kwargs)
cs=ax[0][1].contour(xc_2d,yc_2d,sigma_yy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[0][1].clabel(cs, fmt='%1.1e'); 
ax[0][2].imshow(sigma_zz, **im_kwargs)
cs=ax[0][2].contour(xc_2d,yc_2d,sigma_zz,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[0][2].clabel(cs, fmt='%1.1e'); 
ax[1][0].imshow(sigma_xy, **im_kwargs)
cs=ax[1][0].contour(xc_2d,yc_2d,sigma_xy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[1][0].clabel(cs, fmt='%1.1e'); 


fig,ax=plt.subplots(ncols=3,figsize=(5,3))
sigma_xy_0=edge_stress_xy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
sigma_xy_1=edge_stress_xy(xc_2d-x0,yc_2d-y0,shear_modulus,burgers_vector,poissons_ratio)
ax[0].imshow(sigma_xy_0, **im_kwargs)
cs=ax[0].contour(xc_2d,yc_2d,sigma_xy_0,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[0].clabel(cs, fmt='%1.1e');
ax[1].imshow(sigma_xy_1, **im_kwargs)
cs=ax[1].contour(xc_2d,yc_2d,sigma_xy_1,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[1].clabel(cs, fmt='%1.1e');
ax[2].imshow(sigma_xy_0+sigma_xy_1, **im_kwargs)
cs=ax[2].contour(xc_2d,yc_2d,sigma_xy_0+sigma_xy_1,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
ax[2].clabel(cs, fmt='%1.1e');
#sigma_xx=edge_stress_xy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
##fig,ax=plt.subplots(nrows=2,ncols=3,figsize=(15,10))
#Dictonories
##im_kwargs={'origin':'lower','extent':(x_start,x_end,y_start,y_end),'aspect':'equal','vmin':-0.1e9,'cmap':'RdBu'}
#either of two
#ax[0][0].imshow(sigma_xx,origin='lower',extent=(x_start,x_end,y_start,y_end),aspect='equal',vmin=-0.1e9,cmap='RdBu')
#ax[0][0].imshow(sigma_xx, **im_kwargs)
#ax[0][1].imshow(sigma_yy, **im_kwargs)
#plt.colorbar()
##ax[0][0].set(xlabel='x[m]');
##ax[0][0].set(xlabel='x[m]',ylabel='y [m]');
#plt.show()
#fig, ax=plt.subplots(figsize=(10,10))
##fig, ax=plt.subplots(ncols=3, figsize=(20,7))
##sigma_xy_0=edge_stress_xy(xc_2d,yc_2d,shear_modulus,burgers_vector,poissons_ratio)
##sigma_xy_1=edge_stress_xy(xc_2d-x0,yc_2d-y0,shear_modulus,burgers_vector,poissons_ratio)
##ax[0].imshow(sigma_xy_0, **im_kwargs);
##ax[1].imshow(sigma_xy_1, **im_kwargs);
##ax[2].imshow(sigma_xy_0+sigma_xy_1, **im_kwargs);
plt.show()