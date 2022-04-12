# Pygame Boids

The code in this repository implements flocking behaviour of bird-oid objects (boids) with python pygame library.

Flocking is a model for coordinated movement of agentes (boids). Manouver combinations of a boid are based on the positions and velocities of its neighbours within a pre-defined perception range. 

Three basic rules are used to implement such behaviour. Separation, maneuver to avoid crowded places. Alignment, move in the direction of neighbouring boids. And Cohesion, move to the average position of the other boids.

There is also a species separation rule. Species are represented by the boid color. Boids avoid boids from different species.

Boids can move in three different ways, exemplified by the gifs below.

Unbounded movevment. There is no positional goal, boids only move according to the three basic rules and species rule.
![](https://github.com/heitor-azambuja/huge-gifs/blob/main/boids-unbound.gif)

Mouse following. Boids are attracted to the mouse cursor position.
![](https://github.com/heitor-azambuja/huge-gifs/blob/main/boids-follow-mouse.gif)

Boids path following. Boids move sequentially through a list of predefined goal positions, represented by blue circles on the background.
![](https://github.com/heitor-azambuja/huge-gifs/blob/main/boids-follow-path-list.gif)

Read the tutorial aboud the implementation on [thrivingant.com](https://www.thrivingant.com) (work in progess)

## Instalation

This code only uses one library, [pygame](https://www.pygame.org/docs/). Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
python3 -m pip install -r requirements.txt
```

## Usage

To start the simulation, just run:
```bash
python3 main.py 
```
Key "r" restarts the simulation and "q" quits it. 

All parameters of the simulation can be configured in the file "globals.py".

## Contributing

If you have encountered any bug or problem, have any sugestion or feature request open an issue.

## To do
 - Expand usage;
 - Bound 3d functioin to screen área;
 - Make boids flock around the optimal (min or max);
 - Generate heatmap of function to use as pygame window background;
 - command line argument parser;
 - Write tutorial;


## References
- Craig Reynolds - Original 1986 Boids simulation. [video](https://www.youtube.com/watch?v=86iQiV3-3IA)
- How to make Boids in Godot ([link](https://github.com/aimforbigfoot/NAD-LAB-Godot-Projects/tree/master/boidsArea2D)). Godot game engine implementation with [video tutorial](https://www.youtube.com/watch?v=oFnIlNW_p10&ab_channel=NADLABS).
- Simulating Bird Flock Behavior in Python Using Boids ([link](https://github.com/roholazandie/boids)). Implementation with p5, a javascript library imported to python. [Tutorial](https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118).
- Neat AI does Predator Boids. Video that explains several behaviours. [link](https://www.youtube.com/watch?v=rkQB4zEJggE&ab_channel=NeatAI)

## Author
- Heitor Teixeira de Azambuja

## License

MIT License

Copyright (c) 2022,  Heitor Teixeira de Azambuja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.