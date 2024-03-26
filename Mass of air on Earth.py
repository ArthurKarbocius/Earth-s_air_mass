
# # # <<<<<<<<<<<< Total mass of air on the Earth >>>>>>>>>>>>>>>>>
import math
# Maximum height (altitude), [m]:
h = 10**6
# Total iteration number:
N = h
# Volume and density calculation increment, [m]:
delta = h / N
# Earth's radius, [m]
Reth = 6371000
# Average tempareture on Earth, [K]:
T = 293 
# Universal gas constant, [J/(kg*K)]:
R = 287
# Free fall accelaration constant, [m/s^2]:
g = 9.81
# Initial density of air, [kg/m^3]:
ro0 = 1.205
# Exponent constant:
x = g * delta / (R * T)
# Initial mass, [kg]:
M_sum = 0

for n in range(N):  
        # Volumes of spheres at Vn and Vn+1 step:
        Vn = 4/3 * math.pi * (Reth + delta * n)**3
        Vn1 = 4/3 * math.pi * (Reth + delta * (n + 1))**3
        # Density change at every step n:
        ron = ro0 * math.exp(-x * n)
        # Mass of air at every step n+1 minus n:
        Mn = ron * (Vn1 - Vn)
        # Total Mass of air on Earth:
        M_sum += Mn
if M_sum == M_sum:
        print()
        print("Total mass of air =", M_sum ,"kilograms")
        print()

