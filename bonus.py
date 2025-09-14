import pygame
import random


class Bonus:
    """Класс рисуюший боунсы"""
    def __init__(self, win):
        self.win = win
        self.x = random.randint(10,465)
        self.y = -10
        self.bonus_start = 13
        self.coin = pygame.image.load(f"coin.gif").convert_alpha()
        self.coin.subsurface((0, 0, 60, 60))

    def drew(self):
        """Тут рисутся монетка """
        if self.y == -15:
            self.y = -10
            self.x = random.randint(10, 465)
        elif self.bonus_start % 100 == 0:
            self.win.blit(self.coin, (self.x, self.y))
            self.y += 3
            if self.y >= 500:
                self.y = - 10
                self.x = random.randint(10, 465)
                self.bonus_start = 13
        else:
            self.bonus_start = random.randint(1, 200)
        return self.x, self.y


