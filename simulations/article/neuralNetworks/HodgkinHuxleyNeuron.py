"""
Summary:
This code simulates the Hodgkin-Huxley neuron model, which describes the behavior 
of the action potential in a neuron. The model includes membrane capacitance and 
ion conductances for sodium, potassium, and leakage currents. The simulation uses 
the Euler method to update the membrane potential and gating variables over time 
in response to an injected current. The results, including membrane potential and 
gating variables (m, h, n), are plotted to visualize the dynamics of the Hodgkin-Huxley 
neuron model.
"""

import math
import matplotlib.pyplot as plt

# Hodgkin-Huxley model parameters
Cm = 1.0   # Membrane capacitance (uF/cm^2)
g_Na = 120.0  # Sodium conductance (mS/cm^2)
g_K = 36.0    # Potassium conductance (mS/cm^2)
g_leak = 0.3  # Leak conductance (mS/cm^2)
E_Na = 50.0   # Sodium reversal potential (mV)
E_K = -77.0   # Potassium reversal potential (mV)
E_leak = -54.387  # Leak reversal potential (mV)

# Time parameters
dt = 0.01  # Time step (ms)
t_max = 50.0  # Maximum simulation time (ms)

# Initial conditions
V, m, h, n = -65.0, 0.05, 0.6, 0.32  # V, m, h, n

# Lists to store results for plotting
time_points = []
membrane_potential = []
gating_variables_m = []
gating_variables_h = []
gating_variables_n = []

# Helper functions for rate constants
def alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - math.exp(-(V + 40.0) / 10.0))

def beta_m(V):
    return 4.0 * math.exp(-(V + 65.0) / 18.0)

def alpha_h(V):
    return 0.07 * math.exp(-(V + 65.0) / 20.0)

def beta_h(V):
    return 1.0 / (1.0 + math.exp(-(V + 35.0) / 10.0))

def alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - math.exp(-(V + 55.0) / 10.0))

def beta_n(V):
    return 0.125 * math.exp(-(V + 65.0) / 80.0)

# Simulation loop
for t in range(int(t_max / dt)):
    # Membrane currents
    I_Na = g_Na * m**3 * h * (V - E_Na)
    I_K = g_K * n**4 * (V - E_K)
    I_leak = g_leak * (V - E_leak)

    # Total membrane current
    I_total = 10.0  # Injected current (adjust as needed)

    # Update variables using Euler method
    dVdt = (I_total - I_Na - I_K - I_leak) / Cm
    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n

    V += dt * dVdt
    m += dt * dmdt
    h += dt * dhdt
    n += dt * dndt

    # Store results for plotting
    time_points.append(t * dt)
    membrane_potential.append(V)
    gating_variables_m.append(m)
    gating_variables_h.append(h)
    gating_variables_n.append(n)

# Plot results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time_points, membrane_potential, label='Membrane Potential (mV)')
plt.title('Hodgkin-Huxley Neuron Model')
plt.ylabel('Voltage (mV)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time_points, gating_variables_m, label='m')
plt.plot(time_points, gating_variables_h, label='h')
plt.plot(time_points, gating_variables_n, label='n')
plt.xlabel('Time (ms)')
plt.ylabel('Gating Variables')
plt.legend()

plt.tight_layout()
plt.show()
