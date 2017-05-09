# wind-power-plant
Project contains elements for dealing with wind power plant. 
It let us simulate wind and wind turbine in GAZEBO world.  
Elements of project are organized in ROS package. 
We use ROS basic blocks to reach our goal: create software for controlling (simulated or real) wind power plant.

## Building blocks

### Wind simulator
This is gazebo plugin for generating information about wind (in gazebo 8 we could use wind feature). This allow us
* visualize wind in GAZEBO
* sends ROS message about wind properties

### Wind turbine model
Wind turbine model consists of 
* visual model of turbine (tower, gondola, propeller)
* simulation of gondola direction sensor  
* simulation of actuator of gondola hinge

### Wind power plant controller
ROS node which gather information about wind and gondola direction, calculates new gondola direction and sends message to gondola hinge actuator. 
