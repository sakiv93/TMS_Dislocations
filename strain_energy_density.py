import numpy as np 
import matplotlib.pyplot as plt 


#Scew strain energy function definition.
def screw_strain_energy_density(x,y,burgers_vector,shear_modulus):
    return shear_modulus*burgers_vector**2/(8*np.pi**2*(x**2+y**2))

#System Definition
burgers_vector=0.25e-9      #m
shear_modulus=120e9         #Pa
xv=burgers_vector*np.linspace(-20,20,30)
yv=burgers_vector*np.linspace(-20,20,30)
xx,yy=np.meshgrid(xv,yv)

#Calling energy function.
energy_density=screw_strain_energy_density(xx,yy,burgers_vector,shear_modulus)

#plottting
#cmap: For contour color range
im=plt.imshow(energy_density,origin='lower',vmin=0,vmax=energy_density.max()/10.0,cmap='viridis')
plt.colorbar(im)
plt.show()

core_radius=2.5*burgers_vector
dx=burgers_vector
dy=burgers_vector
radii_R=burgers_vector*np.linspace(5,200,40)


energys=[]
for radius in radii_R:
    xx,yy=np.meshgrid(np.arange(-radius,radius,dx),np.arange(-radius,radius,dy))
    energy_density=screw_strain_energy_density(xx,yy,burgers_vector,shear_modulus)
    energy_density=np.where((xx**2+yy**2)**0.5>core_radius,energy_density,0.0)
    energys.append(energy_density.sum()*dx*dy)

#fig,ax=plt.subplots()
#ax.plot(radii_R/burgers_vector,np.log(radii_R/core_radius)/(4*np.pi),'-',lw=2,label=r'$Gb^2\log(R/r_0)$',c='C1')
#ax.plot(radii_R/burgers_vector,np.array(energys)/(shear_modulus*burgers_vector**2),lw=2,marker='o',label='nemrical')
#ax.set(xlabel=r'radius $R$ $[b]$',ylabel=r'Energy $E$ $[Gb^2]$',ylim=(0,ax.get_ylim()[1]))
#ax.legend()
#plt.show()