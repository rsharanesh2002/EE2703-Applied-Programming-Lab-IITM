'''
EE2703 Applied Programming Lab
Submission for Assignment-4 
Name: Sharanesh R
Roll Numer: EE19B116
'''

from scipy.integrate import quad
from pylab import *

# Function that returns the value of cos(cos(x))
def func_coscosx(x):
    return cos(cos(x))

# Function that returns the value of exp(x)
def func_exp(x):
    return exp(x)

# Function that returns the integrand for getting the coeffcient of cos(n*x)
def func_cos_coeff(x, k, f):
    return f(x)*cos(k*x)

# Function that returns the integrand for getting the coeffcient of sin(n*x)
def func_sin_coeff(x, k, f):
    return f(x)*sin(k*x)

x = linspace(-2*pi, 4*pi, 1201) # A vector set from -2pi to 4pi 
x = x[:-1] # we exclude the last value 4pi
k = linspace(0, 25, 26) # A vector set to make the x-axis for the plot of coefficients in semilog scale.

figure('Figure-1') # Starting a new plot/figure
plot(x, func_coscosx(x), 'r', label='Actual Function')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'$cos(cos(x))$ Function value')
xlabel(r'$x \rightarrow$') 
ylabel(r'$cos(cos(x)) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-1.1') # Starting a new plot/figure
plot(x, func_coscosx(x), 'r', label='Actual Function')
plot(x, func_coscosx(x%(2*pi)), 'b--', label='Periodic extension')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'$cos(cos(x))$ Function value')
xlabel(r'$x \rightarrow$') 
ylabel(r'$cos(cos(x)) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-2') # Starting a new plot/figure
semilogy(x, func_exp(x), 'r', label='Actual Function')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'$e^x$ Function value')
xlabel(r'$x \rightarrow$') 
ylabel(r'$exp(x) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-2.1') # Starting a new plot/figure
semilogy(x, func_exp(x), 'r', label='Actual Function')
semilogy(x, func_exp(x%(2*pi)), 'b--', label='Periodic extension')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'$e^x$ Function value')
xlabel(r'$x \rightarrow$') 
ylabel(r'$exp(x) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

# A function that returns the first 51 fourier series coefficients for the given function
def compute_51_FS_coeffs(f):
    coeffs = zeros(51)
    coeffs[0] = quad(func_cos_coeff, 0, 2*pi, args=(0, f))[0]/(2*pi)
    for i in range(1, 26):
        coeffs[2*i -1] = quad(func_cos_coeff, 0, 2*pi, args=(i, f))[0]/(pi)
        coeffs[2*i] = quad(func_sin_coeff, 0, 2*pi, args=(i, f))[0]/(pi)
        
    return coeffs

coscos_coeff = compute_51_FS_coeffs(func_coscosx) # Computing the FS coefficients of cos(cos(x))
exp_coeff = compute_51_FS_coeffs(func_exp) # Computing the FS coefficients of exp(x)

# A function that performs the least square estimation of the given function to get the 51 best fit coefficients
def compute_lstsq_coeff(f):
    x = linspace(0, 2*pi, 401)
    x = x[:-1]
    b = f(x)
    A = zeros((400, 51))
    A[:,0] = 1
    for k in range(1,26):
        A[:,(2*k)-1]=cos(k*x)
        A[:,2*k]=sin(k*x)

    return lstsq(A, b, rcond=None)[0]
    
lstsq_coscos_coeff = compute_lstsq_coeff(func_coscosx) # Performing the least square estimation to get best fit coefficients of cos(cos(x))
lstsq_exp_coeff = compute_lstsq_coeff(func_exp) # Performing the least square estimation to get best fit coefficients of exp(x)

# Computing the error in the coefficients(from Least square estimate and the ones found using integration)
abs_error_coscos_coeff = [abs(coscos_coeff[i]-lstsq_coscos_coeff[i]) for i in range(len(coscos_coeff))] 
abs_error_exp_coeff = [abs(exp_coeff[i]-lstsq_exp_coeff[i]) for i in range(len(exp_coeff))]
    
print('The maximum deviation in the coefficients computed for cos(cos(x)): '+str(max(abs_error_coscos_coeff)))
print('The maximum deviation in the coefficients computed for exp(x): '+str(max(abs_error_exp_coeff)))

figure('Figure-3') # Starting a new plot/figure
semilogy(abs(exp_coeff), 'ro', label='Coefficients by integration')
title(r'$exp(x)$ Fourier Series coefficents : semilog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-3.1') # Starting a new plot/figure
semilogy(abs(exp_coeff), 'ro', label='Coefficients by integration')
semilogy(abs(lstsq_exp_coeff), 'go', label='Coefficients by lstsq')
title(r'Comparing $exp(x)$ Fourier Series coefficients : semilog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-4') # Starting a new plot/figure
loglog(abs(exp_coeff), 'ro', label='Coefficients by integration')
title(r'$exp(x)$ Fourier Series coefficents : loglog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-4.1') # Starting a new plot/figure
loglog(abs(exp_coeff), 'ro', label='Coefficients by integration')
loglog(abs(lstsq_exp_coeff), 'go', label='Coefficients by lstsq')
title(r'Comparing $exp(x)$ Fourier Series coefficients : loglog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-5') # Starting a new plot/figure
semilogy(abs(coscos_coeff), 'ro', label='Coefficients by integration')
title(r'$cos(cos(x))$ Fourier Series coefficents : semilog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-5.1') # Starting a new plot/figure
semilogy(abs(coscos_coeff), 'ro', label='Coefficients by integration')
semilogy(abs(lstsq_coscos_coeff), 'go', label='Coefficients by lstsq')
title(r'Comparing $cos(cos(x))$ Fourier Series coefficients : semilog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-6') # Starting a new plot/figure
loglog(abs(coscos_coeff), 'ro', label='Coefficients by integration')
title(r'$cos(cos(x))$ Fourier Series coefficents : loglog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-6.1') # Starting a new plot/figure
loglog(abs(coscos_coeff), 'ro', label='Coefficients by integration')
loglog(abs(lstsq_coscos_coeff), 'go', label='Coefficients by lstsq')
title(r'Comparing $cos(cos(x))$ Fourier Series coefficients : loglog plot')
xlabel(r'$n \rightarrow$') 
ylabel(r'$coefficients \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

x_new = linspace(0,2*pi,401)
x_new = x_new[:-1]
matrix_A = zeros((400,51)) # Creating the A matrix
matrix_A[:,0] = 1 # Setting the first column as 1
for i in range(1,26): # Setting the remaining columns
    matrix_A[:,(2*i)-1]=cos(i*x_new) 
    matrix_A[:,2*i]=sin(i*x_new)

figure('Figure-7') # Starting a new plot/figure
plot(x, func_coscosx(x), 'r', label='Actual Function')
plot(x, func_coscosx(x%(2*pi)), 'b--', label='Periodic extension')
plot(x_new, dot(matrix_A,lstsq_coscos_coeff), 'go', label='using lstsq coefficients')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'Estimated Function of $cos(cos(x))$')
xlabel(r'$x \rightarrow$') 
ylabel(r'$cos(cos(x)) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot

figure('Figure-8') # Starting a new plot/figure
semilogy(x, func_exp(x), 'r', label='Actual Function')
semilogy(x, func_exp(x%(2*pi)), 'b--', label='Periodic extension')
semilogy(x_new, dot(matrix_A,lstsq_exp_coeff), 'go', label='using lstsq coefficients')
axes().xaxis.set_major_formatter(FuncFormatter(lambda val,pos: r'{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'))
axes().xaxis.set_major_locator(MultipleLocator(base=pi))
title(r'Estimated Function of $e^x$')
xlabel(r'$x \rightarrow$') 
ylabel(r'$exp(x) \rightarrow$')
legend()
grid() # Adding grid to the figure/plot
show() # Displaying the figure/plot