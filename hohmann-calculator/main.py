import math

# For an ascending transfer
##########################################################
                                                        ##
# Assumes a circular target and chase initial orbit.    ##
                                                        ##
# Gravitational parameter, in m^3 s^-2                  ##
mu = 3.986 * (10**14)                                   ##
                                                        ##
# Radius of body (meters)                               ##
h0 = 6371000                                            ##
                                                        ##
# Height from surface of target and chase orbits        ##
# (meters)                                              ##
h_chase = 200000                                        ##
h_target = 300000                                       ##
                                                        ##
##########################################################

def halfpd(a):
  return math.pi * math.sqrt((a**3)/mu)

a_target = h_target + h0
a_chase = h_chase + h0
a_xfer = (h_target + h_chase)/2 + h0

T_target = 2 * halfpd(a_target)
T_chase = 2 * halfpd(a_chase)
o_xfer = halfpd(a_xfer)

print("T_target " + str(T_target))
print("T_chase  " + str(T_chase))
print("Xfer ToF " + str(o_xfer))

# period/360deg = 1
# 360deg/period = 1
# how many degs does target sweep in xfer tot?

targ_swept = o_xfer * 360/T_target
print("Degs sweeped out by target in " + str(o_xfer) + " secs")
print(targ_swept)

print("Req'd phase")
print("-- " + str(180 - targ_swept) + " --")
