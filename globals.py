from pygame.math import Vector2

#  Screen
WIDTH = 1280
HEIGHT = 720
BACKGROUND_COLOR = (31, 32, 61)
FPS = 60

#  Randomizer
SEED = 1

#  Boids default behaviour
BOIDS_AMOUNT = 190
MAX_SPEED = 15
VISION_RANGE = 50

SEPARATION_THRESHOLD = 25

SEPARATION_MULTIPLIER = 0.1
ALIGNMENT_MULTIPLIER = 0.09
COHESION_MULTIPLIER = 0.02

#  Species
SPECIES_AMOUNT = 1
SPECIES_SEPARATION_MULTIPLIER = 0.1
SPECIES_COLOR = [
    (255,0,0),  # Red
    (0,255,0),  # Green
    (0,0,255),  # Blue
    (255,255,0),  # Yellow
    (255,0,255),  # Purple
    (0,255,255),  # Cyan
    (255,255,255),  # White
    (0,0,0),  # Black
    (127,127,127), # Gray
    (255,127,0),  # Orange
    (0,255,127),  # Teal
]

#  Path following
UNBOUND = 0
FOLLOW_MOUSE = 1
FOLLOW_PATH_LIST = 2

BOID_FOLLOW_BEHAVIOUR = UNBOUND
# BOID_FOLLOW_BEHAVIOUR = FOLLOW_MOUSE
# BOID_FOLLOW_BEHAVIOUR = FOLLOW_PATH_LIST

GLOBAL_GOAL_MULTIPLIER = 0.05

PATH_LIST = [Vector2(640, 80), Vector2(80, 360), Vector2(640, 640), Vector2(1200, 360)]
# PATH_LIST = [Vector2(80, 360), Vector2(1200, 360)]

GLOAL_REACH_THRESHOLD = 20
# GOAL_COLOR = (255, 255, 255)
GOAL_COLOR = (0, 0, 153)