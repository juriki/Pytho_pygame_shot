import pygame
import random
import time
import Start_window

but = Start_window.PopWindow()
pygame.font.init()
win_high = 700
win_weidth = 500
clock = pygame.time.Clock()
bg2 = pygame.image.load("/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/cosmos.jpg")
win = pygame.display.set_mode((win_high, win_weidth))
line = pygame.draw.line(bg2, (255, 255, 255), [520, 0], [520, 500], 5)
pygame.display.set_caption("Shot!")
stop_time = 0
game_time = time.time()
text = False
run = True
speed = 6
bull = []
en = [0, 0, 0, 0]
bull_enemy = [0, 0, 0, 0, 0, 0]
enemys_poistions = []
i = 0

def screen_text(tekst, size=25, color=(255, 255, 255)):
    str(tekst)
    font = pygame.font.SysFont('timesnewromanbold', size)
    my_text = font.render(tekst, 1, color)
    return my_text

win.blit(screen_text(f"{len(en)} Enemys "), (530, 10))



class Enemy:
    def __init__(self, win, enemy_positions):
        test_Y = random.randint(10, 250)
        if len(enemy_positions) > 0:
            i = 0
            while i < len(enemy_positions):
                position = False
                actual_Y = enemy_positions[i][1]
                while not position:
                    if test_Y - 45 <= actual_Y and test_Y + 45 >= actual_Y:
                        test_Y = random.randint(10, 260)
                        i = -1
                        continue
                    else:
                        self.y = test_Y
                        position = True
                        i += 1
        else:
            self.y = random.randint(10, 250)
        self.x = random.randint(10, 455)
        self.enemy_color = (255, 255, 0)
        self.height = 60
        self.width = 40
        self.win = win
        self.speed = random.randint(3, 7)
        self.bum = -1
        self.a_live = 0
        self.right = random.randint(0, 1)
        print(self.x, "<---x pos   y pos--->", self.y)

    def drew(self):
        """Рисуем врога  и двигаем его"""
        pygame.draw.rect(self.win, self.enemy_color, (self.x, self.y, self.height, self.width))
        if self.right == True:
            self.x += self.speed
            if self.x >= 460:
                self.right = False
        elif self.right == False:
            self.x -= self.speed
            if self.x <= 10:
                self.right = True
        return self.x, self.y

    def enemy_position(self, yp, xp):
        """Возврашаем место положение врага на экране"""
        if yp <= self.y + 30:
            if xp >= self.x - 20 and xp <= self.x + 25:
                return
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
            print(self.x, "<---x pos NEW  y pos--->", self.y)
            self.bum = -1
            return False
        return False

    def enemy_posreturn(self):
        return self.x, self.y


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shottiing(self, enemy=None):
        """ Выстрел Пули если enemy == None,(По умолчанию вверч) то пуля летит вверх, иначе вниз"""
        if enemy == None and self.y > 10:
            pygame.draw.circle(win, [255, 99, 71], (self.x + 20, self.y), 4)
            self.y = self.y - 6
        else:
            pygame.draw.circle(win, (124, 252, 0), (self.x + 20, self.y), 4)
            self.y = self.y + 6
            if self.y >= 550:
                return True

    def bullet_posittion1(self, position_to_kii):
        if self.x >= position_to_kii[0] - 20 and self.x <= position_to_kii[0] + 20:
            if self.y >= position_to_kii[1] - 0 and self.y <= position_to_kii[1] + 60:
                return True
        return False

    def bullet_posittion(self):
        """Возврат меспта положения пули"""
        return self.x, self.y


class Player(Bullet):

    def __init__(self):
        self.x = 200
        self.y = 400
        self.boom = 0
        self.pumpkin = pygame.image.load(
            "/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/pumpkin.gif").convert_alpha()
        self.pumpkin.subsurface((0, 0, 60, 60))

    def pleyer_drew(self):
