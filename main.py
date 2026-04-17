import pygame
from logger import log_state
from circleshape import CircleShape
from player import  Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
def main():
    pygame.init()

    
    dt =0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

 

    game_clock=pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))






    #game groups                  add features in parentesis
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()



 #  containers
    Player.containers = (updatable, drawable)

    AsteroidField.containers=(updatable,)

    Asteroid.containers = (asteroids, updatable, drawable)


        
    # objects
    player=Player(x, y)

    asteroidField=AsteroidField()
   






    





    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        dt=game_clock.tick(60)/1000
        for up in updatable:
            up.update(dt)
        for dr in drawable:
            dr.draw(screen)
        


        

        pygame.display.flip()


    


if __name__ == "__main__":
    main()
