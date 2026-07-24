import sys
import math

mdot = 68.039 # kg/s
m = 15102.358 # kg
#thrust = 45040 # N 
v = 1696.65 # m/s
theta = 106 # degrees of pitch
thetadot = 0.108 # rate of pitch reduction

def thrust(t):
  return 4053.6/(0.1 + (math.e ** (-20 * (t-32.2)) ) ) + 4504

dt = 0.01
t = 0.0
d = 0.0

print()

if (len(sys.argv) < 2):
  print("----- \033[1;31mINIT\033[0m -----")
  print("| \033[1;37mVAR   UNIT   VALUE\033[0m")
  print("| MDOT  KG/S = " + str(v))
  print("| M     KG   = " + str(m))
  print("| F     N    = " + str(thrust))
  print("| V     M/S  = " + str(v))
  print("| ------------")
  print("| DT    S    = " + str(dt))
  print()

iter = 0

while v > 0:
  a = thrust(t) / m
  ax = abs(a * math.cos(math.radians(theta)))
  theta -= thetadot * dt
  d += v * dt
  v -= ax * dt
  m -= mdot * dt
  t += dt
  print(f"Iteration {iter}")
  print(f"t     = {t}")
  print(f"a     = {a}")
  print(f"ax    = {ax}")
  print(f"theta = {theta}")
  print(f"d     = {d}")
  print(f"v     = {v}")
  for i in range(7):
    sys.stdout.write("\033[A")
  iter += 1

print("\n\n\n\n\n\n\n")

if (len(sys.argv) < 2):
  print("----- \033[1;31mFINAL\033[0m -----")
  print("| \033[1;37mVAR  UNIT  VALUE\033[0m")
  print("| V    M/S = " + str(v))
  print("| T    S   = " + str(t))
  print("| ------------")

print("| D    M   = " + str(d))
print("| D    KM  = " + str(d/1000))
print("| D    NMI = " + str(d/1852))
print("EQDLNG DEG = " + str(d/30330))
print()
