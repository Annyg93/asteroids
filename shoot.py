import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "red", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
