# wind-power-plant
Resources for simulations and real work of wind power plant

Proposed project structure
- ros/
  - wind-power-plant (package)
    - wind-power-plant-controller (node)
- gazebo
  - plugins
    - wind-generator: model plugin which generates wind. Visualisates as arrow and sends messages about direction and speed
    - compass-simulator: model plugin which sends messages about direction of connected model
    - servomotor-simulator: model plugin which can change yaw of model according to messages with information about angle

