import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# 載入所有圖片並設定大小
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"),(60,60))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"),(25,25))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"),(25,25))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"),(50,50))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"),(50,50))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"),(50,50))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"),(50,50))

# 設定背景、遊戲名稱
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()
# 製作時間time
font = pygame.font.Font(None, 30)
time = time.time()

class Game:
    def __init__(self):
        # window
        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        #起始時間
        time = pygame.time.get_ticks()
        # game loop
        run = True
        while run:
            clock.tick(FPS)
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            win.blit(background_image, (0, 0))
            # draw enemy and health bar
            win.blit(enemy_image, (40, 230))
            pygame.draw.rect(win, (255, 0, 0), [45, 220, 60, 6])
            # draw menu (and buttons)
            pygame.draw.rect(win, (0, 0, 0), [0, 0, WIN_WIDTH, 80])
            win.blit(sound_image, (850, 20))
            win.blit(muse_image, (800, 20))
            win.blit(continue_image, (900, 20))
            win.blit(pause_image, (950, 20))

            win.blit(hp_gray_image, (460, 15))
            win.blit(hp_image, (460, 15))
            win.blit(hp_gray_image, (490, 15))
            win.blit(hp_image, (490, 15))
            win.blit(hp_gray_image, (520, 15))
            win.blit(hp_image, (520, 15))
            win.blit(hp_gray_image, (550, 15))
            win.blit(hp_image, (550, 15))
            win.blit(hp_gray_image, (580, 15))
            win.blit(hp_image, (580, 15))

            win.blit(hp_gray_image, (460, 40))
            win.blit(hp_image, (460, 40))
            win.blit(hp_gray_image, (490, 40))
            win.blit(hp_image, (490, 40))
            win.blit(hp_gray_image, (520, 40))
            win.blit(hp_gray_image, (550, 40))
            win.blit(hp_gray_image, (580, 40))

            # clock
            pygame.draw.rect(win, (0, 0, 0), [0, 560, 65, 40])#時間框框
            text_surface = font.render(str((pygame.time.get_ticks()-time) // 3600000) + ":" +
                                       str((pygame.time.get_ticks() - time) // 1000 % 60).zfill(2), True, (255, 255, 255))#印出時間
            win.blit(text_surface,(6, 570))
            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



