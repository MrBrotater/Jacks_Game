import pygame
import os
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
WIN_WIDTH, WIN_HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Hyper Turbo Space')
FPS = 60
PLAYER_SHIP_SIZE = 125
WHITE = [255, 255, 255]
MUSIC = True

# USER EVENTS -------------------------------------------------------------------------------------
PLAYER_SHOT = pygame.USEREVENT + 1


# BACKGROUND IMAGES ------------------------------------------------------------------------------
LEVEL_1_BG = pygame.transform.scale(
    pygame.image.load(os.path.join('Images', 'Space_background.png')), (WIN_WIDTH, WIN_HEIGHT))


# MUSIC -------------------------------------------------------------------------------------------
if MUSIC:
    pygame.mixer.music.load(os.path.join('Music', 'level_1_music.ogg'))
    pygame.mixer.music.play(-1, 0.0)


class PlayerShip:
    def __init__(self):
        self.height = 150
        self.width = 150
        self.x, self.y = 0, WIN_HEIGHT / 2 - self.height / 2
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('Images', 'Player_ship_500x518.png')), (self.width, self.height))
        self.shot_toggle = -1
        self.gun_positions = {
            -1: (self.x + self.width, self.y + self.height * 0.33),
            1: (self.x + self.width, self.y + self.height * 0.66)}
        self.shots_on_screen = []
        self.max_shots = 6

    def shoot(self):
        self.gun_positions = {
            -1: (self.x + self.width, self.y + self.height * 0.33),
            1: (self.x + self.width, self.y + self.height * 0.66)}
        self.shots_on_screen.append(PlayerShot(self.gun_positions[self.shot_toggle]))
        self.shot_toggle = self.shot_toggle * -1

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x - self.speed > 0:  # LEFT
            self.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.x + self.speed + self.width < WIN_WIDTH:  # RIGHT
            self.x += self.speed
        if keys_pressed[pygame.K_UP] and self.y - self.speed > 0:  # UP
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.y + self.speed + self.height < WIN_HEIGHT:  # DOWN
            self.y += self.speed

        for shot in self.shots_on_screen:
            shot.update()
            shot.draw()
            if shot.x > WIN_WIDTH - shot.width:
                self.shots_on_screen.remove(shot)

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class PlayerShot:
    def __init__(self, gun_position):
        self.height = 10
        self.width = 50
        self.x, self.y = gun_position
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('Images', 'Green_laser_200x38.png')), (self.width, self.height))

    def update(self):
        self.x += self.speed

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

# DRAWING -------------------------------------------------------------------------------------------
def draw(objects_on_screen, keys_pressed):
    WIN.blit(LEVEL_1_BG, (0, 0))
    for obj in objects_on_screen:
        obj.update(keys_pressed)
        obj.draw()
    pygame.display.update()
    return


# MAIN LOOP -------------------------------------------------------------------------------------------
def main():
    clock = pygame.time.Clock()
    run = True
    player = PlayerShip()
    objects_on_screen = [player]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player.shots_on_screen) < player.max_shots:
                    player.shoot()

        keys_pressed = pygame.key.get_pressed()
        draw(objects_on_screen, keys_pressed)

    return


if __name__ == '__main__':
    main()
