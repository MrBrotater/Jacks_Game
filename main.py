import pygame
import os
import random
from time import sleep
pygame.init()

# GAME WINDOW -----------------------------------------------------------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hyper Turbo Space')
FPS = 60
MUSIC_ON = True

# ENEMY WAVE DICTIONARY ------------------------------------------------------------------------------
LEVEL_DATA = {
    1: [(1, 1), (2, 1)],
    2: [(2, 3)],
    3: [(3, 1), (4, 1)],
    4: [(4, 1), (1, 5)],
    5: [(6, 1)]
}

# USER EVENTS -------------------------------------------------------------------------------------
NEXT_GAME_PHASE = pygame.USEREVENT + 1
NEXT_LEVEL = pygame.USEREVENT + 2
PLAYER_SHOT = pygame.USEREVENT + 3
GAME_LOST = pygame.USEREVENT + 4
GAME_WON = pygame.USEREVENT + 5

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
EXPLOSION_FRAMES = [pygame.transform.scale(image, (250, 250)) for image in EXPLOSION_FRAMES_FULLSIZE]

# MUSIC -------------------------------------------------------------------------------------------
PHASE_0_MUSIC = os.path.join('Music', 'phase_0_music.ogg')
PHASE_1_MUSIC = os.path.join('Music', 'phase_1_music.mp3')
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
PLAYER_SHIP_HIT_SOUND = pygame.mixer.Sound(os.path.join('Sound Effects', 'explosion3.wav'))


