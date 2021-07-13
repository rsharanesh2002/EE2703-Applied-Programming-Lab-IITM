'''
EE2703 Applied Programming Lab
Submission for End-Semester Examination
Name: Sharanesh R
Roll Numer: EE19B116
'''

# Importing all functions from pylab
from pylab import *

# Defining constants
N = 100 # Number of sections on the loop
a = 10 # Radius of the wire Looping

x=linspace(-1,1,3) # x grid is -1,0,1
y=linspace(-1,1,3) # y grid is -1,0,1
z=linspace(1,1000,1000) # defining 1000 points along the z-axis
X,Y,Z=meshgrid(x,y,z) # defining meshgrid to access the coordinates

r = zeros((3,3,1000,3)) # Matrix that spans over the entire volume of observation
# Stacking up the meshgrid coordinates 
r[:,:,:,0] = X 
r[:,:,:,1] = Y
r[:,:,:,2] = Z

phi = linspace(0,2*pi,N+1)[:-1] # The angular points on the loop
r_ = a*(c_[cos(phi),sin(phi),zeros(N)]) # These are the coordinates of the points on the loop
# Corresponds to the rl' vector given in the code

# Visualising the points on the closed wire loop
figure('Figure-0') # Starting a new figure
scatter(r_[:,0],r_[:,1],color='red') # Making scatter plot of all the points
xlabel(r"x $\rightarrow$")
ylabel(r"y $\rightarrow$")
title('Scatter plot of loop wire elements')
grid()
show()

# Defining the Current elements as given in the question (multiple of cos(phi))
## For Symmetric current flow case (given question)
I =  4*pi*(c_[-1*cos(phi)*sin(phi),cos(phi)*cos(phi),zeros(N)])

## For Anti-symmetric current flow case
# I =  4*pi*(c_[-1*abs(cos(phi))*sin(phi),abs(cos(phi))*cos(phi),zeros(N)])

## For static current flow case (static in current and time)
# I =  4*pi*(c_[-1*sin(phi),cos(phi),zeros(N)])

# Visualising the current elements at the points on the closed wire loop
figure('Figure-1') # Starting a new figure
quiver(r_[:,0],r_[:,1],I[:,0],I[:,1],color='blue',label='current') # Making a quizer plot of current elements
xlabel(r"x $\rightarrow$")
ylabel(r"y $\rightarrow$")
title('Quiver plot of current in the wire elements on X-Y plane')
legend()
grid()
show()

# dl is defined as the length infinitesmal small loop element, it's along the axial angle direction,
# magnitude of it is the small step angle multiplied by radius
dl = (2*pi*10/100)*c_[-sin(phi),cos(phi),zeros(N)]
dl_x=dl[:,0].reshape((100,))
dl_y=dl[:,1].reshape((100,))

# Defining 'A' vector that stores the magnetic field at all the points in volume of observation
A = zeros((3,3,1000,2),dtype='complex128') 

# Defining the calc(l) function that computes the norm and returns the summation term for each value of 'l'
def calc(l):
	Rl = norm(r-r_[l],axis=-1) # Computing the norm
	### Vector Potential for symmetric and non-static 
	A_x_ = (cos(phi[l])*exp(-0.1j*Rl)*dl_x[l]/Rl) # Computing the magnetic potential along x-axis
	A_y_ = (cos(phi[l])*exp(-0.1j*Rl)*dl_y[l]/Rl) # Computing the magnetic potential along y-axis

	### Vector Potential for symmetric and static in time
	# A_x_ = (cos(phi[l])*dl_x[l]/Rl) # Computing the magnetic potential along x-axis
	# A_y_ = (cos(phi[l])*dl_y[l]/Rl) # Computing the magnetic potential along y-axis

	### Vector Potential for anti-symmetric and non-static 
	# A_x_ = (abs(cos(phi[l]))*exp(-0.1j*Rl)*dl_x[l]/Rl) # Computing the magnetic potential along x-axis
	# A_y_ = (abs(cos(phi[l]))*exp(-0.1j*Rl)*dl_y[l]/Rl) # Computing the magnetic potential along y-axis

	### Vector Potential for anti-symmetric and static in time
	# A_x_ = (abs(cos(phi[l]))*dl_x[l]/Rl) # Computing the magnetic potential along x-axis
	# A_y_ = (abs(cos(phi[l]))*dl_y[l]/Rl) # Computing the magnetic potential along y-axis

	### Vector Potential static in both time and space
	# A_x_ = (dl_x[l]/Rl) # Computing the magnetic potential along x-axis
	# A_y_ = (dl_y[l]/Rl) # Computing the magnetic potential along y-axis

	return Rl, A_x_, A_y_

# Looping through all the loop points and finding the total magnetic potential
for i in range(N):
	Rl, A_x, A_y = calc(i)
	A[:,:,:,0] += A_x
	A[:,:,:,1] += A_y

# Computing 'B' magnetic field as an approximated sum using the magnetic potentials around the neighbouring points
B = (A[1,2,:,1]-A[2,1,:,0]-A[1,0,:,1]+A[0,1,:,0])/4

# Visualising the variation of magnetic field along the z-axis
figure('Figure-2') # Starting a new figure
loglog(z,abs(B),color='blue',label=r'$Magnetic field |B_z(z)|$')
xlabel(r"z $\rightarrow$")
ylabel(r"$|B_z(z)| \rightarrow$")
title("Log-log plot of magnetic field along z-axis")
legend()
grid()
show()

figure('Figure-3') # Starting a new figure
plot(z,abs(B),color='blue',label=r'$Magnetic field |B_z(z)|$')
xlabel(r"z $\rightarrow$")
ylabel(r"$|B_z(z)| \rightarrow$")
title("Magnetic field along z-axis")
legend()
grid()
show()

# Performing the Least squares Estimation and seeking the coefficients
# Fitting B = c*(z^b)
b,log_c = lstsq(c_[log(z),ones(1000)],log(abs(B)),rcond=None)[0]
print("Estimated Coefficient 'b': ",b)
print("Estimated Coefficient 'c': ",exp(log_c))

# Log-log plot of the actual and estimated magnetic fields
figure('Figure-4') # Starting a new figure
loglog(z,abs(B),label='Actual',color='green')
loglog(z,exp(log_c)*(z**b),label='Estimated using fit',color='red')
xlabel(r"z $\rightarrow$")
ylabel(r"$|B_z(z)| \rightarrow$")	
title(r"Comparison of Actual and Estimated Magnetic field $|B_z(z)|$ (Log-log)")
legend()
grid()
show()

# Linear scale plot of the actual and estimated magnetic fields
figure('Figure-5') # Starting a new figure
plot(z,abs(B),label='Actual',color='green')
plot(z,exp(log_c)*(z**b),label='Estimated using fit',color='red')
xlabel(r"z $\rightarrow$")
ylabel(r"$|B_z(z)| \rightarrow$")
title(r"Actual and Estimated Magnetic field $|B_z(z)|$")
legend()
grid()
show()