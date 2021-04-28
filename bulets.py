import pygame

class Enemy:
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.height = 60
        self.width = 40
        self.win = win

    def drew(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, self.height, self.width))

    def posittion(self):
        """Ресуем Врага  и возврашаем место положение"""
        return self.x - 11, self.y + 25



en = Enemy(40, 60)

en.drew()

en.posittion()