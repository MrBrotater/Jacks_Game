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
NEXT_GAME_PHASE = pygame.USEREVENT + 1
PLAYER_SHOT = pygame.USEREVENT + 2
START_GAME = pygame.USEREVENT + 3


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
        self.max_shots = 6

    def shoot(self, shots_on_screen):
        if len(shots_on_screen) < self.max_shots:
            self.gun_positions = {
                -1: (self.x + self.width, self.y + self.height * 0.33),
                1: (self.x + self.width, self.y + self.height * 0.66)}
            shot = Shot('player', self.gun_positions[self.shot_toggle])
            self.shot_toggle = self.shot_toggle * -1
            return shot
        return None

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x - self.speed > 0:  # LEFT
            self.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.x + self.speed + self.width < WIN_WIDTH:  # RIGHT
            self.x += self.speed
        if keys_pressed[pygame.K_UP] and self.y - self.speed > 0:  # UP
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.y + self.speed + self.height < WIN_HEIGHT:  # DOWN
            self.y += self.speed

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class Shot:
    def __init__(self, shot_type, starting_coords):
        self.shot_type = shot_type
        self.shot_dict = {
            'player': {
                'height': 10,
                'width': 50,
                'image': 'Green_laser_200x38.png',
                'speed': 10},
            'enemy': {
                'height': 10,
                'width': 50,
                'image': 'Red_laser_200x37.png',
                'speed': -10
            }
        }
        self.height = self.shot_dict[self.shot_type]['height']
        self.width = self.shot_dict[self.shot_type]['width']
        self.x, self.y = starting_coords
        self.speed = self.shot_dict[self.shot_type]['speed']
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join(
                'Images', self.shot_dict[self.shot_type]['image'])), (self.width, self.height))

    def update(self):
        self.x += self.speed

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class MainApp:
    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.win = window
        self.run = True
        self.level = 0
        self.player = PlayerShip()
        self.ships_on_screen = []
        self.player_shots_on_screen = []
        self.enemy_shots_on_screen = []
        self.BG_IMAGES = {
            0: pygame.transform.scale(
                pygame.image.load(os.path.join('Images', 'Title_screen.png')), (WIN_WIDTH, WIN_HEIGHT)),
            1: pygame.transform.scale(
                pygame.image.load(os.path.join('Images', 'Space_background.png')), (WIN_WIDTH, WIN_HEIGHT))}

    def check_events(self):
        event_dict = {
            pygame.QUIT: self.event_quit,
            NEXT_GAME_PHASE: self.event_next_phase,
        }

        for event in pygame.event.get():
            if event.type in event_dict:
                event_dict[event.type]()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.level == 0:
                    self.level += 1
                if event.key == pygame.K_SPACE:
                    shot = self.player.shoot(self.player_shots_on_screen)
                    if shot is not None:
                        self.player_shots_on_screen.append(shot)
        return

    def event_quit(self):
        self.run = False
        pygame.quit()
        return

    def event_next_phase(self):
        self.level += 1
        return

    def update_shots(self):
        for shot in self.player_shots_on_screen:
            shot.update()
            if shot.x > WIN_WIDTH - shot.width:
                self.player_shots_on_screen.remove(shot)
        for shot in self.enemy_shots_on_screen:
            shot.update()
            if shot.x < 0:
                self.enemy_shots_on_screen.remove(shot)
        return


    def draw(self, keys_pressed):
        self.win.blit(self.BG_IMAGES[self.level], (0, 0))
        if self.level > 0:
            self.player.update(keys_pressed)
            self.player.draw()
            self.update_shots()
            for ship in self.ships_on_screen:
                ship.draw()
            for shot in self.player_shots_on_screen:
                shot.draw()
            for shot in self.enemy_shots_on_screen:
                shot.draw()
        pygame.display.update()
        return

    def main(self):
        while self.run:
            self.clock.tick(FPS)
            self.check_events()
            keys_pressed = pygame.key.get_pressed()
            self.draw(keys_pressed)

        return


game = MainApp(WIN)

if __name__ == '__main__':
    game.main()
