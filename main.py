import pygame
import os
import random
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
WIN_WIDTH, WIN_HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Hyper Turbo Space')
FPS = 60
MUSIC = True

# USER EVENTS -------------------------------------------------------------------------------------
NEXT_GAME_PHASE = pygame.USEREVENT + 1
NEXT_LEVEL = pygame.USEREVENT + 2
PLAYER_SHOT = pygame.USEREVENT + 3
START_GAME = pygame.USEREVENT + 4

# IMAGES ------------------------------------------------------------------------------------------
BG_IMAGES = {
    0: pygame.transform.scale(
        pygame.image.load(os.path.join('Images', 'Title_screen.png')), (WIN_WIDTH, WIN_HEIGHT)),
    1: pygame.transform.scale(
        pygame.image.load(os.path.join('Images', 'Space_background.png')), (WIN_WIDTH, WIN_HEIGHT)),
    2: pygame.transform.scale(
        pygame.image.load(os.path.join('Images', 'Space_background.png')), (WIN_WIDTH, WIN_HEIGHT))}
PLAYER_SHIP_IMG = pygame.image.load(os.path.join('Images', 'Player_ship_500x518.png'))
ENEMY_SHIP_IMAGES = {
    1: pygame.image.load(os.path.join('Images', 'Enemy_ship_1_500x275.png')),
    2: pygame.image.load(os.path.join('Images', 'Enemy_ship_2_500x299.png')),
    3: pygame.image.load(os.path.join('Images', 'Enemy_ship_3_500x419.png')),
    4: pygame.image.load(os.path.join('Images', 'Enemy_ship_4_500x126.png')),
    5: pygame.image.load(os.path.join('Images', 'Enemy_ship_5_500x341.png')),
    6: pygame.image.load(os.path.join('Images', 'Boss_ship_750x487.png'))}
SHOT_IMAGES = {
    'green': pygame.image.load(os.path.join('Images', 'Green_laser_200x38.png')),
    'red': pygame.image.load(os.path.join('Images', 'Red_laser_200x37.png')),
    'boss cannon': pygame.image.load(os.path.join('Images', 'Boss_cannon_laser_250x33.png'))}

# MUSIC -------------------------------------------------------------------------------------------
MUSIC_FILES = {
    0: os.path.join('Music', 'level_1_music.ogg'),
    1: os.path.join('Music', 'level_2_music.mp3'),
    2: os.path.join('Music', 'boss_music.mp3')
}

# SOUND EFFECTS --------------------------------------------------------------------------------------
PLAYER_SHOT_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'laser.wav'))


class PlayerShip:
    def __init__(self):
        self.height = 150
        self.width = 150
        self.x, self.y = 0, WIN_HEIGHT / 2 - self.height / 2
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(PLAYER_SHIP_IMG, (self.width, self.height))
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
            pygame.mixer.Sound.play(PLAYER_SHOT_SOUND)
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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class EnemyShip:
    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.ship_dict = {
            1: {
                'height': 275 // 5,
                'width': 100},
            2: {
                'height': 299 // 5,
                'width': 100},
            3: {
                'height': 419 // 5,
                'width': 100},
            4: {
                'height': 126 // 5,
                'width': 100},
            5: {
                'height': 341 // 5,
                'width': 100},
            6: {
                'height': 487 // 1.3,
                'width': 750 // 1.3
            }}
        self.height = self.ship_dict[self.ship_type]['height']
        self.width = self.ship_dict[self.ship_type]['width']
        self.x = random.randint(WIN_WIDTH // 2, WIN_WIDTH - self.width)
        self.y = random.randint(0, WIN_HEIGHT - self.height)
        self.speed = 3
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(ENEMY_SHIP_IMAGES[self.ship_type], (self.width, self.height))
        self.x_direction = random.choice([1, -1])
        self.y_direction = random.choice([1, -1])

    # todo implement random shooting?
    # def shoot(self, shots_on_screen):
    #     if len(shots_on_screen) < self.max_shots:
    #         self.gun_positions = {
    #             -1: (self.x + self.width, self.y + self.height * 0.33),
    #             1: (self.x + self.width, self.y + self.height * 0.66)}
    #         shot = Shot('player', self.gun_positions[self.shot_toggle])
    #         self.shot_toggle = self.shot_toggle * -1
    #         return shot
    #     return None

    def update(self):

        new_x = self.x + self.speed * self.x_direction
        new_y = self.y + self.speed * self.y_direction

        if new_x > WIN_WIDTH - self.width or new_x < WIN_WIDTH / 2:
            self.x_direction = self.x_direction * -1

        if new_y > WIN_HEIGHT - self.height or new_y < 0:
            self.y_direction = self.y_direction * -1

        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))
        return


