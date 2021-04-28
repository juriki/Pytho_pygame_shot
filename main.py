import pygame
import random
import time


class Enemy:
    def __init__(self, win, enemypos=None):
        self.x = random.randint(10, 455)
        self.y = random.randint(10, 250)
        self.enemy_color = (255, 255, 0)
        self.height = 60
        self.width = 40
        self.win = win
        self.bum = -1
        self.a_live = 0
        self.right = random.randint(0, 1)
        print(self.x, "<---x pos   y pos--->", self.y)


    def drew(self):
        """Рисуем врога  и двигаем его"""
        pygame.draw.rect(self.win, self.enemy_color, (self.x, self.y, self.height, self.width))
        if self.right == True:
            self.x += 4
            if self.x >= 460:
                self.right = False
        elif self.right == False:
            self.x -= 4
            if self.x <= 10:
                self.right = True


    def posittion(self, yp, xp):
        """Возврашаем место положение врага на экране"""
        if yp <= self.y+30:
                if xp >= self.x-20 and xp <= self.x+40:
                    return True
        else:
            return False


    def bumbum(self):
        """Каждому врагу дается 2 жизни Тут идет проверка сколько осталось Жить врагу"""
        self.bum += 1
        self.a_live += 1
        if self.a_live >= 11:
            # смерть врага
            return True
        elif self.bum >= 5:
            # цмена позиции врага
            self.x = random.randint(10, 455)
            self.y = random.randint(10, 250)
            self.enemy_color = (255, 0, 0)
            self.bum = -1
            return False
        return False


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def shottiing(self):
        if self.y > 10:
            pygame.draw.circle(win, (255, 255, 0), (self.x + 20, self.y), 4)
            self.y = self.y-6

    def bullet_posittion(self):
        return self.y, self.x


class Player:

    def __init__(self):
        self.x = 200
        self.y = 400


    def pleyer_drew(self):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, 40, 60))

    def player_moving(self, x=None, y=None):
        if x:
            self.x +=x
        if y:
            self.y += y
        return self.x, self.y




win_high = 500
win_weidth = 500
bg2 = pygame.image.load("/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/cosmos.jpg")
win = pygame.display.set_mode((win_high, win_weidth))
pygame.display.set_caption("Shot!")
stop_time = 0
game_time = 0
run = True
speed = 6
bull = []

en = [Enemy(win), Enemy(win), Enemy(win), Enemy(win)]
pl = Player()

def shot_or_not(bull, en):
    try:
        for i in range(len(bull)):
            if bull[i] == None:
                bull.pop(i)
            elif bull[i].y > 10:
                bull[i].shottiing()
                for j in range(len(en)):
                    ax, ay = bull[i].bullet_posittion()
                    if not en[j].posittion(ax, ay):
                        continue
                    del bull[i]
                    en[j].bumbum()
                    if en[j].bumbum():
                        del en[j]
                        if len(en) == 0:
                            print("You Win The Game Ошибок было --->")
                            time.sleep(0.5)
                            run = False
                            return False
            else:
                bull.append(None)
                del bull[i]

    except IndexError:
        bull.append(None)
    return True


while run:
    # Главный Цикл игры
    pygame.time.delay(30)
    game_time = int(time.time()) - int(game_time)
    if int(game_time) == 50:
        print("Time over Ошибок было --->", problem)
        run = False
    for evnen in pygame.event.get():
        # Проверка на выход из игры
        if evnen.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        # Выход из игры
        run = False

    if keys[pygame.K_LEFT] and player[0] >= 10:
            pl.player_moving(-speed)
    if keys[pygame.K_RIGHT] and player[0] <= 450:
            pl.player_moving(speed)
    if keys[pygame.K_UP] and player[1] >= 320:# and y > 370:
        pl.player_moving(None, -speed)
    if keys[pygame.K_DOWN]and player[1] <= 420:# and y < 400:
        pl.player_moving(None, 10)

    if keys[pygame.K_SPACE] and time.time() - stop_time >= 0.3:
        a = Bullet(player[0], player[1])
        bull.append(a)
        stop_time = time.time()

#  Рисуем  Врагов, экран и Игрока
    win.blit(bg2, (0, 0))
    for k in range(len(en)):
        en[k].drew()
    pl.pleyer_drew()
    player = pl.player_moving()

# Полет пули проверка на поподание
    if not shot_or_not(bull, en):
        run = False

    pygame.display.update()


pygame.quit()
