# swarm_control

This package is a collection implementations that allow conceptual objects to display behaviors of ensembles.  
To control large amounts of objects individually -- as is the example of drones -- one can compute movements for all objects centrally and return instructions to these objects, but this brings limitations that need to be considered. Communication with objects is essential.  
If we consider these swarms of objects capable of executing the right movement in order to fultil a common mission, then we no longer need to communicate with the objects and they can be deployed autonomously.  

To do this we need decentralized control algorithms, such as a distributed consensus algorithm. This type of algorithm allows each body in the ensemble to make decisions based on local information and interactions with its neighboring bodies, without requiring a central authority to coordinate their actions.
This way, the ensemble can coordinate its movements and behavior in a decentralized manner.  

Some of the constraints of commercial drones are regulatory, technological and cost-related.
1. regulatory constraints include strict rules and regulations governing the use of drones in various industries and locations.
2. Technological constraints include limitations in battery life, range, payload capacity, and data transmission capabilities. These affect the feasibility and efficiency of using drones for certain tasks.
3. Cost constraints include the initial cost of purchasing a drone and maintaining a drone; that said, if the control is autonomous, no pilots are needed, and depending on the area the drone is acting, no cost for licenses either.


To be added to https://www.testingbranch.com/ soon
