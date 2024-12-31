# A class for UI for the RPS choices for the player
import pygame
# Buttons 
class Button():
    def __init__(self, x, y, image, scale_x = 1, scale_y = 1, set_x = 0, set_y = 0):
        width = image.get_width()
        height = image.get_height()
        if set_x and set_y:
            self.image = pygame.transform.scale(image, (set_x * scale_x, set_y * scale_y))
        else:
            self.image = pygame.transform.scale(image, (int(width * scale_x), int(height * scale_y)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.game_state = False
    
    def draw(self, surface):
        # draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))