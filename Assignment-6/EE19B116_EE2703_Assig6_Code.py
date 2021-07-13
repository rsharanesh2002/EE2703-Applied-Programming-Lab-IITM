'''
EE2703 Applied Programming Lab
Submission for Assignment-6
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import *
import sys
import pandas as pd

if len(sys.argv)==7:
    n=sys.argv[0]  # spatial grid size.
    M=sys.argv[1]    # number of electrons injected per turn.
    nk=sys.argv[2] # number of turns to simulate.
    u0=sys.argv[3]  # threshold velocity.
    p=sys.argv[4] # probability that ionization will occur
    Msig=sys.argv[5] # standard deviation for the random generation

else:
	n=100 
	M=5
	nk=100
	u0=5
	p=0.25		
	Msig=2

## Creating the vectors and initialize them to zero 
xx = zeros((n*M))
u = zeros((n*M))
dx = zeros((n*M))
ones = ones((n*M))

## Creating lists for the Intensitys, postion and velocity
I = []
X = []
V = []

## Iterating through the given number of iterations
for k in range(1,nk):
	ii=where(xx>0) ## get the indices where electrons number is more than zero
	dx[ii]=u[ii]+0.5 ## increase the displacement

	xx[ii]+=dx[ii] ## increase the position
	u[ii]+=1 ## increase the velocity

	hit_anode=where(xx[ii]>n) ## contains the indices of the electrons that reached anode
	xx[ii[0][hit_anode]]=u[ii[0][hit_anode]]=dx[ii[0][hit_anode]]=0 ## setting position,velocities,displacements to zero
    
	kk=where(u>=u0) ## get the indices of energetic electrons that suffer collision
	ll=where(rand(len(kk[0]))<=p)
	kl=kk[0][ll]
	u[kl]=0 ## reset the velocity to zero after collision

	rho=rand(len(kl)) ## get a random number
	xx[kl]=xx[kl]-dx[kl]*rho ## find the actual value of x where it collides
	I.extend(xx[kl].tolist()) ## Extending the position of electrons to Intensity list

	m=int(rand()*Msig+M) ## get the random number of new electrons to be added

	vacant=where(xx==0) ## get the vacant spaces where electrons can be injected
	re_fill=(min(n*M-len(vacant),m)) ## to have a check on if there are no empty spaces
	xx[vacant[:re_fill]]=1 ## inject the new electrons
	u[vacant[0][:re_fill]]=0 ## set the velocity of injected electrons as zero
	dx[vacant[0][:re_fill]]=0 ## set the displacement of injected electrons as zero

	X.extend(xx.tolist()) ## Extending the position of electrons to Position list
	V.extend(u.tolist()) ## Extending the velocity of electrons to Velocity list

## Plotting the population plot of the electrons
figure(1)
hist(X,bins=arange(0,n+1,0.5),rwidth=0.7,color='g')
title(r'Population plot of electrons for the case of $u_0=$%f and p=%f'%(u0,p))
xlabel(r'$x$')
ylabel('Number of electrons')
show()

## Plotting the Light Intensity plot of the electrons
figure(2)
hist(I,bins=arange(0,n+1,0.5),rwidth=0.7,color='r')
title(r'Light Intensity for the case of $u_0=$%f and p=%f'%(u0,p))
xlabel(r'$x$')
ylabel('Intensity')
show()

## Plotting the electron phase plot of the electrons
figure(3)
plot(X,V,'bo')
title(r'Electron Phase Space for the case of $u_0=$%f and p=%f'%(u0,p))
xlabel(r'$x$')
ylabel(r'Velocity-$v$')
show()

## Convert the histogram of intensity to a tabular form
a,bins,c=hist(I,bins=arange(1,100))
xpos=0.5*(bins[0:-1]+bins[1:])
d={'xpos':xpos,'count':a}
p=pd.DataFrame(data=d)
print("Intensity data:")
print(p)