import pygame as pg
from pygame.math import Vector2
from globals import *


IMAGE = pg.image.load('sprites/boid.png')
# IMAGE = pg.transform.scale(IMAGE, (BOID_SPRITE_SIZE * BOID_SCALE, BOID_SPRITE_SIZE * BOID_SCALE))

class Boid(pg.sprite.Sprite):

    def __init__(self, position, velocity, group):
        pg.sprite.Sprite.__init__(self)
        self.radius = VISION_RANGE
        self.velocity = velocity
        self.image = IMAGE
        # self.color = color
        self.rect = self.image.get_rect(center=position)
        self.group = group
        self.color = pg.Color(SPECIES_COLOR[group])

        # set image color
        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                self.color.a = self.image.get_at((x, y)).a  # Preserve the alpha value.
                self.image.set_at((x, y), self.color)  # Set the color of the pixel.
        self.colored_image = self.image.copy()   # Save the colored image.

        self.rotate()

        if BOID_FOLLOW_BEHAVIOUR == FOLLOW_PATH_LIST:
            self.path_index = 0


    def rotate(self):
        self.image = pg.transform.rotate(self.colored_image, -self.velocity.normalize().as_polar()[1])
        self.rect = self.image.get_rect(center=self.rect.center)


    def update(self, all_others):
        separation = Vector2(0, 0)
        alignment = Vector2(0, 0)
        cohesion = Vector2(0, 0)
        center = Vector2(self.rect.center)

        neighbors = pg.sprite.spritecollide(self, all_others, False, pg.sprite.collide_circle)
        N = len(neighbors) - 1

        if N > 0:  # Boid has neighbors
            for neighbor in neighbors:
                if neighbor != self:
                    neighbor_center = Vector2(neighbor.rect.center) 
                    
                    pos_diff = neighbor_center - center
                    
                    #  Check neighbor's species
                    if neighbor.group != self.group:
                        #  If from different species, intensify separation rule
                        separation -= (SPECIES_SEPARATION_MULTIPLIER * pos_diff)
                    
                    if pos_diff.length() < SEPARATION_THRESHOLD:
                        separation -= pos_diff

                    alignment += neighbor.velocity

                    cohesion += neighbor_center
            
            alignment = alignment / N
            alignment = (alignment - self.velocity)

            cohesion = cohesion / N
            cohesion = (cohesion - center)

            #  update boid velocity
            self.velocity += (separation * SEPARATION_MULTIPLIER) + (alignment * ALIGNMENT_MULTIPLIER) + (cohesion * COHESION_MULTIPLIER)

            if BOID_FOLLOW_BEHAVIOUR == FOLLOW_MOUSE:
                mouse_pos = Vector2(pg.mouse.get_pos())
                pos_diff = mouse_pos - center
                self.velocity += (pos_diff * GLOBAL_GOAL_MULTIPLIER)
            elif BOID_FOLLOW_BEHAVIOUR == FOLLOW_PATH_LIST:
                goal_pos = Vector2(PATH_LIST[self.path_index])
                pos_diff = goal_pos - center
                if pos_diff.length() <= GLOAL_REACH_THRESHOLD:
                    self.path_index += 1
                    if self.path_index >= len(PATH_LIST):
                        self.path_index = 0
                self.velocity += (pos_diff * GLOBAL_GOAL_MULTIPLIER)

        #  limit velocity
        if self.velocity.length() > MAX_SPEED:
            self.velocity = self.velocity.normalize() * MAX_SPEED

        #  update position
        center += self.velocity

        #  Bound to screen
        if center.x > WIDTH:
            center.x = 0
        elif center.x < 0:
            center.x = WIDTH

        if center.y > HEIGHT:
            center.y = 0
        elif center.y < 0:
            center.y = HEIGHT

        #  move boid
        self.rect.center = (center[0], center[1])
        self.rotate()
