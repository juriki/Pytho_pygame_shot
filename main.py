import pygame
import random
import time
import Start_window
import bonus


but = Start_window.PopWindow()
pygame.font.init()
win_high = 800
win_weidth = 490
clock = pygame.time.Clock()
bg2 = pygame.image.load("/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/trava.jpg")
win = pygame.display.set_mode((win_high, win_weidth))
line = pygame.draw.line(bg2, (255, 255, 255), [520, 0], [520, 500], 5)
stop_time = 0
game_time = time.time()
text = False
run = True
speed = 6
score = 0
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
    """Класс рисуюший Врага и все что сним свазано"""
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
        self.is_dead = False
        self.is_dead_move = 1
        self.right = random.randint(0, 1)
        self.bee_fly = random.randint(1,3)
        self.bee_down = 1
        print(self.x, "<---x pos   y pos--->", self.y)


    def drew(self):
        """Рисуем врога  и двигаем его """
        if self.bee_fly >= 8:
            self.bee_fly = 1
        if not self.is_dead:
        # Проверка живойли Враг
            self.bee_fly += 1
            self.bee = pygame.image.load(
                    f"/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/bee/bee{str(self.bee_fly)}.png").convert_alpha()
            self.bee.subsurface((0, 0, 60, 60))
            win.blit(self.bee, (self.x, self.y))
        if self.is_dead:
        # Проверка живойли враг если подбит то тут он падает
            self.speed = 8
            self.bee = pygame.image.load(f"/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/beedown/bee{str(self.is_dead_move)}.png").convert_alpha()
            self.bee.subsurface((0, 0, 60, 60))
            win.blit(self.bee, (self.x, self.y))
            self.y += self.speed
            if self.is_dead_move <= 6:
                self.is_dead_move += 1
        if self.right == True and self.is_dead_move < 6:
            self.x += self.speed
            if self.x >= 460:
                self.right = False
        elif self.right == False and self.is_dead_move < 6:
            self.x -= self.speed
            if self.x <= 10:
                self.right = True
        return self.x, self.y

    def enemy_position(self, yp, xp):
        """Возврашаем место положение врага на экране"""
        if yp <= self.y + 10:
            if xp >= self.x - 51 and xp <= self.x + 50:
                return
        else:
            return False

    def bumbum(self):
        """Каждому врагу дается 8  поаданий"""
        self.bum += 1
        self.a_live += 1
        if self.a_live >= 7:
            self.is_dead = True
            return True
        return False

    def enemy_posreturn(self):
        # Возврат места полжения врага
        return self.x, self.y