# FONTS -------------------------------------------------------------
FONT_1 = pygame.font.SysFont('comicsans', SCREEN_HEIGHT // 20)
FONT_2 = pygame.font.SysFont('comicsans', SCREEN_HEIGHT // 4)


# PLAYER SHIP CLASS --------------------------------------------------------------------------------------------------
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_SHIP_IMAGE
        self.rect = self.image.get_rect()
        self.x_pos, self.y_pos = self.image.get_width() // 2, SCREEN_HEIGHT / 2
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = 10
        self.max_shots = 12
        self.health = 10
        self.heath_txt = FONT_1.render(f'Health: {self.health}', True, (255, 255, 255))
        self.current_explosion_frame = 0
        self.explosion_frames = EXPLOSION_FRAMES
        self.total_explosion_frames = len(self.explosion_frames)
        self.exploding = False

    def shoot(self, sprite_group):
        if len(sprite_group.sprites()) < self.max_shots:
            shots = [
                Projectile(PROJ_GREEN_IMAGE, (self.rect.right, self.rect.top + self.rect.height * 0.3), 1),
                Projectile(PROJ_GREEN_IMAGE, (self.rect.right, self.rect.top + self.rect.height * 0.7), 1)]
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            return shots
        return []

    def hit(self):
        self.health -= 1
        self.heath_txt = FONT_1.render(f'Health: {self.health}', True, (255, 255, 255))
        pygame.mixer.Sound.play(PLAYER_SHIP_HIT_SOUND)
        if self.health == 0:
            pygame.event.post(pygame.event.Event(GAME_LOST))

    def check_collision(self, projectiles):
        if not self.exploding:
            for projectile in projectiles:
                if self.rect.colliderect(projectile.rect):
                    projectile.kill()
                    self.hit()

    def update(self):
        if not self.exploding:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:  # LEFT
                self.x_pos -= self.speed
            if keys_pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:  # RIGHT
                self.x_pos += self.speed
            if keys_pressed[pygame.K_UP] and self.rect.top > 0:  # UP
                self.y_pos -= self.speed
            if keys_pressed[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:  # DOWN
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


# EXPLOSION CLASS ------------------------------------------------------------------------------------------------------
class Explosion(pygame.sprite.Sprite):
    def __init__(self, ship_img, position):
        super().__init__()
        self.ship_iamge = ship_img
        self.explosion_frames = EXPLOSION_FRAMES
        self.total_frames = len(EXPLOSION_FRAMES)
        self.current_frame = 0
        self.image = EXPLOSION_FRAMES[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        self.current_frame += 1
        if self.current_frame == self.total_frames:
            self.kill()
        else:
            self.image = EXPLOSION_FRAMES[self.current_frame]


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
        else:
            self.kill()
        return

    def check_collision(self, projectiles):
        if not self.exploding:
            for projectile in projectiles:
                if self.rect.colliderect(projectile.rect):
                    projectile.kill()
                    pygame.mixer.Sound.play(ENEMY_HIT_SOUND)
                    explosion = Explosion(self.image, self.rect.center)
                    self.exploding = True
                    return explosion

    def shoot(self, sprite_group):
        rand = random.randint(0, 500)
        if rand > 495:
            shot = Projectile(PROJ_RED_IMAGE, self.rect.midleft, -1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            sprite_group.add(shot)


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
        self.health = 10
        self.hit_box = pygame.Rect(self.rect.right, self.rect.top,
                        self.rect.width * 0.20, self.rect.height * 0.20)

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
        self.hit_box.topright = self.rect.topright

    def check_collision(self, projectiles):
        for projectile in projectiles:
            if self.hit_box.colliderect(projectile.rect):
                projectile.kill()
                pygame.mixer.Sound.play(ENEMY_HIT_SOUND)
                self.health -= 1
                if self.health == 0:
                    pygame.event.post(pygame.event.Event(GAME_WON))
                    self.kill()
                return

    def shoot(self, sprite_group):
        gun_1 = random.randint(0, 500)
        if gun_1 > 495:
            shot = Projectile(PROJ_RED_IMAGE, (self.x_pos, self.y_pos - 50), -1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            sprite_group.add(shot)
        gun_2 = random.randint(0, 500)
        if gun_2 > 495:
            shot = Projectile(PROJ_RED_IMAGE, (self.x_pos, self.y_pos), -1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            sprite_group.add(shot)
        gun_3 = random.randint(0, 500)
        if gun_3 > 490:
            shot = Projectile(PROJ_RED_IMAGE, (self.x_pos, self.y_pos + 50), -1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            sprite_group.add(shot)
        gun_4 = random.randint(0, 500)
        if gun_4 > 490:
            shot = Projectile(PROJ_RED_IMAGE, (self.x_pos, self.y_pos + 100), -1)
            pygame.mixer.Sound.play(PLAYER_LASER_SOUND)
            sprite_group.add(shot)
        cannon = random.randint(0, 500)
        if cannon > 480:
            shot = Projectile(PROJ_BOSS_IMAGE, (self.x_pos, self.y_pos + 150), -1)
            pygame.mixer.Sound.play(BOSS_CANNON_SOUND)
            sprite_group.add(shot)


# MAIN APP CLASS ------------------------------------------------------------------------------------------------------
class MainApp:
    def __init__(self, window):
        # initializing game variables
        self.clock = pygame.time.Clock()
        self.win = window
        self.run = True
        self.BG = PHASE_BG_DICT[0]
        self.level = 0
        self.level_text = FONT_1.render(f'Level: {self.level}', True, (255, 255, 255))
        self.game_phase = 0
        self.phase_change_levels = [1, 5]

        # enemy wave dictionary
        self.enemy_waves = {
            1: [(1, 1), (2, 1)],
            2: [(2, 3)],
            3: [(3, 1), (4, 1)],
            4: [(4, 1), (1, 5)],
            5: [(5, 1)]
        }

        # initializing sprites and sprite groups
        self.enemies_on_screen = pygame.sprite.Group()
        self.player = PlayerShip()
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.player_projectiles_on_screen = pygame.sprite.Group()
        self.enemy_projectiles_on_screen = pygame.sprite.Group()
        self.explosions_on_screen = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(
            self.player_group.sprites(),
            self.player_projectiles_on_screen.sprites(),
            self.enemy_projectiles_on_screen.sprites(),
            self.explosions_on_screen.sprites())

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
            elif event.type == GAME_LOST:
                self.game_phase = 'GAMEOVER'
                self.game_over()
            elif event.type == GAME_WON:
                self.game_phase = 'WIN'
                self.game_won()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.event_next_level()
                if event.key == pygame.K_SPACE:
                    shots = self.player.shoot(self.player_projectiles_on_screen)
                    if len(shots) > 0:
                        for shot in shots:
                            self.player_projectiles_on_screen.add(shot)
                            self.all_sprites.add(shot)
        return

    def event_next_level(self):
        self.level += 1
        self.level_text = FONT_1.render(f'Level: {self.level}', True, (255, 255, 255))
        if self.level == 1:
            self.game_phase = 1
        elif self.level == 5:
            self.game_phase = 2

        if self.game_phase == 1:
            self.BG = PHASE_BG_DICT[2]
            for wave in self.enemy_waves[self.level]:
                ship_type, number = wave[0], wave[1]
                for i in range(number):
                    ship = EnemyShip(ship_type)
                    self.enemies_on_screen.add(ship)
                    self.all_sprites.add(ship)

        if self.game_phase == 2:
            ship = BossShip()
            self.enemies_on_screen.add(ship)
            self.all_sprites.add(ship)

    def phase_0(self):  # ----- INTRO SCREEN ----- #
        if MUSIC_ON:
            pygame.mixer.music.load(MUSIC_FILE_DICT[self.game_phase])
            pygame.mixer.music.play(-1, 0.0)

        while self.game_phase == 0:
            self.check_events()
            self.win.blit(self.BG, (0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)

    def phase_1(self):  # ----- ENEMY WAVES ----- #
        if MUSIC_ON:
            pygame.mixer.music.load(MUSIC_FILE_DICT[self.game_phase])
            pygame.mixer.music.play(-1, 0.0)

        while self.game_phase == 1:
            self.clock.tick(FPS)
            self.check_events()
            self.win.blit(self.BG, (0, 0))
            self.all_sprites.update()
            for ship in self.enemies_on_screen.sprites():
                explosion = ship.check_collision(self.player_projectiles_on_screen)
                if explosion is not None:
                    self.explosions_on_screen.add(explosion)
                    self.all_sprites.add(explosion)
            for ship in self.enemies_on_screen.sprites():
                ship.shoot(self.enemy_projectiles_on_screen)
                self.all_sprites.add(self.enemy_projectiles_on_screen)
            self.player.check_collision(self.enemy_projectiles_on_screen.sprites())
            self.all_sprites.draw(self.win)
            self.win.blit(self.player.heath_txt, (5, 5))
            self.win.blit(self.level_text, (500, 5))
            pygame.display.flip()
            if len(self.enemies_on_screen.sprites()) == 0:
                self.event_next_level()

    def phase_2(self):  # ----- BOSS FIGHT ----- #
        if MUSIC_ON:
            pygame.mixer.music.load(MUSIC_FILE_DICT[self.game_phase])
            pygame.mixer.music.play(-1, 0.0)

        while self.game_phase == 2:
            self.clock.tick(FPS)
            self.check_events()
            self.win.blit(self.BG, (0, 0))
            self.all_sprites.update()

            for ship in self.enemies_on_screen.sprites():
                ship.check_collision(self.player_projectiles_on_screen)
                ship.shoot(self.enemy_projectiles_on_screen)
                self.all_sprites.add(self.enemy_projectiles_on_screen)
            self.player.check_collision(self.enemy_projectiles_on_screen.sprites())

            self.all_sprites.draw(self.win)
            self.win.blit(self.player.heath_txt, (5, 5))

            pygame.display.flip()

    def game_over(self):
        gameover_text = FONT_2.render('GAME OVER', True, (255, 255, 255))
        self.win.blit(self.BG, (0, 0))
        self.win.blit(gameover_text, (0, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        sleep(2)
        self.reset()

    def game_won(self):
        game_won_text = FONT_2.render('YOU WON!', True, (255, 255, 255))
        self.win.blit(self.BG, (0, 0))
        self.win.blit(game_won_text, (0, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        sleep(2)
        self.reset()

    def reset(self):
        self.BG = PHASE_BG_DICT[0]
        self.level = 0
        self.level_text = FONT_1.render(f'Level: {self.level}', True, (255, 255, 255))
        self.game_phase = 0
        self.player.health = 10

    def main(self):
        phases = {0: self.phase_0, 1: self.phase_1, 2: self.phase_2}
        while self.run:
            phases[self.game_phase]()


# RUNTIME CODE ---------------------------------------------------------------------------------------------------------
game = MainApp(SCREEN)

if __name__ == '__main__':
    game.main()
