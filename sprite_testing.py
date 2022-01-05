import pygame
import os

import pygame
import sys
import os
import random
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
WIN_WIDTH, WIN_HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Hyper Turbo Space')
FPS = 60

# IMAGES ------------------------------------------------------------------------------------------
BG_IMG_0 = pygame.image.load(os.path.join('Images', 'Title_screen.png'))
BG_IMG_1 = pygame.image.load(os.path.join('Images', 'Space_background.png'))
BG_IMG_2 = pygame.image.load(os.path.join('Images', 'Space_background.png'))

PLAYER_SHIP_IMG = pygame.image.load(os.path.join('Images', 'Player_ship_500x518.png'))

ENEMY_SHIP_1_IMG = pygame.image.load(os.path.join('Images', 'Enemy_ship_1_500x275.png'))
ENEMY_SHIP_2_IMG = pygame.image.load(os.path.join('Images', 'Enemy_ship_2_500x299.png'))
ENEMY_SHIP_3_IMG = pygame.image.load(os.path.join('Images', 'Enemy_ship_3_500x419.png'))
ENEMY_SHIP_4_IMG = pygame.image.load(os.path.join('Images', 'Enemy_ship_4_500x126.png'))
ENEMY_SHIP_5_IMG = pygame.image.load(os.path.join('Images', 'Enemy_ship_5_500x341.png'))

BOSS_SHIP_IMG = pygame.image.load(os.path.join('Images', 'Boss_ship_750x487.png'))

PROJ_GREEN_IMG = pygame.image.load(os.path.join('Images', 'Green_laser_200x38.png'))
PROJ_RED_IMG = pygame.image.load(os.path.join('Images', 'Red_laser_200x37.png'))
PROJ_BOSS_IMG = pygame.image.load(os.path.join('Images', 'Boss_cannon_laser_250x33.png'))

SHIPS_ON_SCREEN = pygame.sprite.Group()

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(SHIPS_ON_SCREEN)
        self.image = pygame.transform.scale(PLAYER_SHIP_IMG, (150, 150))
        self.rect = self.image.get_rect()
        self.x_pos, self.y_pos = 0, WIN_HEIGHT / 2 - 150 / 2


# class MainApp:
#     def __init__(self, window):
#         self.clock = pygame.time.Clock()
#         self.win = window
#         self.run = True
#
#         player = PlayerShip()
#         ships_on_screen = pygame.sprite.Group()
#         ships_on_screen.add(player)
#
#     def check_events(self):
#         event_dict = {
#             pygame.QUIT: self.event_quit
#         }
#
#         for event in pygame.event.get():
#
#             if event.type in event_dict:
#                 event_dict[event.type]()
#
#         return
#
#     def event_quit(self):
#         self.run = False
#         pygame.quit()
#         return
#
#     def main(self):
#         while self.run:
#             self.ships_on_screen.draw(self.win)
#         return
#
# game = MainApp(WIN)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

        SHIPS_ON_SCREEN.draw(WIN)
        pygame.display.flip()



if __name__ == '__main__':
    # game.main()

    player = PlayerShip()
    main()