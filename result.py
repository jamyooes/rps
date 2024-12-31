# result display
import pygame
class result_text():
    def __init__(self, ai, player, result, screen_width, screen_height, ai_won, player_won, game_count):
        self.ai = ai
        self.player = player
        self.result = result
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ai_win_count = ai_won
        self.player_win_count = player_won
        self.game_count = game_count
    def print_result(self, surface):
        text = ""
        text_rect = ""
        font = pygame.font.SysFont('Arial', 25)
        black = (0, 0, 0)
        if self.result == -1:
            text = font.render(f"You lose! Enemy chose {self.ai} and you chose {self.player}",
                               True, 
                               black)
            text_rect = text.get_rect()
            text_rect.center = (self.screen_width // 2, self.screen_height // 2)
        elif self.result == 1:
            text = font.render(f"You win! Enemy chose {self.ai} and you chose {self.player}",
                               True, 
                               black)
            text_rect = text.get_rect()
            text_rect.center = (self.screen_width // 2, self.screen_height // 2)
        else:
            text = font.render(f"Tie! Enemy chose {self.ai} and you chose {self.player}",
                               True, 
                               black)
            text_rect = text.get_rect()
            text_rect.center = (self.screen_width // 2, self.screen_height // 2)

        surface.blit(text, text_rect)
        
        # Display win count for AI and player
        ai_win_text = font.render(f"Enemy wins: {self.ai_win_count}",
                               True, 
                               black)
        ai_win_text_rect = ai_win_text.get_rect()
        ai_win_text_rect.center = (self.screen_width // 2 + 200, self.screen_height // 2 - 200)
        surface.blit(ai_win_text, ai_win_text_rect)
        
        player_win_text = font.render(f"Your wins: {self.player_win_count}",
                               True, 
                               black)
        player_win_text_rect = player_win_text.get_rect()
        player_win_text_rect.center = (self.screen_width // 2 - 200, self.screen_height // 2 - 200)
        surface.blit(player_win_text, player_win_text_rect)
        
        game_count = font.render(f"Game count: {self.game_count}",
                               True, 
                               black)
        game_count_rect = game_count.get_rect()
        game_count_rect.center = (self.screen_width // 2, self.screen_height // 2 - 200)
        surface.blit(game_count, game_count_rect)
        
        return self.ai_win_count, self.player_win_count