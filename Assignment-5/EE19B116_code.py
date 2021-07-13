'''
EE2703 Applied Programming Lab
Submission for Assignment-5 
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import*
import mpl_toolkits.mplot3d.axes3d as p3

## Setting the default parameters
Nx=25 # size along x
Ny=25 # size along y
radius=0.35 # radius of central lead
Niter=1500 # number of iterations to perform

## Getting the parameters from command line
if(len(sys.argv)>1):
    Nx = int(sys.argv[1])
    Ny = int(sys.argv[2])
    Niter = int(sys.argv[3])

## Initializing the potential array
phi = zeros((Nx,Ny))
x = linspace(-0.5, 0.5, Nx)
y = linspace(-0.5, 0.5, Ny)

X,Y=meshgrid(x,-y) ## Setting a meshgrid

## Finding the points of the square where less than a unit circle and making the potential at those points as 1V.
nodes_1_volt = where(square(X)+square(Y) <= radius**2)
phi[nodes_1_volt] = 1.0

## Creating a contour plot of the initial potential
figure('Figure-1')
scatter(x[nodes_1_volt[0]], y[nodes_1_volt[1]], color='r', label=r'$V = 1V$ region')
contPlot = contourf(X, Y, phi, cmap=cm.jet)
axes().set_aspect('equal')
title(r'Contour Plot of the potential $\phi$')
colorbar()
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
show()

## Iteratively updating the potential and simultanously applying the boundary condition and computing the error.
iterations = []
error = []
for k in range(Niter):
    oldphi = phi.copy() ## Creating a copy of the potential to find the error.

    ## Updating the potential as the average of the points surrounding it.
    phi[1:-1, 1:-1] = 0.25*(phi[1:-1, 0:-2]+phi[1:-1, 2:]+phi[0:-2, 1:-1]+phi[2:, 1:-1]) 

    ## Applying the boundary condition at the edges of the square
    phi[1:-1, 0] = phi[1:-1, 1]
    phi[1:-1, -1] = phi[1:-1, -2]
    phi[0, :] = phi[1, :]

    ## Setting the potential as 1V to the electrode region
    phi[nodes_1_volt] = 1.0

    ## Appending the error at each iteration
    error.append(abs(phi-oldphi).max())
    iterations.append(k)

## Plotting a semilog plot of the error computed
figure('Figure-2')
semilogy(iterations, error, 'b', label='Error')
semilogy(iterations[::50], error[::50], 'ro', label='every 50th point')
title('Semilog plot of error')
xlabel(r'$Iterations\rightarrow$')
ylabel(r'$Error$')
legend()
show()

## Plotting a loglog plot of the error computed
figure('Figure-3')
loglog(iterations, error, 'b', label='Error')
loglog(iterations[::50], error[::50], 'ro', label='every 50th point')
title('Loglog plot of error')
xlabel(r'$Iterations\rightarrow$')
ylabel(r'$Error$')
legend()
show()

## Performing the least squares fit to the error and the iterations
all_fit_coefficients = lstsq(c_[ones(Niter),arange(Niter)],log(error),rcond=None)[0]
all_fit_estimated = dot(c_[ones(Niter),arange(Niter)],all_fit_coefficients)

aft500_fit_coefficients = lstsq(c_[ones(Niter-501),arange(501,Niter)],log(error[501:]),rcond=None)[0]
aft500_fit_estimated = dot(c_[ones(Niter-501),arange(501,Niter)],all_fit_coefficients)

print('Least square fit with all the error points returned, A = {} and  B = {} from Fit 1'.format(exp(all_fit_coefficients[0]), all_fit_coefficients[1]))
print('Least square fit with error points after 500 iterations returned, A = {} and B = {} from Fit 2'.format(exp(aft500_fit_coefficients[0]), aft500_fit_coefficients[1]))

cummulErr = []
for n in range(1, Niter):
    cummulErr.append((exp(all_fit_coefficients[0]/exp(all_fit_coefficients[1]))*exp(all_fit_coefficients[1]*(n+0.5))))

figure('Figure-4')
semilogy(iterations[1:], cummulErr, 'b', label='Cummulative error')
semilogy(iterations[1::50], cummulErr[::50], 'ro', label='every 50th point')
title('Semilog plot of Cummulative Error')
xlabel(r'$Iterations\rightarrow$')
ylabel(r'$Cummulative Error \rightarrow$')
legend()
show()

figure('Figure-5')
loglog(iterations[1:], cummulErr, 'b', label='Cummulative error')
loglog(iterations[1::50], cummulErr[::50], 'ro', label='every 50th point')
title('Semilog plot of Cummulative Error')
xlabel(r'$Iterations\rightarrow$')
ylabel(r'$Cummulative Error \rightarrow$')
legend()
show()

## Plotting a semilog plot of the actual error computed along with the best fitted error
figure('Figure-6')
semilogy(iterations[::50], exp(all_fit_estimated[::50]), 'ro', label='fit using all points')
semilogy(iterations[501::50], exp(aft500_fit_estimated[::50]), 'go', label='fit after 500 points')
semilogy(iterations, error, 'b', label='actual error')
title('Actual error vs Error obtanied by fitting')
xlabel(r'$Iterations\rightarrow$')
ylabel(r'$Error$')
legend()
show()

## Plotting a 3D Surface plot of the potential
fig7 = figure('Figure-7')
ax = p3.Axes3D(fig7)
title(r'3D surface plot of the potential $\phi$')
surfacePlot = ax.plot_surface(X,Y,phi, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel(r'$X\rightarrow$')
ax.set_ylabel(r'$Y\rightarrow$')
ax.set_zlabel(r'$\phi\rightarrow$')
show()

## Plotting the updated Contour plot of potential
figure('Figure-8')
scatter(x[nodes_1_volt[0]], y[nodes_1_volt[1]], color='r', label=r'$V = 1V$ region')
contourf(X, Y, phi, cmap=cm.jet)
axes().set_aspect('equal')
colorbar()
title(r'Updated Contour Plot of the potential $\phi$')
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
show()

## Computing the current from the potential
Jx = zeros((Nx,Ny))
Jy = zeros((Nx,Ny))

Jx[1:-1, 1:-1] = 0.5*(phi[1:-1, 0:-2] - phi[1:-1, 2:])
Jy[1:-1, 1:-1] = 0.5*(phi[2:, 1:-1] - phi[0:-2, 1:-1])

## Plotting the vector plot of the current
figure('Figure-9')
scatter(x[nodes_1_volt[0]], y[nodes_1_volt[1]], color='r', label=r'$V = 1V$ region')
axes().quiver(X,Y,Jx,Jy)
axes().set_title('Vector Plot of current flow')
xlabel(r'$X\rightarrow$')
ylabel(r'$Y\rightarrow$')
legend()
show()

# Intitialize the temperature matrix to zeros at all points
Temp=zeros((Nx,Ny))
Temp[nodes_1_volt]=300 #The electrode region is at 300K
Temp[-1,:]=300 #The boundary region also lies at 300K

kappa=1  #Thermal conductivity of copper
sigma=1  #Electrical conductivity of copper
constant_term= Jx[1:-1,1:-1]**2+Jy[1:-1,1:-1]**2/(sigma*kappa) ##The constant term while solving the heat equation

for k in range(Niter):
    ## Iteratively updating the Temperature as the average of all points around it
    Temp[1:-1,1:-1]=0.25*((Temp[1:-1,0:-2]+Temp[1:-1,2:]+Temp[0:-2,1:-1]+Temp[2:,1:-1]))+constant_term

    ## Updating the boundaries or the edges
    Temp[1:-1,0]=Temp[1:-1,1] 
    Temp[1:-1,-1]=Temp[1:-1,-2] 
    Temp[0,:]=Temp[1,:] 

    ## Setting the temperature as 300K to the electrode region
    Temp[nodes_1_volt]=300

## Plotting a 3D Surface plot of the temperature
fig10 = figure('Figure-10')
ax = p3.Axes3D(fig10)
title('3D surface plot of the Temperature')
surfacePlot = ax.plot_surface(X,Y,Temp, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel(r'$X\rightarrow$')
ax.set_ylabel(r'$Y\rightarrow$')
ax.set_zlabel(r'$T\rightarrow$')
show()