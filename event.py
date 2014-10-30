import pygame
import sys
from random import randint
from classes import Booba, RoiSpit


def process_events(roi):
    # Exit event on window frame
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                RoiSpit.fire = not RoiSpit.fire

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        roi.going_right = True
        roi.rect.x += 5
    elif keys[pygame.K_LEFT]:
        roi.going_right = False
        roi.rect.x -= 5
    else:
        roi.velx = 0

    if keys[pygame.K_UP]:
        roi.jumping = True

    if keys[pygame.K_SPACE]:
        projectile_path = 'images/projectiles/frost.png'
        is_fire = False
        if RoiSpit.fire:
            projectile_path = 'images/projectiles/fire.png'
            is_fire = True

        if roi.going_right:
            p = RoiSpit(roi.rect.x + 10, roi.rect.y + 30, projectile_path, is_fire)
            p.velx = 8
        else:
            p = RoiSpit(roi.rect.x - 15, roi.rect.y + 26, projectile_path, is_fire)
            p.image = pygame.transform.flip(p.image, True, False)
            p.velx = -8


def spawn(fps, total_frames):
    four_sec = fps * 4
    if total_frames % four_sec == 0:
        r = randint(1, 2)
        booba = Booba(randint(10, 562), 100, 'images/booba.PNG')


def handle_collisions():
    #for booba in Booba.boobas:
    #    if pygame.sprite.spritecollide(booba, RoiSpit.spits, False):
    #       if RoiSpit.fire:
    #            booba.health -= booba.half_health
    #        else:
    #            booba.image = pygame.image.load('images/booba_frozen.png')
    #            booba.velx = 0

    #for spit in RoiSpit.spits:
    #    if pygame.sprite.spritecollide(spit, Booba.boobas, False):
    #        spit.rect.x = -2 * spit.rect.width
    #        spit.destroy()
    for booba in Booba.boobas:
        spits = pygame.sprite.spritecollide(booba, RoiSpit.spits, True)
        for spit in spits:
            if spit.is_fire:
                booba.image = pygame.image.load('images/booba_burnt.png')
                booba.health -= booba.half_health
            else:
                booba.image = pygame.image.load('images/booba_frozen.png')
                booba.velx = 0

            spit.rect.x = -2 * spit.rect.width
            spit.destroy()


def check_theme():
    if pygame.mixer.music.get_pos() > 103000:
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()