"""
Write a Python function that takes in two dictionaries representing the scores of two players in a 
game. Each dictionary contains the names of the players as keys and their scores as values. The 
function should return a new dictionary with the names of the players as keys and the difference 
in their scores as values. 
    
    """
def score_difference(player1_scores, player2_scores):
    score_diff = {}
    
    for player in player1_scores:
        if player in player2_scores:
            score_diff[player] = player1_scores[player] - player2_scores[player]
    
    return score_diff

# Example usage
player1_scores = {'Alice': 10, 'Bob': 15, 'Charlie': 20}
player2_scores = {'Alice': 8, 'Bob': 18, 'Charlie': 20}

diff = score_difference(player1_scores, player2_scores)
print(diff)  # Output: {'Alice': 2, 'Bob': -3, 'Charlie': 0}
