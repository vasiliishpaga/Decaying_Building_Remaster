import pygame
import sys
import os
from random import randint
from time import sleep

pygame.init()

W = 600
H = 600
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Decaying Building - Remastered")
WHITE = (255,255,255)
LIGHTBLUE = (0,65,155)

def abs_path():
    path_object = os.path.abspath(__file__ + "/..")
    path_object = path_object.split("\\")
    path_object = "\\".join(path_object)
    return path_object

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center= (W//2, H//2))
        self.x = x
        self.y = y
    def draw(self):
        win.blit(self.image, (self.x, self.y))

work_directory = abs_path()
os.chdir(work_directory)

block = pygame.Surface((235,35))
block.fill(LIGHTBLUE)

block2 = pygame.Surface((300,35))
block2.fill(LIGHTBLUE)

block3 = pygame.Surface((20,50))
block3.fill(LIGHTBLUE)

block4 = pygame.Surface((20,50))
block4.fill(LIGHTBLUE)

block5 = pygame.Surface((10,H))
block5.fill(LIGHTBLUE)

block6 = pygame.Surface((W,10))
block6.fill(LIGHTBLUE)

block7 = pygame.Surface((W,10))
block7.fill(LIGHTBLUE)

block8 = pygame.Surface((10,H))
block8.fill(LIGHTBLUE)

block9 = pygame.Surface((235,35))
block9.fill(LIGHTBLUE)

block10 = pygame.Surface((300,35))
block10.fill(LIGHTBLUE)

block11 = pygame.Surface((235,35))
block11.fill(LIGHTBLUE)

block12 = pygame.Surface((300,35))
block12.fill(LIGHTBLUE)

block13 = pygame.Surface((235,35))
block13.fill(LIGHTBLUE)

block14 = pygame.Surface((300,35))
block14.fill(LIGHTBLUE)

block15 = pygame.Surface((20,50))
block15.fill(LIGHTBLUE)

block16 = pygame.Surface((20,50))
block16.fill(LIGHTBLUE)

block17 = pygame.Surface((20,50))
block17.fill(LIGHTBLUE)

block18 = pygame.Surface((20,50))
block18.fill(LIGHTBLUE)

block19 = pygame.Surface((20,50))
block19.fill(LIGHTBLUE)

block20 = pygame.Surface((20,50))
block20.fill(LIGHTBLUE)

block21 = pygame.Surface((90,20))
block21.fill(LIGHTBLUE)

block22 = pygame.Surface((90,20))
block22.fill(LIGHTBLUE)

block23 = pygame.Surface((90,20))
block23.fill(LIGHTBLUE)

block24 = pygame.Surface((90,20))
block24.fill(LIGHTBLUE)

block25 = pygame.Surface((10,100))
block25.fill(LIGHTBLUE)

block26 = pygame.Surface((10,100))
block26.fill(LIGHTBLUE)

block27 = pygame.Surface((10,125))
block27.fill(LIGHTBLUE)

block28 = pygame.Surface((10,125))
block28.fill(LIGHTBLUE)

block29 = pygame.Surface((10,125))
block29.fill(LIGHTBLUE)

block30 = pygame.Surface((10,125))
block30.fill(LIGHTBLUE)

block31 = pygame.Surface((10,125))
block31.fill(LIGHTBLUE)

block32 = pygame.Surface((10,125))
block32.fill(LIGHTBLUE)

block33 = pygame.Surface((10,125))
block33.fill(LIGHTBLUE)

block34 = pygame.Surface((10,125))
block34.fill(LIGHTBLUE)

block35 = pygame.Surface((5,100))
block35.fill(LIGHTBLUE)

block36 = pygame.Surface((5,100))
block36.fill(LIGHTBLUE)

block37 = pygame.Surface((5,100))
block37.fill(LIGHTBLUE)

block38 = pygame.Surface((5,100))
block38.fill(LIGHTBLUE)

block39 = pygame.Surface((5,100))
block39.fill(LIGHTBLUE)

block40 = pygame.Surface((5,100))
block40.fill(LIGHTBLUE)

block41 = pygame.Surface((5,75))
block41.fill(LIGHTBLUE)

block42 = pygame.Surface((5,75))
block42.fill(LIGHTBLUE)

block_rect = pygame.Rect(0, 100, 235, 35)

block2_rect = pygame.Rect(325,100,300,35)

block9_rect = pygame.Rect(0,225,235,35)

block10_rect = pygame.Rect(325,225,300,35)

block11_rect = pygame.Rect(0,350,235,35)

block12_rect = pygame.Rect(325,350,300,35)

block13_rect = pygame.Rect(0,475,235,35)

block14_rect = pygame.Rect(325,475,235,35)

block35_rect = pygame.Rect(190,50,5,75)

block36_rect = pygame.Rect(375,50,5,75)

block37_rect = pygame.Rect(190,175,5,75)

block38_rect = pygame.Rect(375,175,5,75)

block39_rect = pygame.Rect(190,300,5,75)

block40_rect = pygame.Rect(375,300,5,75)

block41_rect = pygame.Rect(190,425,5,75)

block42_rect = pygame.Rect(375,425,5,75)

plr_surf = pygame.image.load("sprite/1.png").convert()
plr_surf.set_colorkey((255,255,255))
plr_rect = plr_surf.get_rect(center= (W//2, H//2))

plr = plr_surf

x_speed = 15
y_speed = 15

hp = 100


#key_surf = pygame.image.load("sprite/2.png").convert()
#key_surf.set_colorkey((255,255,255))
#key_rect = key_surf.get_rect(center= (W//2, H//2))

collision_rects = [block_rect, block2_rect, block9_rect, block10_rect, block11_rect, block12_rect, block13_rect, block14_rect]

def collisions():
    global y_speed
    if plr_rect.collidelistall(collision_rects):
        y_speed = 0
    if not plr_rect.collidelistall(collision_rects):
        y_speed = 15

#block42_rect == door with key


doors = [block35_rect, block36_rect, block37_rect, block38_rect, block39_rect, block40_rect, block41_rect,]

check = False
check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False
check10 = False
check11 = False
check12 = False
check13 = False
check14 = False
check15 = False
check16 = False
check17 = False
check18 = False
check19 = False
check20 = False
check21 = False
print("test")
def doortouch():
    global check
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check8
    global check9
    global check10
    global check11
    global check12
    global check13
    global check14
    global check15
    global check16
    global check17
    global check18
    global check19
    global check20
    global check21
    if plr_rect.colliderect(block35_rect):
        ran = randint(1,3)
        if ran == 1:
            check = True
        if ran == 2:
            check2 = True
        if ran == 3:
            check3 = True
    if plr_rect.colliderect(block36_rect):
        ran = randint(1,3)
        if ran == 1:
            check4 = True
        if ran == 2:
            check5 = True
        if ran == 3:
            check6 = True
    if plr_rect.colliderect(block37_rect):
        ran = randint(1,3)
        if ran == 1:
            check = True
        if ran == 2:
            check2 = True
        if ran == 3:
            check3 = True
    if plr_rect.colliderect(block38_rect):
        ran = randint(1,3)
        if ran == 1:
            check10 = True
        if ran == 11:
            check2 = True
        if ran == 12:
            check3 = True
    if plr_rect.colliderect(block39_rect):
        ran = randint(1,3)
        if ran == 1:
            check13 = True
        if ran == 2:
            check14 = True
        if ran == 3:
            check15 = True
    if plr_rect.colliderect(block40_rect):
        ran = randint(1,3)
        if ran == 1:
            check16 = True
        if ran == 2:
            check17 = True
        if ran == 3:
            check18 = True
    if plr_rect.colliderect(block41_rect):
        ran = randint(1,3)
        if ran == 1:
            check19 = True
        if ran == 2:
            check20 = True
        if ran == 3:
            check21 = True

game_score = 0

game = True

while game:
    win.fill((0,0,0))
    win.blit(block, (0, 100))
    win.blit(block2, (325, 100))
    win.blit(block3, (175,0))
    win.blit(block4, (375,0))
    win.blit(block5, (0,0))
    win.blit(block6, (0,590))
    win.blit(block7, (0,0))
    win.blit(block8, (590,0))
    win.blit(block9, (0,225))
    win.blit(block10, (325,225))
    win.blit(block11, (0,350))
    win.blit(block12, (325,350))
    win.blit(block13, (0,475))
    win.blit(block14, (325,475))
    win.blit(block15, (175, 125))
    win.blit(block16, (375, 125))
    win.blit(block17, (175, 250))
    win.blit(block18, (375, 250))
    win.blit(block19, (175, 375))
    win.blit(block20, (375, 375))
    win.blit(block21, (235,100))
    win.blit(block22, (235,225))
    win.blit(block23, (235,350))
    win.blit(block24, (235,475))
    win.blit(block25, (235,0))
    win.blit(block26, (315,0))
    win.blit(block27, (235,100))
    win.blit(block28, (315,100))
    win.blit(block29, (235,225))
    win.blit(block30, (315,225))
    win.blit(block31, (235,350))
    win.blit(block32, (315,350))
    win.blit(block33, (235,475))
    win.blit(block34, (315,475))
    win.blit(block35, (190, 50))
    win.blit(block36, (375, 50))
    win.blit(block37, (190, 175))
    win.blit(block38, (375, 175))
    win.blit(block39, (190, 300))
    win.blit(block40, (375, 300))
    win.blit(block41, (190, 425))
    win.blit(block42, (375, 425))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        e = pygame.key.get_pressed()
        if e[pygame.K_a]:
            plr_rect.x -= x_speed
            if plr_rect.x < 0:
                plr_rect.x = 0
        elif e[pygame.K_d]:
            plr_rect.x += x_speed
            if plr_rect.x > W - plr_rect.height:
                plr_rect.x = W - plr_rect.height
        elif e[pygame.K_w]:
            plr_rect.y -= y_speed
            if plr_rect.y < 0:
                plr_rect.y = 0
        elif e[pygame.K_s]:
            plr_rect.y += y_speed
            if plr_rect.y > H - plr_rect.height:
                plr_rect.y = H - plr_rect.height
        if check == True:
            apple = Sprite("sprite/3.png",20,80)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check2 == True:
            srng = Sprite("sprite/4.png", 20, 80)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check3 == True:
            ghost = Sprite("sprite/5.png", 20, 80)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check4 == True:
            apple = Sprite("sprite/3.png",576,80)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check5 == True:
            srng = Sprite("sprite/4.png", 576, 80)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check6 == True:
            ghost = Sprite("sprite/5.png", 576, 80)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check7 == True:
            apple = Sprite("sprite/3.png",20,240)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check8 == True:
            srng = Sprite("sprite/4.png", 20, 240)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check9 == True:
            ghost = Sprite("sprite/5.png", 20, 240)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check10 == True:
            apple = Sprite("sprite/3.png",576,240)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check11 == True:
            srng = Sprite("sprite/4.png", 576, 240)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check12 == True:
            ghost = Sprite("sprite/5.png", 576, 240)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check13 == True:
            apple = Sprite("sprite/3.png",20,320)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check14 == True:
            srng = Sprite("sprite/4.png", 20, 320)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check15 == True:
            ghost = Sprite("sprite/5.png", 20, 320)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check16 == True:
            apple = Sprite("sprite/3.png",576,320)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check17 == True:
            srng = Sprite("sprite/4.png", 576, 320)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check18 == True:
            ghost = Sprite("sprite/5.png", 576, 320)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if check19 == True:
            apple = Sprite("sprite/3.png", 20,460)
            apple.draw()
            pygame.display.update()
            sleep(0.01)
            if apple.rect.colliderect(plr_rect):
                game_score += 50
                print(game_score)
        if check20 == True:
            srng = Sprite("sprite/4.png", 20, 460)
            srng.draw()
            pygame.display.update()
            sleep(0.01)
            if srng.rect.colliderect(plr_rect):
                game_score += 100
                print(game_score)
        if check21 == True:
            ghost = Sprite("sprite/5.png", 20, 460)
            ghost.draw()
            pygame.display.update()
            sleep(0.01)
            if ghost.rect.colliderect(plr_rect):
                game_score += 150
                print(game_score)
        if plr_rect.colliderect(block42_rect):
            key = Sprite("sprite/2.png", 576, 460)
            key.draw()
            pygame.display.update()
        collisions()
        doortouch()
    win.blit(plr, plr_rect)

    pygame.display.flip()
    clock.tick(FPS)