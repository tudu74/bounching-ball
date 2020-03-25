import pygame
import sys
from settings import Settings
import time
from pygame import mixer

s = Settings()
clock = pygame.time.Clock()

pygame.init()

#Img = pygame.image.load('Image.jpg')

X = 200
Y = 400
R = 20
screen = pygame.display.set_mode((s.screen_width, s.screen_height))
pygame.display.set_caption("Game")
UP = 0
Down = 0
Left = 0
Right = 0
moveY = 0

while True:

    screen.fill((45, 179, 246))
#    screen.blit(Img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if X <= 15 or X == 200:
        Right = 7
        Left = 0
    if X >= 785:
        Right = 0
        Left = 10

    X += Right
    X -= Left

    if Y >= 400:
        moveY += 1
    if Y >= 585:
        moveY -= 20
 #   bound_sound = mixer.Sound('')
#  bound_sound.play()
    Y += moveY

    clock.tick(s.FPS)

    pygame.draw.circle(screen, (0, 0, 153), (X, Y), R, 0)

    pygame.display.update()
