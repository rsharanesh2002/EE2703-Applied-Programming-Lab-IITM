'''
EE2703 Applied Programming Lab
Submission for Assignment-7
Name: Sharanesh R
Roll Numer: EE19B116
'''

from pylab import *
import scipy.signal as sg

# A function that computes the impulse response for the spring equation
def spring_response(b,w):
	X_Num = poly1d([1, b])
	X_Den = polymul([1, 2*b, b**2 + 2.25], [1, 0, 2.25])
	X = sg.lti(X_Num, X_Den)
	t, x = sg.impulse(X, None, linspace(0, 50, 1000))
	return t, x

# Question-1
t, x = spring_response(0.5, 1.5)
figure('Figure_1')
plot(t, x)
xlabel(r"$t \rightarrow$")
ylabel(r"$x(t) \rightarrow$")
title(r'Solution for the spring equation with damping decay coeffcient of 0.5')
grid()
show()

# Question-2
t, x = spring_response(0.05, 1.5)
figure('Figure_2')
plot(t, x)
xlabel(r"$t \rightarrow$")
ylabel(r"$x(t) \rightarrow$")
title(r'Solution for the spring equation with damping decay coeffcient of 0.05')
grid()
show()

# Question-3
H = sg.lti([1], [1, 0, 2.25])
figure('Figure_3')
for w in arange(1.4, 1.6, 0.05): # Looping through the given set of frequencies
	vec_t = linspace(0, 50, 1000)
	t, y, rest = sg.lsim(H, exp(-0.05*vec_t)*cos(w*vec_t), vec_t)
	plot(t, y, label=r'$w = {} rad/s$'.format(w))

legend()
xlabel(r"$t \rightarrow$")
ylabel(r"$x(t) \rightarrow$")
title(r"Output of the LTI system to the various frequencies in (1.4,1.6,0.05)")
grid()
show()

# Question-4
X = sg.lti([1, 0, 2], [1, 0, 3, 0])
t, x = sg.impulse(X, None, linspace(0, 20, 1000))
Y = sg.lti([2], [1, 0, 3, 0])
t, y = sg.impulse(Y, None, linspace(0, 20, 1000))

figure('Figure_4')
plot(t, y, label=r"$y(t)$")
plot(t, x, label=r"$x(t)$")
xlabel(r"$t \rightarrow$")
title(r"Solution the coupled spring problem") 
legend()
grid()
show()

# Question-5
H = sg.lti([1], [1e-12, 1e-4, 1]) # Definfing a LTI system for the RLC network
w, mag, phase = sg.bode(H)

figure('Figure_5')
semilogx(w, mag)
xlabel(r"$\omega \rightarrow$")
ylabel(r"$\|H(jw)\|\ (in\ dB)$")
title("Magnitude response plot of the given RLC network")
grid()
show()

figure('Figure_6')
semilogx(w, phase)
xlabel(r"$\omega \rightarrow$")
ylabel(r"$\angle H(jw)\ (in degrees)$")
title("Phase response plot of the given RLC network")
grid()
show()

# Question-6
t = arange(0, 0.05, 1e-7)
v_in = cos(1e3*t) - cos(1e6*t) # Given input for the two port RLC network
t_plot, v_out, rest = sg.lsim(H, v_in, t) # Simulating the RLC network for the given input

# Plot showing the low frequency variation
figure('Figure_7')
plot(t_plot, v_out)
xlabel(r"$t\rightarrow$")
ylabel(r"$v_o(t)\rightarrow$")
title(r"$v_o(t)$ for the given input $v_i(t)$")
grid()
show()

# Plot showing the high frequency variation
figure('Figure_8')
plot(t_plot, v_out)
xlim(0, 3e-5)
ylim(0, 0.35)
xlabel(r"$t\rightarrow$")
ylabel(r"$v_o(t)\rightarrow$")
title(r"$v_o(t)$ for $0<t<30\ us$")
grid()
show()