class Shot:
    def __init__(self, shot_type, starting_coords):
        self.shot_type = shot_type
        self.shot_dict = {
            'player': {
                'height': 10,
                'width': 50,
                'image': SHOT_IMAGES['green'],
                'speed': 10},
            'enemy': {
                'height': 10,
                'width': 50,
                'image': SHOT_IMAGES['red'],
                'speed': -10},
            'boss cannon': {
                'height': 20,
                'width': 100,
                'image': SHOT_IMAGES['boss cannon'],
                'speed': -15
            }
        }
        self.height = self.shot_dict[self.shot_type]['height']
        self.width = self.shot_dict[self.shot_type]['width']
        self.x, self.y = starting_coords
        self.speed = self.shot_dict[self.shot_type]['speed']
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(self.shot_dict[self.shot_type]['image'], (self.width, self.height))

    def update(self):
        self.x += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class MainApp:
    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.win = window
        self.run = True
        self.level = 0
        self.game_phase = 0
        self.change_game_phase = [1, 5]
        self.player = PlayerShip()
        self.ships_on_screen = []
        self.player_shots_on_screen = []
        self.enemy_shots_on_screen = []
        self.level_spawns = {  # todo make this work
            0: [(0, 0)],
            1: [(1, 1), (2, 1)],
            2: [(2, 3)],
            3: [(3, 1), (4, 1)],
            4: [(4, 1), (1, 5)],
            5: [(6, 1)]
        }

    def check_events(self):
        event_dict = {
            pygame.QUIT: self.event_quit,
            NEXT_GAME_PHASE: self.event_next_level,
        }

        for event in pygame.event.get():
            if event.type in event_dict:
                event_dict[event.type]()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.event_next_level()
                    if self.level == 1:
                        self.game_phase = 1
                if event.key == pygame.K_SPACE:
                    shot = self.player.shoot(self.player_shots_on_screen)
                    if shot is not None:
                        self.player_shots_on_screen.append(shot)
        return

    def event_quit(self):
        self.run = False
        pygame.quit()
        return

    def event_next_game_phase(self):
        self.game_phase += 1
        if MUSIC:
            pygame.mixer.music.load(MUSIC_FILES[self.game_phase])
            pygame.mixer.music.play(-1, 0.0)

    def event_next_level(self):
        self.level += 1
        if self.level in self.change_game_phase:
            self.event_next_game_phase()
        enemies_to_spawn = self.level_spawns[self.level]
        for spawn in enemies_to_spawn:
            print(spawn)
            self.spawn_enemies(spawn)
        return

    def spawn_enemies(self, spawn_data):
        ship_type, number = spawn_data
        for i in range(0, number):
            ship = EnemyShip(ship_type)
            self.ships_on_screen.append(ship)

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

    def update_enemy_ships(self):
        for ship in self.ships_on_screen:
            ship.update()
        return

    def draw(self, keys_pressed):
        self.win.blit(BG_IMAGES[self.game_phase], (0, 0))
        if self.level > 0:
            self.player.update(keys_pressed)
            self.player.draw()
            self.update_shots()
            self.update_enemy_ships()
            for ship in self.ships_on_screen:
                ship.draw()
            for shot in self.player_shots_on_screen:
                shot.draw()
            for shot in self.enemy_shots_on_screen:
                shot.draw()
        pygame.display.update()
        return

    def main(self):
        if MUSIC:
            pygame.mixer.music.load(MUSIC_FILES[self.level])
            pygame.mixer.music.play(-1, 0.0)
        while self.run:
            self.clock.tick(FPS)
            self.check_events()
            keys_pressed = pygame.key.get_pressed()
            self.draw(keys_pressed)
        return


game = MainApp(WIN)

if __name__ == '__main__':
    game.main()
