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
## Author
- Heitor Teixeira de Azambuja

## License
[MIT](https://choosealicense.com/licenses/mit/)