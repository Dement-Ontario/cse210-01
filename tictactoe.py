"""
Assignment: W02 Prove: Developer - Solo Code Submission
Authors:
- Joseph Toronto
"""

def main():
    game_over = False
    whose_turn = 'x'
    player_choice = ''
    
    spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while not game_over:
        while player_choice not in spaces:
            print(f'{spaces[0]}|{spaces[1]}|{spaces[2]}')
            print(f'-+-+-')
            print(f'{spaces[3]}|{spaces[4]}|{spaces[5]}')
            print(f'-+-+-')
            print(f'{spaces[6]}|{spaces[7]}|{spaces[8]}')
            print()

            player_choice = input(f"{whose_turn}'s turn to choose a square (1-9): ")

            if player_choice not in spaces:
                print('Invalid choice. Please choose another space.')
                print()
        
        print()

        spaces[int(player_choice) - 1] = whose_turn
        player_choice = ''

        if whose_turn == 'x':
            whose_turn = 'o'
        else:
            whose_turn = 'x'
        
        game_over = tie_condition(spaces)
        game_over = win_condition(spaces)

    print(f'{spaces[0]}|{spaces[1]}|{spaces[2]}')
    print(f'-+-+-')
    print(f'{spaces[3]}|{spaces[4]}|{spaces[5]}')
    print(f'-+-+-')
    print(f'{spaces[6]}|{spaces[7]}|{spaces[8]}')
    print()

    print('Good game. Thanks for playing!')

def win_condition(spaces):
    # Horizontal
    if (spaces[0] == spaces[1] == spaces[2] or
    spaces[3] == spaces[4] == spaces[5] or
    spaces[6] == spaces[7] == spaces[8] or
    # Vertical
    spaces[0] == spaces[3] == spaces[6] or
    spaces[1] == spaces[4] == spaces[7] or
    spaces[2] == spaces[5] == spaces[8] or
    # Diagonal
    spaces[0] == spaces[4] == spaces[8] or
    spaces[2] == spaces[4] == spaces[6]):
        game_over = True
    else:
        game_over = False
    
    return game_over

def tie_condition(spaces):
    for space in range(len(spaces)):
        if spaces[space] != 'x' and spaces[space] != 'o':
            game_over = False
            break
        else:
            game_over = True
    
    return game_over

if __name__ == '__main__':
    main()