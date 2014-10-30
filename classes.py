import pygame
from random import randint
from math import sin


class BaseClass(pygame.sprite.Sprite):

    allSprites = pygame.sprite.Group()

    def __init__(self, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        BaseClass.allSprites.add(self)

    def destroy(self, class_name):
        if Roi == class_name:
            Roi.allRois.remove(self)
        elif Booba == class_name:
            Booba.boobas.remove(self)

        BaseClass.allSprites.remove(self)
        del self


class Roi(BaseClass):
    allRois = pygame.sprite.Group()

    def __init__(self, x, y, image_path):
        BaseClass.__init__(self, x, y, image_path)
        Roi.allRois.add(self)
        self.velx, self.vely = 0, 20
        self.jumping, self.go_down = False, False
        self.going_right = True

    def motion(self, screen_width, screen_height):
        #self.rect.x += self.vel
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width > screen_width:
            self.rect.x = screen_width - self.rect.width

        self.__jump(screen_height)

    def __jump(self, screen_height):
        max_jump = 75
        if self.jumping:
            if self.rect.y < max_jump or self.vely == 0:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely

                predicted_location = self.rect.y + self.vely
                if predicted_location + self.rect.height > screen_height:
                    self.go_down, self.jumping = False, False

                self.vely += 1
            else:
                self.rect.y -= self.vely
                if 0 < self.vely:
                    self.vely -= 1

            if 20 < self.vely:
                self.vely = 20


class Booba(BaseClass):
    boobas = pygame.sprite.Group()

    def __init__(self, x, y, image_path):
        BaseClass.__init__(self, x, y, image_path)
        Booba.boobas.add(self)
        self.velx = randint(1, 4)
        self.vely = 2
        self.amplitude, self.period = randint(20, 140), randint(4, 5) / 100
        self.health = 100
        self.half_health = self.health / 2.0

    def fly(self, screen_width):
        if self.rect.x + self.rect.width > screen_width or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx

        self.rect.x += self.velx
        self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 140

    @staticmethod
    def update_all(screen_width, screen_height):
        for booba in Booba.boobas:
            if booba.health <= 0:
                if booba.rect.y + booba.rect.height < screen_height:
                    booba.rect.y += booba.vely
            else:
                booba.fly(screen_width)


class RoiSpit(pygame.sprite.Sprite):
    spits = pygame.sprite.Group()
    spits_list = []
    fire = True

    def __init__(self, x, y, image_path, is_fire):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.is_fire = is_fire
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        if RoiSpit.spits_list:
            last_elmt = RoiSpit.spits_list[-1]
            if abs(self.rect.x - last_elmt.rect.x) < self.rect.width / 2:
                return

        RoiSpit.spits.add(self)
        RoiSpit.spits_list.append(self)
        self.velx = 0

    @staticmethod
    def movement():
        for spit in RoiSpit.spits:
            spit.rect.x += spit.velx

    def destroy(self):
        RoiSpit.spits.remove(self)
        RoiSpit.spits_list.remove(self)
        del self