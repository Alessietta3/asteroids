import pygame
from logger import log_state
from circleshape import CircleShape
from player import  Player 
from constants import SCREEN_WIDTH , SCREEN_HEIGHT 
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
    player=Player( x , y )



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        dt=game_clock.tick(60)/1000
        player.draw(screen)


        

        pygame.display.flip()


    


if __name__ == "__main__":
    main()
