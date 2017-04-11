## ENGPHYS 213 Final

This is small python script that simulates a chaotic double pendulum.
The equations were taken from <a src="http://scienceworld.wolfram.com/physics/DoublePendulum.html"> this </a> link.
A more detailed description of the implementation can be found in the <a src="pendulum.py">file</a>.

The algorithim accurately computes the steady values for the system:
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/steady_state.png)

Similarily, the output for the case where m1 << m0 also appears logical:
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/neglibile_mass.png)

The chaoticness of the system can be observed from the following charts:
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/chaotic1.png)
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/chaotic1.png)

Otherwise, these various outputs from the different input parameters
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/cool.png)
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/cool2.png)
![](https://raw.github.com/ReckoningReckoner/pendulum/master/outupt/cool3.png)
