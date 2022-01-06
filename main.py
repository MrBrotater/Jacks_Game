import pygame
import os
import random
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hyper Turbo Space')
FPS = 60
MUSIC_ON = True

# USER EVENTS -------------------------------------------------------------------------------------
NEXT_GAME_PHASE = pygame.USEREVENT + 1
NEXT_LEVEL = pygame.USEREVENT + 2
PLAYER_SHOT = pygame.USEREVENT + 3

# IMAGE SCALING -----------------------------------------------------------------------------------
PLAYER_SHIP_TGT_WIDTH = 150
ENEMY_SHIP_TGT_WIDTH = 100
BOSS_SHIP_TGT_WIDTH = 500
PROJ_STD_TGT_WIDTH = 50
PROJ_BOSS_TGT_WIDTH = 100

PLAYER_SHIP_SCALE_FACTOR = 500 / PLAYER_SHIP_TGT_WIDTH
ENEMY_SHIP_SCALE_FACTOR = 500 / ENEMY_SHIP_TGT_WIDTH
BOSS_SHIP_SCALE_FACTOR = 750 / BOSS_SHIP_TGT_WIDTH
PROJ_STD_SCALE_FACTOR = 200 / PROJ_STD_TGT_WIDTH
PROJ_BOSS_SCALE_FACTOR = 250 / PROJ_BOSS_TGT_WIDTH