#        if self.boom <= 3:
        win.blit(self.pumpkin, (self.x, self.y))
# TODO  add new sprites
#        elif self.boom <= 6:
#            pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, 40, 60))
#        elif self.boom <= 9:
#            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 40, 60))

    def player_moving(self, x=None, y=None):
        if x:
            self.x += x
        if y:
            self.y += y
        return self.x, self.y

    def player_boom(self):
        self.boom += 1
        if self.boom < 9:
            return True
        else:
            print("GAME OVER YOU LOOS")
            return False

    def shots_to_die(self):
        return 9 - self.boom


while i < 4:
    # Тут создаются обьекты класса "Enemy"
    print(len(enemys_poistions))
    en[i] = Enemy(win, enemys_poistions)
    enemys_poistions.append(en[i].enemy_posreturn())
    i += 1

print(enemys_poistions)
pl = Player()

ship = pygame.image.load("/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/New Piskel.gif").convert_alpha()
ship.subsurface((0, 0, 32, 32))


def shot_or_not(bull, en):
    try:
        for i in range(len(bull)):
            if bull[i] == None:
                bull.pop(i)
            elif bull[i].y > 10:
                bull[i].shottiing()
                for j in range(len(en)):
                    if bull[i].bullet_posittion1(en[j].enemy_posreturn()):
                        en[j].bumbum()
                        del bull[i]
                        if en[j].bumbum():
                            del en[j]
                    if len(en) == 0:
                        print("You Win The Game")
                        time.sleep(0.5)
                        return False
                    else:
                        continue
            else:
                bull.append(None)
                del bull[i]

    except IndexError:
        bull.append(None)
    return True

####################-----------------------------------------------------------##################

while run:
    # Главный Цикл игры

        win.blit(bg2, (0, 0))
        clock.tick(50)
        if int(time.time()) - int(game_time) == 60:
            print("Time is over")
            run = False
        for evnen in pygame.event.get():
            # Проверка на выход из игры
            if evnen.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player[0] >= 10:
            pl.player_moving(-speed)
        if keys[pygame.K_RIGHT] and player[0] <= 465:
            pl.player_moving(speed)
        if keys[pygame.K_UP] and player[1] >= 320:  # and y > 370:
            pl.player_moving(None, -speed)
        if keys[pygame.K_DOWN] and player[1] <= 465:  # and y < 400:
            pl.player_moving(None, 10)
        if keys[pygame.K_SPACE] and time.time() - stop_time >= 0.3:
            a = Bullet(player[0], player[1])
            bull.append(a)
            stop_time = time.time()
        if keys[pygame.K_q]:
            # Выход из игры
            run = False

        #  Рисуем  Врагов, экран и Игрока
        for k in range(len(en)):
            en[k].drew()
            if bull_enemy[k] == 0 and (random.randint(1, 100) % 10) == 0:
                bull_enemy[k] = Bullet(en[k].drew()[0], en[k].drew()[1])
        pl.pleyer_drew()
        player = pl.player_moving()

        # Полет пули проверка на поподание
        if not shot_or_not(bull, en):
            run = False
        for im in range(6):
            try:
                if bull_enemy[im] == 0:
                    continue
                bull_enemy[im].shottiing(1)
                if bull_enemy[im].shottiing(1):
                    bull_enemy[im] = 0
                if bull_enemy[im].bullet_posittion1(pl.player_moving()):
                    run = pl.player_boom()
                    bull_enemy[im] = 0
            except AttributeError:
                continue
        if text:
            win.blit(screen_text(f"{len(en)} Enemys "), (530, 10))
            win.blit(screen_text(f"you have {pl.shots_to_die()} Lives", 22, (255, 255, 0)), (530, 40))
            win.blit(screen_text(f"Time to end {67 - (int(time.time()) - int(game_time))} ", 22, (255, 255, 0)),
                     (530, 80))
        pygame.display.update()
        if not text:
            but.Button()
            text = True

pygame.quit()
