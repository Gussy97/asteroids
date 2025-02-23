from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        new_vel1 = self.velocity.rotate(angle) 
        new_vel2 = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid.velocity = new_vel1 * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid.velocity = new_vel2 * 1.2


    