IMAGE_SIZES = {
    'background': (SCREEN_WIDTH, SCREEN_HEIGHT),
    'player ship': (500 // PLAYER_SHIP_SCALE_FACTOR, 518 // PLAYER_SHIP_SCALE_FACTOR),
    'enemy ship 1': (500 // ENEMY_SHIP_SCALE_FACTOR, 275 // ENEMY_SHIP_SCALE_FACTOR),
    'enemy ship 2': (500 // ENEMY_SHIP_SCALE_FACTOR, 299 // ENEMY_SHIP_SCALE_FACTOR),
    'enemy ship 3': (500 // ENEMY_SHIP_SCALE_FACTOR, 419 // ENEMY_SHIP_SCALE_FACTOR),
    'enemy ship 4': (500 // ENEMY_SHIP_SCALE_FACTOR, 126 // ENEMY_SHIP_SCALE_FACTOR),
    'enemy ship 5': (500 // ENEMY_SHIP_SCALE_FACTOR, 341 // ENEMY_SHIP_SCALE_FACTOR),
    'boss ship': (750 // BOSS_SHIP_SCALE_FACTOR, 487 // BOSS_SHIP_SCALE_FACTOR),
    'green laser': (200 // PROJ_STD_SCALE_FACTOR, 38 // PROJ_STD_SCALE_FACTOR),
    'red laser': (200 // PROJ_STD_SCALE_FACTOR, 37 // PROJ_STD_SCALE_FACTOR),
    'boss laser': (250 // PROJ_BOSS_SCALE_FACTOR, 33 // PROJ_BOSS_SCALE_FACTOR)
}

# STATIC IMAGES ------------------------------------------------------------------------------------------
BG_TITLE_FULLSIZE = pygame.image.load(os.path.join('Images', 'Title_screen.png'))
BG_SPACE_FULLSIZE = pygame.image.load(os.path.join('Images', 'Space_background.png'))
PLAYER_SHIP_FULLSIZE = pygame.image.load(os.path.join('Images', 'Player_ship_500x518.png'))
ENEMY_SHIP_1_FULLSIZE = pygame.image.load(os.path.join('Images', 'Enemy_ship_1_500x275.png'))
ENEMY_SHIP_2_FULLSIZE = pygame.image.load(os.path.join('Images', 'Enemy_ship_2_500x299.png'))
ENEMY_SHIP_3_FULLSIZE = pygame.image.load(os.path.join('Images', 'Enemy_ship_3_500x419.png'))
ENEMY_SHIP_4_FULLSIZE = pygame.image.load(os.path.join('Images', 'Enemy_ship_4_500x126.png'))
ENEMY_SHIP_5_FULLSIZE = pygame.image.load(os.path.join('Images', 'Enemy_ship_5_500x341.png'))
BOSS_SHIP_FULLSIZE = pygame.image.load(os.path.join('Images', 'Boss_ship_750x487.png'))
PROJ_GREEN_FULLSIZE = pygame.image.load(os.path.join('Images', 'Green_laser_200x38.png'))
PROJ_RED_FULLSIZE = pygame.image.load(os.path.join('Images', 'Red_laser_200x37.png'))
PROJ_BOSS_FULLSIZE = pygame.image.load(os.path.join('Images', 'Boss_cannon_laser_250x33.png'))

BG_TITLE_IMAGE = pygame.transform.scale(BG_TITLE_FULLSIZE, IMAGE_SIZES['background'])
BG_SPACE_IMAGE = pygame.transform.scale(BG_SPACE_FULLSIZE, IMAGE_SIZES['background'])
PLAYER_SHIP_IMAGE = pygame.transform.scale(PLAYER_SHIP_FULLSIZE, IMAGE_SIZES['player ship'])
ENEMY_SHIP_1_IMAGE = pygame.transform.scale(ENEMY_SHIP_1_FULLSIZE, IMAGE_SIZES['enemy ship 1'])
ENEMY_SHIP_2_IMAGE = pygame.transform.scale(ENEMY_SHIP_2_FULLSIZE, IMAGE_SIZES['enemy ship 2'])
ENEMY_SHIP_3_IMAGE = pygame.transform.scale(ENEMY_SHIP_3_FULLSIZE, IMAGE_SIZES['enemy ship 3'])
ENEMY_SHIP_4_IMAGE = pygame.transform.scale(ENEMY_SHIP_4_FULLSIZE, IMAGE_SIZES['enemy ship 4'])
ENEMY_SHIP_5_IMAGE = pygame.transform.scale(ENEMY_SHIP_5_FULLSIZE, IMAGE_SIZES['enemy ship 5'])
BOSS_SHIP_IMAGE = pygame.transform.scale(BOSS_SHIP_FULLSIZE, IMAGE_SIZES['boss ship'])
PROJ_GREEN_IMAGE = pygame.transform.scale(PROJ_GREEN_FULLSIZE, IMAGE_SIZES['green laser'])
PROJ_RED_IMAGE = pygame.transform.scale(PROJ_RED_FULLSIZE, IMAGE_SIZES['red laser'])
PROJ_BOSS_IMAGE = pygame.transform.scale(PROJ_BOSS_FULLSIZE, IMAGE_SIZES['boss laser'])

ENEMY_SHIP_IMG_DICT = {
    1: ENEMY_SHIP_1_IMAGE,
    2: ENEMY_SHIP_2_IMAGE,
    3: ENEMY_SHIP_3_IMAGE,
    4: ENEMY_SHIP_4_IMAGE,
    5: ENEMY_SHIP_5_IMAGE
}

PHASE_BG_DICT = {
    0: BG_TITLE_IMAGE,
    1: BG_SPACE_IMAGE,
    2: BG_SPACE_IMAGE
}

# ANIMATIONS --------------------------------------------------------------------------------------
EXPLOSION_FILES = os.listdir(os.path.join('Images', 'explosion'))
EXPLOSION_FRAMES_FULLSIZE = [pygame.image.load(os.path.join('Images', 'explosion', frame)) for frame in EXPLOSION_FILES]
EXPLOSION_FRAMES = [pygame.transform.scale(image, (100, 100)) for image in EXPLOSION_FRAMES_FULLSIZE]

# MUSIC -------------------------------------------------------------------------------------------
PHASE_0_MUSIC = os.path.join('Music', 'level_1_music.ogg')
PHASE_1_MUSIC = os.path.join('Music', 'level_2_music.mp3')
PHASE_2_MUSIC = os.path.join('Music', 'boss_music.mp3')

MUSIC_FILE_DICT = {
    0: PHASE_0_MUSIC,
    1: PHASE_1_MUSIC,
    2: PHASE_2_MUSIC
}

# SOUND EFFECTS --------------------------------------------------------------------------------------
PLAYER_LASER_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'player_laser.wav'))
BOSS_CANNON_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'boss_cannon.wav'))
ENEMY_HIT_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'enemy_hit.wav'))
PLAYER_SHIP_HIT_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'player_ship_hit.wav'))


# PLAYER SHIP CLASS --------------------------------------------------------------------------------------------------
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_SHIP_IMAGE
        self.rect = self.image.get_rect()
        self.x_pos, self.y_pos = self.image.get_width() // 2, SCREEN_HEIGHT / 2
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = 10
        self.max_shots = 6

    def shoot(self, sprite_group):
        if len(sprite_group.sprites()) < self.max_shots:
            proj = Projectile(PROJ_GREEN_IMAGE, self.rect.midright, 1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            return proj
        return None

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.x_pos - self.speed > 0:  # LEFT
            self.x_pos -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.x_pos + self.speed + self.image.get_width() < SCREEN_WIDTH:  # RIGHT
            self.x_pos += self.speed
        if keys_pressed[pygame.K_UP] and self.y_pos - self.speed > 0:  # UP
            self.y_pos -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.y_pos + self.speed + self.image.get_height() < SCREEN_HEIGHT:  # DOWN
            self.y_pos += self.speed
        self.rect.center = (self.x_pos, self.y_pos)


# PROJECTILE CLASS ----------------------------------------------------------------------------------------------------
class Projectile(pygame.sprite.Sprite):
    def __init__(self, img, position, direction):
        super().__init__()
        self.image = img
        self.x_pos, self.y_pos = position
        self.speed = 10
        self.direction = direction
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        self.x_pos += self.speed * self.direction
        self.rect.center = (self.x_pos, self.y_pos)
        if self.direction == 1 and self.rect.left > SCREEN_WIDTH:
            self.kill()
        if self.direction == -1 and self.rect.right < 0:
            self.kill()

    def collide(self):
        self.kill()


# ENEMY SHIP CLASS -----------------------------------------------------------------------------------------------------
class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, ship_type):
        super().__init__()
        self.image = ENEMY_SHIP_IMG_DICT[ship_type]
        self.rect = self.image.get_rect()
        self.x_pos = random.randint(
            SCREEN_WIDTH // 2 + self.image.get_width() // 2,
            SCREEN_WIDTH - self.image.get_width() // 2)
        self.y_pos = random.randint(self.image.get_height() // 2, SCREEN_HEIGHT - self.image.get_height() // 2)
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = 3
        self.x_direction = random.choice([1, -1])
        self.y_direction = random.choice([1, -1])
        self.current_explosion_frame = 0
        self.explosion_frames = EXPLOSION_FRAMES
        self.total_explosion_frames = len(self.explosion_frames)
        self.exploding = False

    def update(self):
        if not self.exploding:
            if self.x_direction == 1 and self.rect.right + self.speed > SCREEN_WIDTH:
                self.x_direction = self.x_direction * -1
            if self.x_direction == -1 and self.rect.left - self.speed < SCREEN_WIDTH // 2:
                self.x_direction = self.x_direction * -1
            if self.y_direction == 1 and self.rect.bottom + self.speed > SCREEN_HEIGHT:
                self.y_direction = self.y_direction * -1
            if self.y_direction == -1 and self.rect.top - self.speed < 0:
                self.y_direction = self.y_direction * -1

            self.x_pos += self.speed * self.x_direction
            self.y_pos += self.speed * self.y_direction

            self.rect.center = (self.x_pos, self.y_pos)
        return

    def check_collision(self, projectiles):
        if not self.exploding:
            for projectile in projectiles:
                if self.rect.colliderect(projectile.rect):
                    projectile.kill()
                    self.exploding = True

    def draw(self, window):  # todo this is not working right
        if not self.exploding:
            window.blit(self.image, self.rect.topleft)
        else:
            if self.current_explosion_frame > self.total_explosion_frames:
                self.kill()
                return
            window.blit(self.image, self.rect.topleft)
            window.blit(self.explosion_frames[self.current_explosion_frame], self.rect.topleft)
            self.current_explosion_frame += 1


# BOSS SHIP CLASS -----------------------------------------------------------------------------------------------------
class BossShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = BOSS_SHIP_IMAGE
        self.rect = self.image.get_rect()
        self.x_pos = random.randint(
            SCREEN_WIDTH // 2 + self.image.get_width() // 2,
            SCREEN_WIDTH - self.image.get_width() // 2)
        self.y_pos = random.randint(self.image.get_height() // 2, SCREEN_HEIGHT - self.image.get_height() // 2)
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = 3
        self.x_direction = random.choice([1, -1])
        self.y_direction = random.choice([1, -1])
        self.hit_box = (self.rect.right - self.rect.width * 0.25, self.rect.top,
                        self.rect.width * 0.25, self.rect.height * 0.25)

    def update(self):
        if self.x_direction == 1 and self.rect.right + self.speed > SCREEN_WIDTH:
            self.x_direction = self.x_direction * -1
        if self.x_direction == -1 and self.rect.left - self.speed < SCREEN_WIDTH // 2:
            self.x_direction = self.x_direction * -1
        if self.y_direction == 1 and self.rect.bottom + self.speed > SCREEN_HEIGHT:
            self.y_direction = self.y_direction * -1
        if self.y_direction == -1 and self.rect.top - self.speed < 0:
            self.y_direction = self.y_direction * -1

        self.x_pos += self.speed * self.x_direction
        self.y_pos += self.speed * self.y_direction

        self.rect.center = (self.x_pos, self.y_pos)
        self.hit_box = (self.rect.right - self.rect.width * 0.25, self.rect.top,
                        self.rect.width * 0.25, self.rect.height * 0.25)
        return


# MAIN APP CLASS ------------------------------------------------------------------------------------------------------
class MainApp:
    def __init__(self, window):
        self.clock = pygame.time.Clock()
        self.win = window
        self.run = True
        self.BG = PHASE_BG_DICT[0]
        self.level = 0
        self.game_phase = 0
        self.change_game_phase = [1, 5]
        self.enemies_on_screen = pygame.sprite.Group()
        self.player = PlayerShip()
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.player_projectiles_on_screen = pygame.sprite.Group()
        self.enemy_projectiles_on_screen = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(
            self.player_group.sprites(),
            self.player_projectiles_on_screen.sprites(),
            self.enemy_projectiles_on_screen.sprites())
        self.level_spawns = {
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
                    shot = self.player.shoot(self.player_projectiles_on_screen)
                    if shot is not None:
                        self.player_projectiles_on_screen.add(shot)
                        self.all_sprites.add(shot)
        return

    def event_quit(self):
        self.run = False
        pygame.quit()
        return

    def event_next_game_phase(self):
        self.game_phase += 1
        if self.game_phase in self.change_game_phase:
            self.BG = PHASE_BG_DICT[self.game_phase]
        if MUSIC_ON:
            pygame.mixer.music.load(MUSIC_FILE_DICT[self.game_phase])
            pygame.mixer.music.play(-1, 0.0)

    def event_next_level(self):
        self.level_spawns = {
            1: [(1, 1), (2, 1)],
            2: [(2, 3)],
            3: [(3, 1), (4, 1)],
            4: [(4, 1), (1, 5)],
            5: [(6, 1)]
        }
        self.level += 1
        if self.level in self.change_game_phase:
            self.event_next_game_phase()
        if self.game_phase == 1:
            self.spawn_enemies(self.level_spawns[self.level])
        if self.game_phase == 2:
            self.spawn_boss()
        return

    def spawn_enemies(self, level_data):
        for spawn in level_data:
            ship_type = spawn[0]
            number = spawn[1]
            for i in range(number):
                ship = EnemyShip(ship_type)
                self.enemies_on_screen.add(ship)
                self.all_sprites.add(ship)

    def spawn_boss(self):
        ship = BossShip()
        self.enemies_on_screen.add(ship)
        self.all_sprites.add(ship)

    def main(self):
        while self.run:
            while self.game_phase == 0:
                self.clock.tick(FPS)
                self.check_events()
                self.win.blit(self.BG, (0, 0))
                pygame.display.flip()
            while self.game_phase == 1:
                self.clock.tick(FPS)
                self.check_events()
                self.win.blit(self.BG, (0, 0))
                self.all_sprites.update()
                for ship in self.enemies_on_screen.sprites():
                    ship.check_collision(self.player_projectiles_on_screen)
                self.all_sprites.draw(self.win)
                pygame.display.flip()
            while self.game_phase == 2:
                self.clock.tick(FPS)
                self.check_events()
                self.win.blit(self.BG, (0, 0))
                self.all_sprites.update()
                self.all_sprites.draw(self.win)
                pygame.display.flip()


# RUNTIME CODE ---------------------------------------------------------------------------------------------------------
game = MainApp(SCREEN)

if __name__ == '__main__':
    game.main()
