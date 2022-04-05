# Pygame Boids

The code in this repository implements flocking behaviour of bird-oid objects (boids) with python pygame library.

Flocking is a model for coordinated movement of agentes (boids). Manouver combinations of a boid are based on the positions and velocities of its neighbours within a pre-defined perception range. 

Three basic rules are used to implement such behaviour. Separation, maneuver to avoid crowded places. Alignment, move in the direction of neighbouring boids. And Cohesion, move to the average position of the other boids.

Read the tutorial aboud the implementation on [thrivingant.com](https://www.thrivingant.com) (work in progess)

## Instalation

This code only uses one library, [pygame](https://www.pygame.org/docs/). Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
python3 -m pip install -r requirements.txt
```

## References
Related projects.
- How to make Boids in Godot ([link](https://github.com/aimforbigfoot/NAD-LAB-Godot-Projects/tree/master/boidsArea2D)). Godot game engine implementation with [video tutorial](https://www.youtube.com/watch?v=oFnIlNW_p10&ab_channel=NADLABS).
- Simulating Bird Flock Behavior in Python Using Boids ([link](https://github.com/roholazandie/boids)). Implementation with p5, a javascript library imported to python. [Tutorial](https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118).

## Author
- Heitor Teixeira de Azambuja

## License
[MIT](https://choosealicense.com/licenses/mit/)
