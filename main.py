import pygame as pg
import random as rng
from globals import *

# rng.seed(SEED)
clock = pg.time.Clock()
# bg = pg.image.load('sprites/background.jpg')
# bg = pg.transform.scale(bg, (WIDTH, HEIGHT))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Boids')

    from boids import Boid

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    #  Generate boids
    boids_group = pg.sprite.Group()
    for _ in range(BOIDS_AMOUNT):
        group = rng.randint(0, SPECIES_AMOUNT - 1)
        boid = Boid(
            position=(rng.random() * WIDTH, rng.random() * HEIGHT), 
            velocity=pg.math.Vector2(rng.random() - 0.5, rng.random() - 0.5) * MAX_SPEED,
            # color=pg.Color(rng.randint(0, 200), rng.randint(200, 255), 0),
            # color=pg.Color(200, group * (255 // SPECIES_AMOUNT), group * (255 // SPECIES_AMOUNT)),
            group=group
        )
        boids_group.add(boid)

    # Game loop
    running = True
    while running:
        # Input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    main()
                if event.key == pg.K_q:
                    running = False

        # Update
        for boid in boids_group:
            boid.update(boids_group)
        
        # Draw
        screen.blit(background, (0, 0))
        # screen.blit(bg, (0, 0))
        #  Mark goals for pathfinding
        if BOID_FOLLOW_BEHAVIOUR == FOLLOW_PATH_LIST:
            for i in range(len(PATH_LIST)):
                pg.draw.circle(screen, pg.Color(GOAL_COLOR), PATH_LIST[i], GLOAL_REACH_THRESHOLD)

        
        boids_group.draw(screen)
        pg.display.flip()
        
        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()