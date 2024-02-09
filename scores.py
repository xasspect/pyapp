import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    '''Статистика'''
    def __init__(self, screen, stats):
        '''инициализируем подсчет очка'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (166, 230, 29)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_record()
        self.image_guns()

    def image_score(self):
        '''cчет в интрефейс'''
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = 20

    def image_record(self):
        ''' рекорд -> интерфейс'''
        self.ri = self.font.render(str(self.stats.record), True, self.text_color, (0,0,0))
        self.record_rect = self.ri.get_rect()
        self.record_rect.right = self.screen_rect.right - 40
        self.record_rect.top = 20
    def image_guns(self):
        ''' кол-во жизней'''
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 174 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        '''вывод счета на экран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.ri, self.record_rect)
        self.guns.draw(self.screen)

