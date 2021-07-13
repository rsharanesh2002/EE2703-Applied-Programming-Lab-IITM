'''
EE2703 Applied Programming Lab
Submission for Assignment-9 
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import *

## Random Sequence FFT and IFFT
x = rand(128)
X = fft(x)
x_regen = ifft(X)
t = linspace(-64, 64, 129)
t = t[:-1]
figure('Figure_0')
plot(t, x, 'b', label='Actual $x(t)$', lw=2)
plot(t, abs(x_regen), 'r', label='Regenerated $x(t)$', lw=2)
xlabel(r'$t \rightarrow$')
title('Comparison of actual and estimated functions')
grid()
legend()
show()
maxError = max(abs(x_regen-x))
print('Maximum absolute error between actual and regnerated values of the random sequence: ', maxError) 

## Spectrum of sin(5t)
x = linspace(0, 2*pi, 129)
x = x[:-1]
y = sin(5*x)
Y = fftshift(fft(y))/128.0
figure('Figure_1')
suptitle(r'Spectrum of $sin(5t)$')
Y_mag = abs(Y)
Y_phase = angle(Y)
peak_freqs = where(Y_mag > 1e-3)
w = linspace(-64, 64, 129)
w = w[:-1]
subplot(211)
plot(w, Y_mag, lw=2)
xlim([-10, 10])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
grid()
subplot(212)
xlim([-10, 10])
ylim([-pi, pi])
ylabel(r'$\angle Y$')
xlabel(r'$\omega \rightarrow$')
plot(w[peak_freqs], Y_phase[peak_freqs], 'ro', lw=2)
title("Phase Spectrum")
grid()
show()

## AM Modulation with (1 + 0.1cos(t))cos(10t)
x = linspace(-4*pi, 4*pi, 513)
x = x[:-1]
y = (1+0.1*cos(x))*cos(10*x)
Y = fftshift(fft(y))/512.0
figure('Figure_2')
suptitle(r'Spectrum of $(1+0.1cos(t))cos(10t)$')
Y_mag = abs(Y)
Y_phase = angle(Y)
peak_freqs = where(Y_mag > 1e-3)
w = linspace(-64, 64, 513)
w = w[:-1]
subplot(211)
plot(w, Y_mag, lw=2)
xlim([-15, 15])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
grid()
subplot(212)
xlim([-15, 15])
ylim([-pi, pi])
ylabel(r'$\angle Y$')
xlabel(r'$\omega \rightarrow$')
plot(w[peak_freqs], Y_phase[peak_freqs], 'ro', lw=2)
title("Phase Spectrum")
grid()
show()

## Spectrum of sin^3(t)
x = linspace(-4*pi, 4*pi, 513)
x = x[:-1]
y = (sin(x))**3
Y = fftshift(fft(y))/512.0
figure('Figure_3')
suptitle(r'Spectrum of $sin^3(t)$')
Y_mag = abs(Y)
Y_pahse = angle(Y)
peak_freqs = where(Y_mag > 1e-3)
w = linspace(-40, 40, 513)
w = w[:-1]
subplot(211)
plot(w, Y_mag, lw=2)
xlim([-15, 15])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
grid()
subplot(212)
plot(w[peak_freqs], Y_pahse[peak_freqs], 'ro', lw=2)
xlim([-15, 15])
ylim([-pi, pi])
ylabel(r'$\angle Y$')
xlabel(r'$\omega \rightarrow$')
title("Phase Spectrum")
grid()
show()

## Spectrum of cos^3(t)
x = linspace(-4*pi, 4*pi, 513)
x = x[:-1]
y = (cos(x))**3
Y = fftshift(fft(y))/512.0
figure('Figure_4')
suptitle(r'Spectrum of $cos^3(t)$')
Y_mag = abs(Y)
Y_pahse = angle(Y)
peak_freqs = where(Y_mag > 1e-3)
w = linspace(-64, 64, 513)
w = w[:-1]
subplot(211)
plot(w, Y_mag, lw=2)
xlim([-15, 15])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
grid()
subplot(212)
plot(w[peak_freqs], Y_pahse[peak_freqs], 'ro', lw=2)
xlim([-15, 15])
ylim([-pi, pi])
ylabel(r'$\angle Y$')
xlabel(r'$\omega \rightarrow$')
title("Phase Spectrum")
grid()
show()

## Spectrum of cos(20t + 5cos(t))
x = linspace(-4*pi, 4*pi, 513)
x = x[:-1]
y = cos(20*x + 5*cos(x))
Y = fftshift(fft(y))/512.0
figure('Figure_5')
suptitle(r'Spectrum of $cos(20t + 5cos(t))$')
Y_mag = abs(Y)
Y_phase = angle(Y)
peak_freqs = where(Y_mag > 1e-3)
w = linspace(-64, 64, 513)
w = w[:-1]
subplot(211)
plot(w, Y_mag, lw=2)
xlim([-40, 40])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
grid()
subplot(212)
plot(w[peak_freqs], Y_phase[peak_freqs], 'ro', lw=2)
xlim([-40, 40])
ylim([-pi, pi])
ylabel(r'$\angle Y$')
xlabel(r'$\omega \rightarrow$')
title("Phase Spectrum")
grid()
show()

# Spectrum of the gaussain e^(-t^2)/2
# For this case i have taken the interval of [-4*pi,4*pi], for 512 points
t= linspace(-4*pi, 4*pi, 513)
t= t[:-1]     
x = exp(-1*(t**2)/2)
Y = fftshift(fft(x))*4/512.0 
Y_mag = abs(Y)
Y_phase = angle(Y)
w = linspace(-64, 64, 513)
w = w[:-1]
actual_Y = exp(-(w**2)/2)/sqrt(2*pi)
actual_Y_mag = abs(actual_Y)
actual_Y_phase = angle(actual_Y)
figure('Figure_6')
suptitle(r'Comparison of Spectrum of $e^{-t^2/2}$')
subplot(211)
plot(w, Y_mag, 'r', label='Computed spectrum', lw=2)
plot(w, actual_Y_mag,'g.',label= 'Actual spectrum', lw=2)
xlim([-8, 8])
ylabel(r'$\|Y\|$')
title("Magnitude Spectrum")
legend()
grid()
subplot(212)
xlim([-8, 8])
ylim([-2, 2])
ylabel(r'$\angle Y$')
xlabel(r'$\omega$ $\rightarrow$')
title("Phase Spectrum")
plot(w, Y_phase,'ro',lw=2, label='Computed spectrum')
plot(w, actual_Y_phase,'g.',lw=2,label='Computed spectrum')
legend()
grid()
show()

meanError = mean(abs(actual_Y - Y))
print(r'Magnitude of mean error between actual and computed values of the Gaussian: ', meanError)