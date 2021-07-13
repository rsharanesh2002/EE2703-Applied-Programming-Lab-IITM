'''
EE2703 Applied Programming Lab
Submission for Assignment-8 
Name: Sharanesh R
Roll Numer: EE19B116
'''

import scipy.signal as sg
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

s = sym.symbols('s')
t = np.linspace(0, 0.1, 10**6)

# Function for a lowpass filter
def lowpass(R1, R2, C1, C2, G, Vi):
    s = sym.symbols('s')
    A = sym.Matrix([[0, 0, 1, -1/G],
                    [-1/(1+s*R2*C2), 1, 0, 0],
                    [0, -G, G, 1],
                    [-1/R1-1/R2-s*C1, 1/R2, 0, s*C1]])
    b = sym.Matrix([0,0,0,-Vi/R1])
    V = A.inv() * b
    return V[3]

# Function for a highpass filter
def highpass(R1,R3,C1,C2,G,Vi):
    s = sym.symbols("s")
    A = sym.Matrix([[0,-1,0,1/G],
        [s*C2*R3/(s*C2*R3+1),0,-1,0],
        [0,G,-G,1],
        [-1*s*C2-1/R1-s*C1,0,s*C2,1/R1]])
    b = sym.Matrix([0,0,0,-Vi*s*C1])
    V = A.inv()*b
    return V[3]

# A function for converting the sympy expressions to a LTI system
def sympytoLTI(symboFunc):
    num, den = sym.fraction(symboFunc)
    num = sym.Poly(num, s)
    den = sym.Poly(den, s)
    num_coeffs = num.all_coeffs()
    den_coeffs = den.all_coeffs()
    num_coeffs = [float(num) for num in num_coeffs]
    den_coeffs = [float(den) for den in den_coeffs]
    return sg.lti(num_coeffs,den_coeffs)

# Computing the lowpass filter system
Vo_s_lp = sympytoLTI(lowpass(10000, 10000, 1e-9, 1e-9, 1.586, 1))

# Bode Plot of Transfer Function
w, mag, phase = sg.bode(Vo_s_lp, w=np.linspace(0, 10**6, 10**6))
plt.figure(1)
plt.title(r'Bode Plot of Transfer function of lowpass filter')
plt.semilogx(w, mag)
plt.xlabel(r'$\omega \ \to$')
plt.ylabel(r'$20log(\|H(j\omega)\|)$')
plt.grid(True)
plt.show()

# Step response of the low pass filter
time, Vo_step = sg.step(Vo_s_lp, None, t)
plt.figure(2)
plt.plot(time, Vo_step)
plt.title(r'Step Response of Lowpass filter')
plt.xlabel(r'$t\ \longrightarrow$')
plt.ylabel(r'$V_o(t)\ \longrightarrow$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Response of the low pass filter for the given Vi(t)
Vi = np.heaviside(t, 1)*(np.sin(2e3*np.pi*t)+np.cos(2e6*np.pi*t))
time, V_out, rest = sg.lsim(Vo_s_lp, Vi, t)
plt.figure(3)
plt.plot(t, Vi)
plt.title(r'$V_i(t)=(sin(2x10^3\pi t)+cos(2x10^6\pi t))u(t)$ to Lowpass filter')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_i(t)\ \to$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Plot of the output of the lowpass filter for the given input
plt.figure(4)
plt.plot(time, V_out)
plt.title(r'$V_o(t)$ for $V_i(t)=(sin(2x10^3\pi t)+cos(2x10^6\pi t))u(t)$ for Lowpass filter')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_o(t)\ \to$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Computing the highpass filter system
Vo_s_hp = sympytoLTI(highpass(10000, 10000, 1e-9, 1e-9, 1.586, 1))

## Bode Plot of Transfer Function
w, mag, phase = sg.bode(Vo_s_hp, w=np.linspace(0, 10**6, 10**6))
plt.figure(5)
plt.title(r'Bode Plot of Transfer function of highpass filter')
plt.semilogx(w, mag)
plt.xlabel(r'$\omega \ \to$')
plt.ylabel(r'$20log(\|H(j\omega)\|)$')
plt.grid(True)
plt.show()

time, voStep = sg.step(Vo_s_hp, None, t)
plt.figure(6)
plt.plot(time, voStep)
plt.title(r'Step Response of highpass filter')
plt.xlabel(r'$t\ \longrightarrow$')
plt.ylabel(r'$V_o(t)\ \longrightarrow$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Response of the highpass filter for the given Vi(t)
Vi = np.heaviside(t, 1)*(np.sin(2e3*np.pi*t)+np.cos(2e6*np.pi*t))
time, V_out, rest = sg.lsim(Vo_s_hp, Vi, t)
plt.figure(7)
plt.plot(t, Vi)
plt.title(r'$V_i(t)=(sin(2x10^3\pi t)+cos(2x10^6\pi t))u(t)$ to highpass filter')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_i(t)\ \to$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Plot of the output of the highpass filter for the given input
plt.figure(8)
plt.plot(time, V_out)
plt.title(r'$V_o(t)$ for $V_i(t)=(sin(2x10^3\pi t)+cos(2x10^6\pi t))u(t)$ for highpass filter')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_o(t)\ \to$')
plt.xlim(0, 1e-3)
plt.grid(True)
plt.show()

# Defining the high and low frequency damped sinusoidal signals
Vi_damp_low_freq = np.heaviside(t, 1)*(np.sin(2e3*np.pi*t))*np.exp(-10*t)
Vi_damp_high_freq = np.heaviside(t, 1)*(np.sin(2e6*np.pi*t))*np.exp(-10*t)

# Output for low frequency damped sinusoid
time, Vo_damp_low_freq, rest = sg.lsim(Vo_s_hp, Vi_damp_low_freq, t)
plt.figure(9)
plt.plot(time, Vi_damp_low_freq,label=r'$V_i(t)$')
plt.plot(time, Vo_damp_low_freq,label=r'$V_o(t)$')
plt.title(r'$V_o(t)$ for $V_i(t)=sin(2x10^3\pi t)e^{-10t}u(t)$ for Highpass filter (Low frequency Damped input)')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_o(t)\ \to$')
plt.xlim(0, 1e-1)
plt.legend()
plt.grid(True)
plt.show()

# Output for high frequency damped sinusoid
time, Vo_damp_high_freq, rest = sg.lsim(Vo_s_hp, Vi_damp_high_freq, t)
plt.figure(10)
plt.plot(time, Vi_damp_high_freq,label=r'$V_i(t)$')
plt.plot(time, Vo_damp_high_freq,label=r'$V_o(t)$')
plt.title(r'$V_o(t)$ for $V_i(t)=sin(2x10^6\pi t)e^{-10t}u(t)$ for Highpass filter (High frequency Damped input)')
plt.xlabel(r'$t\ \to$')
plt.ylabel(r'$V_o(t)\ \to$')
plt.xlim(0, 5e-5)
plt.legend()
plt.grid(True)
plt.show()