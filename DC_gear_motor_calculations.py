
import math

####################### Definitions #################
# Mass to be lifted
m = 30

# gravity
g = 9.82

# Speed
v = 2/7
print("Linear speed =",v,"m/s")


#Diameter of coil
d_coil = 60*10**-3

# wire diameter [m]
d_wire = 1*10**-3

# wire travel [m]
t = 2

# Circumference
c = math.pi * d_coil
print("Circumference =",c,"m")

# rounds at coil needed
rounds = t / c
print("Rounds needed =",rounds)

# needed height for the given coil diameter
h = rounds * d_wire
print("Needed height =",h*1000,"mm")

# Force
F = m*g
print("Force =",F,"N")

# Minimum torque motor must deliver
T = F * d_coil/2
print("Needed torque =",T,"Nm")




