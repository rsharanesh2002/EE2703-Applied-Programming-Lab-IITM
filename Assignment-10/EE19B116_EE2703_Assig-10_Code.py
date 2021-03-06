'''
EE2703 Applied Programming Lab
Submission for Assignment-10 
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# Question-1 
# Plot of spectrum of sin(sqrt(2)t) without hamming window
t = linspace(-pi,pi,65)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
y = sin(sqrt(2)*t)
y[0] = 0 
y = fftshift(y) 
Y = fftshift(fft(y))/64.0
w = linspace(-pi*fmax,pi*fmax,65)
w = w[:-1]

figure('Figure_1')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-10,10])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of $\sin\left(\sqrt{2}t\right)$")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-10,10])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

# Plot of spectrum of sin(sqrt(2)t) with hamming window
t = linspace(-4*pi,4*pi,257)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(256)
ham_wnd = fftshift(0.54+0.46*cos(2*pi*n/256))
y = sin(sqrt(2)*t)*ham_wnd
y[0] = 0 
y = fftshift(y) 
Y = fftshift(fft(y))/256.0
w = linspace(-pi*fmax,pi*fmax,257)
w = w[:-1]

figure('Figure_2')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-4,4])
ylabel(r"$|Y|\rightarrow$")
title(r"Improved Spectrum of $\sin\left(\sqrt{2}t\right)$")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

# Question-2 
# Plotting a spectrum of cos^3(0.86t), with and without windowing.
y = cos(0.86*t)**3
y1 = y*ham_wnd
y[0]=0
y1[0]=0
y = fftshift(y)
y1 = fftshift(y1)
Y = fftshift(fft(y))/256.0
Y1 = fftshift(fft(y1))/256.0

figure('Figure_3')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-4,4])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of $\cos^{3}(0.86t)$ without Hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

figure('Figure_4')
subplot(2,1,1)
plot(w,abs(Y1),lw=2)
xlim([-4,4])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of $\cos^{3}(0.86t)$ with Hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y1),'go',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

# Question-3 
# Estimating the spectrum of cosine w0 = 1.5 and delta = 0.5.
w0 = 1.5
d = 0.5

t = linspace(-pi,pi,129)[:-1]
dt = t[1]-t[0]; fmax = 1/dt
n = arange(128)
ham_wnd = fftshift(0.54+0.46*cos(2*pi*n/128))
y = cos(w0*t + d)*ham_wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/128.0
w = linspace(-pi*fmax,pi*fmax,129)
w = w[:-1]

figure('Figure_5')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-4,4])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of $\cos(w_0t+\delta)$ with Hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

# w0 is estimated by finding the weighted average of all w>0
# Delta is found by calculating the phase at w closest to w0
ii = where(w>=0)
w_cal = sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2)
i = abs(w-w_cal).argmin()
delta = angle(Y[i])
print("Estimated value of w0 without noise: ",w_cal)
print("Estimated value of delta without noise: ",delta)

# Question-4 
# Adding white gaussian noice to the above part
y = (cos(w0*t + d) + 0.1*randn(128))*ham_wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/128.0

figure('Figure_6')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-4,4])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of a noisy $\cos(w_0t+\delta)$ with Hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-4,4])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

# w0 is estimated by finding the weighted average of all w>0
# Delta is found by calculating the phase at w closest to w0
ii = where(w>=0)
w_cal = sum(abs(Y[ii])**2*w[ii])/sum(abs(Y[ii])**2)
i = abs(w-w_cal).argmin()
delta = angle(Y[i])
print("Estimated value of w0 with noise: ",w_cal)
print("Estimated value of delta with noise: ",delta)

# Question-5 + Question-6
# Plotting the spectrum of a "chirped" signal
# Plotting a 3D surface plot with respect to t and w.

# For the case without hamming window
t = linspace(-pi,pi,1025)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(1024)
y = cos(16*t*(1.5 + t/(2*pi)))
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/1024.0
w = linspace(-pi*fmax,pi*fmax,1025)
w = w[:-1]

figure('Figure_7')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-100,100])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of chirped function $|Y|\rightarrow$ without hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-100,100])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

t_array = split(t,16)
Y_mag = zeros((16,64))
Y_phase = zeros((16,64))

for i in range(len(t_array)):
	n = arange(64)
	y = cos(16*t_array[i]*(1.5 + t_array[i]/(2*pi)))
	y[0]=0
	y = fftshift(y)
	Y = fftshift(fft(y))/64.0
	Y_mag[i] = abs(Y)
	Y_phase[i] = angle(Y)

t = t[::64]	
w = linspace(-fmax*pi,fmax*pi,64+1)
w = w[:-1]
t,w = meshgrid(t,w)

fig = figure('Figure_9')
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(w,t,Y_mag.T,cmap='jet')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_title('Surface plot for the case, without hamming window');
ylabel(r"$\omega\rightarrow$")
xlabel(r"$t\rightarrow$")
show()

# For the case with hamming window
t = linspace(-pi,pi,1025)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(1024)
ham_wnd = fftshift(0.54+0.46*cos(2*pi*n/1024))
y = cos(16*t*(1.5 + t/(2*pi)))*ham_wnd
y[0]=0
y = fftshift(y)
Y = fftshift(fft(y))/1024.0
w = linspace(-pi*fmax,pi*fmax,1025)
w = w[:-1]

figure('Figure_8')
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-100,100])
ylabel(r"$|Y|\rightarrow$")
title(r"Spectrum of chirped function $|Y|\rightarrow$ with hamming window")
grid(grid)
subplot(2,1,2)
plot(w,angle(Y),'go',lw=2)
xlim([-100,100])
ylabel(r"Phase of $Y\rightarrow$")
xlabel(r"$\omega\rightarrow$")
grid()
show()

t_array = split(t,16)
Y_mag = zeros((16,64))
Y_phase = zeros((16,64))

for i in range(len(t_array)):
	n = arange(64)
	ham_wnd = fftshift(0.54+0.46*cos(2*pi*n/64))
	y = cos(16*t_array[i]*(1.5 + t_array[i]/(2*pi)))*ham_wnd
	y[0]=0
	y = fftshift(y)
	Y = fftshift(fft(y))/64.0
	Y_mag[i] = abs(Y)
	Y_phase[i] = angle(Y)

t = t[::64]	
w = linspace(-fmax*pi,fmax*pi,64+1)
w = w[:-1]
t,w = meshgrid(t,w)

fig = figure('Figure_10')
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(w,t,Y_mag.T,cmap='jet')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_title('Surface plot for the case, with hamming window');
ylabel(r"$\omega\rightarrow$")
xlabel(r"$t\rightarrow$")
show()