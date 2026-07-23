# Stopping Distance Simulator
Uses an Euler integrator to predict stopping distance ground track (tuned for the Apollo LM's DPS, but can be changed)

## Presentation
The results of the simulator are output in the following format:
```
VAR  UNIT    VALUE
------------------
V    M/S  =  0.2
```

Of course, ideally, velocity should be zero by the end of the simulation, but this is not possible with this method of numerical integration.

The stopping distance is also presented in many units, namely:
* Meters (M)
* Kilometers (KM)
* Nautical miles (NMI)
* Lunar equatorial degrees of longitude (marked with EQDLNG)

During the simulation, values will be output in the following format:
```
Iteration {iter}
t     = time
a     = acceleration
ax    = horizontal component of acceleration vector
theta = pitch angle
d     = distance traveled
v     = velocity
```

## Problems
* Assumes a non-rotating Moon (very big problem).
* This model predicts 194 nmi of stopping distance, and that's about 60 nmi off from the actual Apollo telemetry. Also, to my knowledge, the Apollo missions didn't even cancel out all of their horizontal velocity in this phase of flight, making this model even more inaccurate.
  * Possible causes:
    * Assumes linear pitch change rate
    * Assumes a non-rotating Moon
    * Assumes a flat Moon (not *that* big of a problem)
    * Does not change mass rate (mdot) based on variable thrust (problem because of the 26-second low-thrust period after PDI)

Hopefully it adds to the merit of this project that I also included the 26-second low-thrust period after powered descent ignition (PDI) as a sigmoid.
