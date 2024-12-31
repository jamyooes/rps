# Main file containing the game loop
from button import Button
import pygame
import result
import rps_logic

# pygame setup
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# clock = pygame.time.Clock()
running = True

# Load images for buttons
rock_img = pygame.image.load('img/rock.jpg').convert_alpha()
paper_img = pygame.image.load('img/paper.jpg').convert_alpha()
scissor_img = pygame.image.load('img/scissor.jpg').convert_alpha()

# instantiate the button instance
rock_button = Button(300, 500, rock_img, 1.5, 1.5, 100, 100)
paper_button = Button(600, 500, paper_img, 1.5, 1.5, 100, 100)
scissor_button = Button(900, 500, scissor_img, 1.5, 1.5, 100, 100)

games_played = 0
player_games_won = 0
ai_won = 0
player_decision = ""
ai_decision = ""
game_result = 0
game_state = False

def game_won(game_result, ai_count, player_count):
    if game_result == -1:
        return ai_count + 1, player_count 
    elif game_result == 1:
        return ai_count, player_count + 1
    else:
        return ai_count, player_count

while running:
    # As per pygame docs poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button?
                if rock_button.rect.collidepoint(event.pos):
                    game_result, ai_decision, player_decision = rps_logic.rps(0)
                    ai_won, player_games_won = game_won(game_result, ai_won, player_games_won)
                elif paper_button.rect.collidepoint(event.pos):
                    game_result, ai_decision, player_decision = rps_logic.rps(1)
                    ai_won, player_games_won = game_won(game_result, ai_won, player_games_won)
                elif scissor_button.rect.collidepoint(event.pos):
                    game_result, ai_decision, player_decision = rps_logic.rps(2)
                    ai_won, player_games_won = game_won(game_result, ai_won, player_games_won)
                games_played += 1
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    # This will print out the buttons on the screen
    rock_button.draw(screen)
    paper_button.draw(screen)
    scissor_button.draw(screen)
    
    # This will print out the current status for the game
    result.result_text(ai_decision, player_decision, game_result, SCREEN_WIDTH, SCREEN_HEIGHT, ai_won, player_games_won, games_played).print_result(screen)
    # flip() the display to put your work on screen
    # pygame.display.flip()
    pygame.display.update()
    # clock.tick(60)  # limits FPS to 60

pygame.quit()