## ENGPHYS 213 Final

This is small python script that simulates a chaotic double pendulum.
The equations were taken from <a src="http://scienceworld.wolfram.com/physics/DoublePendulum.html"> this </a> link.
A more detailed description of the implementation can be found in the <a src="pendulum.py">file</a>.

The algorithim accurately computes the steady values for the system:
<img src="output/steady_state.png">

Similarily, the output for the case where m1 << m0 also appears logical:
<img src="output/negligible_mass.png">

The chaoticness of the system can be observed from the following charts:
<img src="output/chaotic1.png">
<img src="output/chaotic2.png">

Otherwise, these various outputs from the different input parameters
<img src="output/cool.png">
<img src="output/cool2.png">
<img src="output/cool3.png">
