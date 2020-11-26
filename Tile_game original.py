"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255) 
PURPLE = (128, 0, 128)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 650)
screen = pygame.display.set_mode(size)

 # Set name of window
pygame.display.set_caption("Tile game")
 
#Set up map List

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.y=240
        self.rect.x=240
        self.health = 1000
        self.money = 0
        self.score = 0
        self.key = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((2, 2))
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def move(self):
        if Bullet_direction == "L":
            self.rect.x = self.rect.x - 2
        elif Bullet_direction == "R":
            self.rect.x = self.rect.x + 2
        elif Bullet_direction == "U":
            self.rect.y = self.rect.y - 2
        elif Bullet_direction == "D":
            self.rect.y = self.rect.y + 2
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((12, 12))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.health = 300

    def move(self):
        if player.rect.x > enemy.rect.x:
            enemy.rect.x = enemy.rect.x + 10
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.x -= 10
        if player.rect.x < enemy.rect.x:
            enemy.rect.x = enemy.rect.x - 10
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.x += 10
        if player.rect.y > enemy.rect.y:
            enemy.rect.y = enemy.rect.y + 10
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.y -= 10
        if player.rect.y < enemy.rect.y:
            enemy.rect.y = enemy.rect.y -10
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.y += 10

class Enemy(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.health = 500


     def move(self):
        if player.rect.x > enemy.rect.x:
            enemy.rect.x = enemy.rect.x + 5
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.x -= 5
        if player.rect.x < enemy.rect.x:
            enemy.rect.x = enemy.rect.x - 5
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.x += 5
        if player.rect.y > enemy.rect.y:
            enemy.rect.y = enemy.rect.y + 5
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.y -= 5
        if player.rect.y < enemy.rect.y:
            enemy.rect.y = enemy.rect.y -5
            enemy_collision_list = pygame.sprite.spritecollide(enemy, enemy_sprites_list, False)
            if len(enemy_collision_list) > 1:
                enemy.rect.y += 5

class Portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40, 40))
        self.image.fill(PURPLE)
        self.rect=self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 230
        
class TextPrint(object):
    
    def __init__(self):
        self.reset()
        self.x_pos = 50
        self.y_pos = 510
        self.font = pygame.font.Font(None, 20)
 
    def print(self, my_screen, text_string):
        text = self.font.render(text_string, True, BLACK)
        my_screen.blit(text, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height

    def Titleprint(self, my_screen, Text):
        text = self.font.render(Text, True, RED)
        my_screen.blit(text, [250, 80])
 
    def reset(self):
        self.x_pos = 50
        self.y_pos = 510
        self.line_height = 15


# Create wall class
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.x=x


# Declare lists of sprites
enemy_sprites_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
wall_sprites_list = pygame.sprite.Group()
portal_sprite_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)
textPrint = TextPrint()

