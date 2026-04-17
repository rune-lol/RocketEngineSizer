import math

### Design parameters
F = 250 # N, design thrust
P_CHAMBER = 10 # bar, chamber pressure
Isp = 2175.4/9.81 # s, take data from the CEA Output
OF_RATIO = 1.3 # make sure it lines up with CEA
AeAt = 2.2959 # taken from CEA
C_star = 1715 # m/s, taken from CEA
L_star = 1.5 # m, guessed based on data from the internet
dcdt = 3 # guessed based off of data from the internet
deltaP = 2.5 # bar, injector deltaP, guessed from data from the internet
Cd = 0.7 # injector discharge coefficient
rho_fuel = 789 # kg/m^3
rho_ox = 0 # kg/m^3
d_injectorhole = 0.8 # mm

### Physical constants
G = 9.81 # m/s^2

### Calculate mass flow
m_dot = F/(Isp*G)
m_dot_ox = m_dot * (OF_RATIO/(1+OF_RATIO))
m_dot_fuel = m_dot * (1/(1+OF_RATIO))

print(f"Mass flow: {round(m_dot, 3)}kg/s ({round(m_dot_ox, 3)} OX, {round(m_dot_fuel, 3)} FUEL)")

### Throat sizing
A_t = (m_dot*C_star)/(P_CHAMBER*100_000) # 100_000 to go from bar to Pa
d_t = math.sqrt(A_t/math.pi) * 2

print(f"Throat Area: {round(A_t*10_000, 3)}cm^2, d_t={d_t*1_000}mm")

### Nozzle exit sizing
A_e = AeAt * A_t
d_e = math.sqrt(A_e/math.pi) * 2
print(f"Nozzle exit area: {round(A_e*10_000, 3)}cm^2, d_e={d_e*1_000}mm")

### Chamber sizing
V_c = L_star * A_t
d_c = dcdt * d_t
A_c = math.pi * (d_c/2)**2
L_c = V_c/A_c
print(f"Chamber volume: {round(V_c*1_000_000, 3)}cc, d_c={d_c*1_000}mm, L_c={L_c*1_000}mm")

### Injector sizing
A_hole = ((d_injectorhole / (2*1000))**2)*math.pi
A_fuel = m_dot/(Cd * math.sqrt(2*rho_fuel*(deltaP*100_000)))

N_fuel = A_fuel / A_hole
print("Injector:")
print(f"Fuel: Area: {round(A_fuel*1_000_000, 3)}mm^2, holes: {N_fuel} of {d_injectorhole}mm")

### Tank pressure verification
print(f"P_tank needs to be at least {(P_CHAMBER + deltaP)}bar")