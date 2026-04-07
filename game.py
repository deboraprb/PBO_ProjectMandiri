import pygame
import sys
from player import PlayerCharacter
from enemy import EnemyCharacter
from game_object import GameObject

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('ComicSans', 75)
level_font = pygame.font.SysFont('ComicSans', 30)

class Game:
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
        
        self.hit_sound = pygame.mixer.Sound('sound/LoseMusic.wav')
        self.win_sound = pygame.mixer.Sound('sound/WinMusic.wav')
        
        pygame.mixer.music.load('sound/Music.mp3')

    def run_game_loop(self, level_speed):
        pygame.mixer.music.play(loops=-1)
        is_game_over = False
        did_win = False
        direction = 0
        
        show_instruction = True
        start_time = pygame.time.get_ticks()
        
        level = int(level_speed)

        player = PlayerCharacter('asset/Player.png', 410, 700, 50, 50)
        player2_img = pygame.transform.scale(
        pygame.image.load('asset/Player2.png'),
        (50, 50))

        enemy_0 = EnemyCharacter('asset/Enemy1.png', 20, 630, 50, 50)
        enemy_1 = EnemyCharacter('asset/Enemy2.png', self.width - 40, 480, 50, 50)
    

        enemy_0.SPEED *= level_speed
        enemy_1.SPEED *= level_speed
        

        goal = GameObject('asset/IcecreamCar.png', 375, 50, 120, 120)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    direction = 0

            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            goal.draw(self.game_screen)

            player.move(direction, self.height)
            player.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            
            if show_instruction:
                instruction_text = pygame.font.SysFont('ComicSans', 20).render(
                    'Tekan tombol UP untuk maju', True, BLACK_COLOR)

                text_rect = instruction_text.get_rect()
                text_rect.bottomright = (self.width - 10, self.height - 10)

                self.game_screen.blit(instruction_text, text_rect)

                if pygame.time.get_ticks() - start_time > 3000:
                    show_instruction = False

            if level_speed > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if player.detection_collision(enemy_0) or player.detection_collision(enemy_1):
                pygame.mixer.music.stop()
                player.image = player2_img
                player.draw(self.game_screen)
                self.hit_sound.play()  
                is_game_over = True
                text = font.render('You Lose!', True, BLACK_COLOR)
                self.game_screen.blit(text, (250, 350))
                pygame.display.update()
                pygame.time.delay(int(self.hit_sound.get_length() * 1000))

            elif player.detection_collision(goal):
                self.win_sound.play()  
                pygame.mixer.music.stop()
                is_game_over = True
                did_win = True
                text = font.render('You Win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (250, 350))
                pygame.display.update()
                pygame.time.delay(2000)
                
            level_text = level_font.render(f'Level: {int(level_speed)}', True, BLACK_COLOR)
            self.game_screen.blit(level_text, (10, 10))
            pygame.display.update()
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 1)
            
        while is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()