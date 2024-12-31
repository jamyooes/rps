import random
# Logic for rock paper scissors (RPS)
def rps(user):
    """
    Logic for Rock Paper Scissors
    
    The idea is that the outcomes are mapped in an array
    where 0 are ties, 1 is a player win, and -1 is a player loss
    
    The array is accessed using the player's choice for the x and 
    Ai's decision on the y.
    
    0 index = Rock
    1 index = Paper
    2 index = Scissor
        
    Input:
    user (int): Takes in the user's decision for RPS as an int
    
    Output:
    result (int): numerical result for the user's decision
    mappings[ai] (string): string representation of AI's choice for displaying
    mappings[user] (string): string representation of AI's choice for displaying
    """
    mappings = ['Rock', 'Paper', 'Scissors']
    ai = random.randint(0, 2)
    # x is the player's decision and y is the AI's decision
    decision = [[0, -1, 1],
                [1, 0, -1], 
                [-1, 1, 0]]
    result = decision[user][ai]
    # print(result)
    
    return result, mappings[ai], mappings[user]