class Bullet:
    """Класс рисуюший Пулю"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.seed = pygame.image.load(
            "/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/seed.gif").convert_alpha()
        self.seed.subsurface((0, 0, 40, 40))

    def shottiing(self, enemy=None):
        """ Выстрел Пули если enemy == None,(По умолчанию вверч) то пуля летит вверх, иначе вниз"""
        if enemy == None and self.y > 10:
            win.blit(self.seed, (self.x+20, self.y-5))
            self.y = self.y - 6
        else:
            pygame.draw.circle(win, (124, 252, 0), (self.x+23, self.y+35), 4)
            self.y = self.y + 6
            if self.y >= 550:
                return True

    def bullet_posittion1(self, position_to_kii):
        if self.x >= position_to_kii[0] - 15 and self.x <= position_to_kii[0] + 5:
            if self.y >= position_to_kii[1] - 0 and self.y <= position_to_kii[1] + 40:
                return True
        return False

    def bullet_posittion2(self, position_to_kii):
        if self.x >= position_to_kii[0] - 10 and self.x <= position_to_kii[0] + 55:
            if self.y >= position_to_kii[1] - 0 and self.y <= position_to_kii[1] + 60:
                return True
        return False

    def bullet_posittion(self):
        """Возврат меспта положения пули"""
        return self.x, self.y


class Player:

    def __init__(self):
        self.x = 200
        self.y = 400
        self.file = 1
        self.boom = 0

    def pleyer_drew(self):
        self.pumpkin = pygame.image.load(
            f"/Users/jurijtokvin/PycharmProjects/pygameTest/Pytho_pygame_shot/pumpkin{str(self.file)}.png").convert_alpha()
        self.pumpkin.subsurface((0, 0, 90, 90))
        if self.boom <= 3:
            win.blit(self.pumpkin, (self.x, self.y))
        elif self.boom <= 6:
            win.blit(self.pumpkin, (self.x, self.y))
            self.file = 2
        elif self.boom <= 9:
            win.blit(self.pumpkin, (self.x, self.y))
            self.file = 3

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
            win.blit(screen_text("Game Over You Lose", 50, (255, 255, 255)), (50, 250))
            print("GAME OVER YOU LOOS")
            return False

    def shots_to_die(self):
        die = 9 - self.boom
        if die >= 9:
            return 9
        else:
            return die

    def player_posittion(self, position_to_kii):
        if self.x <= position_to_kii[0]+24 and position_to_kii[0] <= self.x+50:
            if self.y >= position_to_kii[1]-50 and self.y <= position_to_kii[1]:
                return True

        return False


while i < 4:
    # Тут создаются обьекты класса "Enemy"
    print(len(enemys_poistions))
    en[i] = Enemy(win, enemys_poistions)
    enemys_poistions.append(en[i].enemy_posreturn())
    i += 1

bonus = bonus.Bonus(win)
pl = Player()


def shot_or_not(bull, en):
    try:
        for i in range(len(bull)):
            if bull[i] == None:
                bull.pop(i)
            elif bull[i].y > 10:
                bull[i].shottiing()
                for j in range(len(en)):
                    if bull[i].bullet_posittion1(en[j].enemy_posreturn()):
                        global score
                        score += 20
                        en[j].bumbum()
                        del bull[i]
                    elif len(en) == 0:
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
        clock.tick(60)
        if int(time.time()) - int(game_time) == 60:
            win.blit(screen_text("Time is Over", 50, (255, 255, 255)), (50, 250))
            run = False
        for evnen in pygame.event.get():
            # Проверка на выход из игры
            if evnen.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player[0] >= 10:
            pl.player_moving(-speed)
        if keys[pygame.K_RIGHT] and player[0] <= 450:
            pl.player_moving(speed)
        if keys[pygame.K_UP] and player[1] >= 320:  # and y > 370:
            pl.player_moving(None, -speed)
        if keys[pygame.K_DOWN] and player[1] <= 400:
            pl.player_moving(None, 10)
        if keys[pygame.K_SPACE] and time.time() - stop_time >= 0.3:
            a = Bullet(player[0], player[1])
            bull.append(a)
            stop_time = time.time()
        if keys[pygame.K_q]:
            # Выход из игры
            win.blit(screen_text("Game Over you Lose", 50, (255, 255, 255)), (50, 150))
            run = False

        #  Рисуем  Врагов, экран и Игрока
        try:
            for k in range(len(en)):
                en[k].drew()
                if text and en[k].y >=500:
                    del en[k]
                if bull_enemy[k] == 0 and (random.randint(1, 100) % 25) == 0:
                        bull_enemy[k] = Bullet(en[k].drew()[0], en[k].drew()[1])
        except IndexError:
            continue
        pl.pleyer_drew()
        player = pl.player_moving()
        bonus.drew()

        # Полет пули врега проверка на поподание
        if not shot_or_not(bull, en) or len(en) == 0:
            win.blit(screen_text("You Win the game", 50, (250, 255, 250)), (50, 200))
            run = False
        for im in range(6):
            try:
                if bull_enemy[im] == 0:
                    continue
                bull_enemy[im].shottiing(1)
                if bull_enemy[im].shottiing(1):
                    bull_enemy[im] = 0
                if bull_enemy[im].bullet_posittion2(pl.player_moving()):
                    run = pl.player_boom()
                    bull_enemy[im] = 0
            except AttributeError:
                continue

        if pl.player_posittion(bonus.drew()):
            bonus.y = -15
            pl.boom-=1


        if text:
            win.blit(screen_text(f"Score : {score}", 22, (255, 255, 255)), (530, 10))
            win.blit(screen_text(f"{len(en)} Enemys ",22, (255, 0, 0)), (530, 40))
            win.blit(screen_text(f"Shots to Die : {pl.shots_to_die()}", 22, (255, 255, 0)), (530, 80))
            win.blit(screen_text(f"Time to end {67 - (int(time.time()) - int(game_time))} ", 22, (255, 255, 0)),
                     (530, 120))
        pygame.display.update()
        if not text:
            but.Button()
            text = True

time.sleep(5)
pygame.quit()
