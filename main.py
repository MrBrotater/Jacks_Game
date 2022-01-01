import pygame
import os
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graveyard Maze')
FPS = 30
NINJA_SIZE = 125
WHITE = [255, 255, 255]


# NINJA FRAME IMAGES --------------------------------------------------------------------------------
NINJA_FILES = os.listdir(os.path.join('Images', 'Ninja', 'Testing'))
NINJA_FRAMES = [pygame.image.load(os.path.join('Images', 'Ninja', 'Testing', file)) for file in NINJA_FILES]


# NINJA ---------------------------------------------------------------------------------------------
class Ninja(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.image = pygame.transform.scale(NINJA_FRAMES[self.frame], (NINJA_SIZE, NINJA_SIZE))

    def update(self):

        self.frame += 1
        if self.frame > len(NINJA_FRAMES) - 1:
            self.frame = 0

        self.image = pygame.transform.scale(NINJA_FRAMES[self.frame], (NINJA_SIZE, NINJA_SIZE))

    def draw(self):
        WIN.blit(self.image, (500, 500))


# DRAWING -------------------------------------------------------------------------------------------
def draw(ninja):
    WIN.fill(WHITE)
    WIN.blit(ninja.image, (500, 500))
    ninja.draw()
    pygame.display.update()
    return


# MAIN LOOP -------------------------------------------------------------------------------------------
def main():
    clock = pygame.time.Clock()
    run = True
    ninja1 = Ninja()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        ninja1.update()
        draw(ninja1)
    return


if __name__ == '__main__':
    main()