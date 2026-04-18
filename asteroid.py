from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # signature form parent alfeady sets up the paraeetres
        super().__init__(x, y, radius)
 
        self.radius=radius
    def draw(self, screen):
        pygame.draw.circle(screen , "white" , self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position+=self.velocity*dt
    def split(self):
        #kill itself
        self.kill()
        #If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS,
        #  just return; this was a small asteroid and we're done.
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        else:


            log_event("asteroid_split")
            rand_angle= random.uniform(20, 50)
            new_asteroid_1_vec= self.velocity.rotate(rand_angle)
            new_asteroid_2_vec= self.velocity.rotate(-rand_angle)
            
            old_radius=self.radius
            new_radius_asteroid=old_radius - ASTEROID_MIN_RADIUS

            new_asteroid_1= Asteroid(self.position.x, self.position.y, new_radius_asteroid)
            new_asteroid_2= Asteroid(self.position.x, self.position.y,  new_radius_asteroid)
            new_asteroid_1.velocity=new_asteroid_1_vec *1.2
            new_asteroid_2.velocity =new_asteroid_2_vec *1.2



        #Otherwise, we need to spawn 2 new asteroids like so
        #Call log_event("asteroid_split") (be sure to import log_event at the top of the file).
        #Call random.uniform to generate a random angle between 20 and 50 degrees 
        # (be sure to import the standard random library at the top of the file). 

        


