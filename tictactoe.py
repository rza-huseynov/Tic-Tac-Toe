board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def board_reset() :
    
    for i in range(len(board)) :
        board[i] = ' '

def display_board() :
    for i in range(0, 9, 3) :
        print(' {} | {} | {} '.format(board[i], board[i + 1], board[i + 2]))
        if (i == 0 or i == 3) :
            print('-' * 11)

def player_choice() :
    
    choice = 'WRONG'
    
    while (choice not in ['X', 'O']) :
        
        choice = input('Please choose your side - (X or O): ')
        
        if (choice not in ['X', 'O']) :
            print('Sorry, there is no such side')
    
    return choice

def other_player(player_one) :
    
    if (player_one == 'X') :
        return 'O'
    else :
        return 'X'

def board_value_checker(position) :
    
    return (board[position].isspace())

def place_marker(side) :
    
    position = 10
    valid_position = False
    
    while (position not in range(1, 10) or not valid_position) :
        
        position = int(input('Enter your next position (1 - 9): '))
        
        if (position not in range(1, 10)) :
            print('Position must be in range (1 - 9)')
        else :
            valid_position = board_value_checker(position - 1)
            if (not valid_position) :
                print('This position is occupied!')
    
    position -= 1
    board[position] = side
    
    display_board()

def win_check() :
    
    win_cases = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [3, 4, 5], [6, 7, 8], [1, 4, 7], [2, 5, 8], [2, 4, 6]]
    
    ans = False
    
    for case in win_cases :
        cur = True
        for i in case :
            cur &= (not board[i].isspace())
        cur &= (board[case[0]] == board[case[1]] and board[case[1]] == board[case[2]])
        ans |= cur
        if (cur) :
            print('The winning case is: {}'.format(case))
    
    return ans

def tie_check() :
    
    for i in board :
        if (i.isspace()) :
            return False
    
    return True

def replay() :
    
    choice = 'WRONG'
    
    while (choice not in ['Y', 'N']) :
        
        choice = input('Keep Playing? (Y or N)')
        
        if (choice not in ['Y', 'N']) :
            print('Choose (Y or N)')
    
    return (choice == 'Y')

# GAME ON!


# Game Setup

print('Welcome to the Tic-Tac-Toe! Enjoy!')

gameon = True

while (gameon) :
    
    playon = True
    
    board_reset()
    
    display_board()
    
    player_one = player_choice()

    player_two = other_player(player_one)
    
    while (playon) :
        
        place_marker(player_one)
        
        have_winner = win_check()
        
        if (have_winner) :
            print('Congratulations! You win!')
            break
        
        have_tie = tie_check()
        
        if (have_tie) :
            print('TIE GAME!')
            break
         
        place_marker(player_two)
        
        have_winner = win_check()
        
        if (have_winner) :
            print('Congratulations! You win!')
            break
        
        have_tie = tie_check()
        
        if (have_tie) :
            print('TIE GAME!')
            break
            
    gameon = replay()

print('Well Done!')
