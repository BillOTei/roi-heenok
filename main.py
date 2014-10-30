import pygame
import event

from classes import *

pygame.init()
pygame.mixer.init()

width, height = 640, 400
screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()
fps = 26
total_frames = 0
roi = Roi(0, 349, 'images/roi.PNG')
bg = pygame.image.load('images/bg.jpg')

# Music negros !!
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play()

while True:
    event.check_theme()

    event.process_events(roi)

    event.spawn(fps, total_frames)

    event.handle_collisions()

    # Logic
    roi.motion(width, height)
    Booba.update_all(width, height)
    RoiSpit.movement()
    total_frames += 1

    # Draw
    screen.blit(bg, (0, 0))
    BaseClass.allSprites.draw(screen)
    RoiSpit.spits.draw(screen)
    pygame.display.flip()

    clock.tick(fps)