import pygame

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)


    def draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))