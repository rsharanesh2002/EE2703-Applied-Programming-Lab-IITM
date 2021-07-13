'''
EE2703 Applied Programming Lab
Submission for Assignment-3	
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import *
import scipy.special as sp
import numpy as np
import sys

# Trying to load the content of the file
try:
	raw_data = np.loadtxt("fitting.dat", delimiter=" ", unpack=True)
except Exception:
	sys.exit("Error: The file named 'fitting.dat' is not found")

time_stamps = raw_data[0] #getting the time stamps from the loaded data
data = raw_data[1:] #getting the actual data from the loaded data


t = linspace(0,10,101) #creating the array of the time values
sigma = logspace(-1,-3,9) #creating the array of standard deviation values
sigma = around(sigma,3) #round off the standard deviation values

# Defing the function g(t,A,B) to get the function value
def g(t, A, B):
    return A*sp.jn(2,t) + B*t

figure(0) # Starting a new plot/figure
for i in range(len(data)):
	plot(t,data[i],label='$\sigma_{} = {}$'.format(i, sigma[i])) # Plotting the functions with added noise


true_value = g(t, 1.05, -0.105) #Generating the true value of the plot
plot(t, true_value, label='True Value', color='black') # Plotting the true value

xlabel(r'$t \rightarrow$') 
ylabel(r'$f(t)+noise \rightarrow$')
title('Data to be fitted to theory')
legend()
grid()
show() # Displaying the figure/plot


figure(1) # Starting a new plot/figure
plot(t, true_value, label=r'$f(t)$', color='black') # Plotting the true value
errorbar(t[::5], data[0][::5], 0.1, fmt='or', label='Error Bar') # Making errorbar plot

xlabel(r'$t \rightarrow$')
ylabel(r'$f(t) \rightarrow$')
title(r'Errorbar plot for $\sigma_=0.10$ and the exact function')
legend()
grid()
show() # Displaying the figure/plot


# Creating column vector for least-squares estimation
A0 = 1.05
B0 = -0.105
j2_column = sp.jn(2,t)
M = c_[j2_column, t] #Creating the M matrix
p = array([A0, B0]) #Creating the p matrix

if array_equal(dot(M,p),g(t,A0,B0)): #Checking if the two matrices are equal
	print('Q6: The two vectors are equal')
else:
	print('Q6: The two vectors aren\'t equal')


A = array([0.1*i for i in range(21)]) #Creating the matrix A
B = array([-0.2+0.01*i for i in range(21)]) #Creating the matrix B
epsilon_error = empty((len(A), len(B))) #Creating an empty matrix for storing the mean squared error

for i in range(len(A)):
    for j in range(len(B)):
            epsilon_error[i][j] = mean(square(data[0][:]-g(t[:], A[i], B[j])))
            #Computing the mean squared error between the actual data and the assumed model


figure(2) # Starting a new plot/figure
# Contour plot of mean squared error with A and B on axes
contour_plot=contour(A,B,epsilon_error,levels=20)
clabel(contour_plot, inline=1, fontsize=10)
plot([1.05], [-0.105], 'ro') #Plotting the exact loxation of the minima (which is A=1.05, B=-0.105)	
# Annotating the graph with exact location of the minima 
annotate("Exact Location", (1.05, -0.105), xytext=(-50, -40), textcoords="offset points", arrowprops={"arrowstyle": "->"})

xlabel(r'$A \rightarrow$')
ylabel(r'$B \rightarrow$')
title('contour plot of $\epsilon_{ij}$')
show() # Displaying the figure/plot


p, *residuals = lstsq(M,true_value,rcond=None) # Performing the least square estimation for the true value function


figure(3) # Starting a new plot/figure
#p_err = empty((9, 2))
err_in_A = empty(9)
err_in_B = empty(9)
# Performing the least square estimation for the noisy data of the 'fitting.dat' file
for k in range(len(data)):
    p_err, *residuals = lstsq(M, data[k], rcond=None) 
    err_in_A[k] = square(p_err[0] - A0)
    err_in_B[k] = square(p_err[1] - B0)
	# Calculating the mean squared error in A and error in B for each least square estimation

# Plotting the error in A and B versus the standard deviation 
plot(sigma, err_in_A, 'o--', label='$A_{err}$')
plot(sigma, err_in_B, 'o--', label='$B_{err}$')

xlabel(r'Noise standard deviation $\rightarrow$')
ylabel(r'MS error $\rightarrow$')
title("Variation of error with noise")
legend()
grid()
show() # Displaying the figure/plot

	
figure(4) # Starting a new plot/figure
# Plotting error in A and B versus the standard deviation in a log-log scale
loglog(sigma, err_in_A, 'ro', label="$A_{err}$")
errorbar(sigma, err_in_A, std(err_in_A), fmt='ro')
loglog(sigma, err_in_B, 'bo', label="$B_{err}$")
errorbar(sigma, err_in_B, std(err_in_B), fmt='bo')

xlabel(r'$\sigma_{n} \rightarrow$')
ylabel(r'MS error $\rightarrow$')
title("Variation of error with noise")
legend(loc='upper right')
grid()
show() # Displaying the figure/plot