done = False
Bullet_on_screen = False
Bullet_x = player.rect.x + 9
Bullet_y = player.rect.y + 2
enemy_timer = 0
num_enemies = 4
New_level = True
Level_num = 0
Shop = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#Declare any fonts
font = pygame.font.Font('freesansbold.ttf', 16)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
          #Set up new level


        elif New_level == True:
            New_level = False
            Cash = player.money
            Health = player.health
            Score = player.score
            enemy_sprites_list.empty()
            all_sprites_list.empty()
            wall_sprites_list.empty()
            portal_sprite_list.empty()
            player = Player()
            player.health = Health
            player.money = Cash
            player.score = Score
            all_sprites_list.add(player)
            Level_num += 1
            if Level_num % 3 == 1:
                    Maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1], 
                            [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
                            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

            elif Level_num % 3 == 2:
                    Maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], 
                            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], 
                            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

            elif Level_num % 3 == 0:
                    Maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                #Set up Walls
            for xnum in range(0, 25):
                    for ynum in range(0, 25):
                        if Maps[ynum][xnum] == 1:
                            wall = Wall(xnum*20, ynum*20)
                            all_sprites_list.add(wall)
                            wall_sprites_list.add(wall)
     
            num_enemies += 1
                #Set up Enemies
            for num in range(0,num_enemies):
                    free_space = False
                    while not free_space:
                        x = random.randrange(23) + 1
                        y = random.randrange(23) + 1
                        if Maps[y][x] == 0:
                            free_space = True
                    x_coord = x * 20
                    y_coord = y * 20
                    Enemy_type = random.randrange(2)
                    if Enemy_type == 0:
                        enemy = Enemy2(x_coord, y_coord)
                        all_sprites_list.add(enemy)
                        enemy_sprites_list.add(enemy)
                    else: 
                        enemy = Enemy(x_coord, y_coord)
                        all_sprites_list.add(enemy)
                        enemy_sprites_list.add(enemy)


    # --- Game logic should go here
 #If user presses down a key
        elif event.type == pygame.KEYDOWN:
    #If key is an arrow key
            if event.key == pygame.K_LEFT:
                player.rect.x = player.rect.x - 20
                Last_movement = "left"
                player_wall_collision_list = pygame.sprite.spritecollide(player, wall_sprites_list, False)
                if len(player_wall_collision_list) > 0:
                    player.rect.x += 20
            elif event.key == pygame.K_RIGHT:
                player.rect.x = player.rect.x + 20
                Last_movement = "right"
                player_wall_collision_list = pygame.sprite.spritecollide(player, wall_sprites_list, False)
                if len(player_wall_collision_list) > 0:
                    player.rect.x -= 20
            elif event.key == pygame.K_UP:
                player.rect.y = player.rect.y - 20
                Last_movement = "up"
                player_wall_collision_list = pygame.sprite.spritecollide(player, wall_sprites_list, False)
                if len(player_wall_collision_list) > 0:
                    player.rect.y += 20
            elif event.key == pygame.K_DOWN:
                player.rect.y = player.rect.y + 20
                Last_movement = "down"
                player_wall_collision_list = pygame.sprite.spritecollide(player, wall_sprites_list, False)
                if len(player_wall_collision_list) > 0:
                    player.rect.y -= 20

            if event.key == pygame.K_SPACE and Bullet_on_screen == False:
                if Last_movement == "left":
                    Bullet_x = player.rect.x + 2
                    Bullet_y = player.rect.y + 9
                    print("Shot")
                    Bullet_direction = "L"
                    Bullet_on_screen = True
                if Last_movement == "right":
                    Bullet_x = player.rect.x + 22
                    Bullet_y = player.rect.y + 9
                    print("Shot")
                    Bullet_direction = "R"
                    Bullet_on_screen = True
                if Last_movement == "up":
                    Bullet_x = player.rect.x + 9
                    Bullet_y = player.rect.y + 2
                    print("Shot")
                    Bullet_direction = "U"
                    Bullet_on_screen = True
                if Last_movement == "down":
                    Bullet_x = player.rect.x + 9
                    Bullet_y = player.rect.y + 22
                    print("shot")
                    Bullet_direction = "D"
                    Bullet_on_screen = True
                bullet = Bullet(Bullet_x, Bullet_y)
                all_sprites_list.add(bullet)
        #endif

    #Move bullet
    if Bullet_on_screen == True:
        bullet.move()

    #Player/enemy collisions
    collisions_list = pygame.sprite.spritecollide(player, enemy_sprites_list, False)
    if len(collisions_list) > 0:
        for enemy in collisions_list:
            player.health = player.health - random.randrange(10)
            enemy.health = enemy.health - random.randrange(10)
            if enemy.health < 0:
                    enemy_sprites_list.remove(enemy)
                    all_sprites_list.remove(enemy)
                    player.health = player.health + 100
                    player.money = player.money + 10
                    player.score = player.score + 100
                    player.key = player.key + 1
                    print("Congratulations, you killed an enemy and gained a key!!!")
       

    #Bullet/enemy collisions
    if Bullet_on_screen == True:
        Bullet_enemy_collisions_list = pygame.sprite.spritecollide(bullet, enemy_sprites_list, False)
        if len(Bullet_enemy_collisions_list) > 0:
              for enemy in Bullet_enemy_collisions_list:
                 enemy.health = enemy.health - 100
                 all_sprites_list.remove(bullet)
                 Bullet_on_screen = False
                 if enemy.health < 0:
                     enemy_sprites_list.remove(enemy)
                     all_sprites_list.remove(enemy)
                     player.health = player.health + 100
                     player.money = player.money + 10
                     player.score = player.score + 100
                     player.key = player.key + 1
                     print("Congratulations, you killed an enemy and gained a key!!!")
           

    #Bullet Wall Collisions
    if Bullet_on_screen == True:
        Bullet_wall_collisions_list = pygame.sprite.spritecollide(bullet, wall_sprites_list, False)
        if len(Bullet_wall_collisions_list) > 0:
            all_sprites_list.remove(bullet)
            for bullet in Bullet_wall_collisions_list:
                Bullet_on_screen = False

    #Timer for enemy movement
    enemy_timer = enemy_timer + 1
    if enemy_timer % 20 == 0:
         for enemy in enemy_sprites_list:
              enemy.move()

     #Portal appear
    if len(enemy_sprites_list) == 0:
         portal = Portal() 
         portal_sprite_list.add(portal)
         all_sprites_list.add(portal)
    #if player touches portal start new level
    portal_collision_list = pygame.sprite.spritecollide(player, portal_sprite_list, False)
    if len(portal_collision_list) > 0:
        New_level = True
        
    #If player dies, end game
    if player.health < 0:
        done = True

    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    textPrint.reset()
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    all_sprites_list.update()
    # --- Drawing code should go here
    # Draw all Sprites
    all_sprites_list.draw(screen)
    # Write text
    textPrint.print(screen, "Player Health:")
    textPrint.print(screen, str(player.health))
    textPrint.print(screen, "Player Score:")
    textPrint.print(screen, str(player.score))
    textPrint.print(screen, "Player money:")
    textPrint.print(screen, str(player.money))
    textPrint.print(screen, "Level:")
    textPrint.print(screen, str(Level_num))


    #update the screen with what's been drawn.
    pygame.display.flip()
 
    #Limit to 60 frames per second
    clock.tick(60)
 
    
    # Close the window and quit.
pygame.quit()
