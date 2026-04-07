import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Cross The Road'

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('sound/Music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 


new_game = Game('asset/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

pygame.quit()
quit()