import random
import re
import string

boggle_board = [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
]
######## Part 1 : Not so smart boggle board ######## 
    # boggle_board = [
    #     ["Z","F","L","S"],
    #     ["E","H","N","W"],
    #     ["B","A","U","Y"],
    #     ["H","I","I","H"]
    # ]


    

    # def print_boggle_board() :
        
    #     for i in range (0, 4) :
    #         for j in range (0,4) :
    #             boggle_board[i][j] = random.choice(string.ascii_uppercase)
                
    #     for rows in boggle_board :
    #         print(' '.join(rows))
    
    
    # print_boggle_board()

####################################################



##### Part 2 : Smarter boggle board ####   

dice = [
    ['A', 'A', 'E', 'E', 'G', 'N'],
    ['E', 'L', 'R', 'T', 'T', 'Y'],
    ['A', 'O', 'O', 'T', 'T', 'W'], 
    ['A', 'B', 'B', 'J', 'O', 'O'],
    ['E', 'H', 'R', 'T', 'V', 'W'],
    ['C', 'I', 'M', 'O', 'T', 'U'],
    ['D', 'I', 'S', 'T', 'T', 'Y'],
    ['E', 'I', 'O', 'S', 'S', 'T'], 
    ['D', 'E', 'L', 'R', 'V', 'Y'], 
    ['A', 'C', 'H', 'O', 'P', 'S'], 
    ['H', 'I', 'M', 'N', 'Q', 'U'], 
    ['E', 'E', 'I', 'N', 'S', 'U'], 
    ['E', 'E', 'G', 'H', 'N', 'W'], 
    ['A', 'F', 'F', 'K', 'P', 'S'], 
    ['H', 'L', 'N', 'N', 'R', 'Z'], 
    ['D', 'E', 'I', 'L', 'R', 'X']
]
        

# --------------------------------
##### Shuffle the boggle board ####
# --------------------------------
def shuffle_smarter_boggle_board() :    
    
    # random shuffle
    random.shuffle(dice)
    
    for i in range (0, len(dice)) :
        random.shuffle(dice[i])

    dice_shuffled = dice
    
    for i in range (0, 4) :
        for j in range (0,4) :
            boggle_board[i][j] = random.choice(dice[i * 4 + j][0])    
            
    print(boggle_board)            
        
shuffle_smarter_boggle_board()


# --------------------------------
##### Print the boggle board in 4 x 4 #####
# --------------------------------
def print_smarter_boggle_board() :
    
    print("--------------")
    
    for rows in boggle_board :
            # board = '  '.join(rows).replace("Q", "Qu")
            ## substitute all words except "Q" to letter + ' '(space), then replace "Q" with "Qu". "join()" makes list into strings
            board = re.sub(r'([^Q])',r'\1 ','|'.join(rows)).replace("Q", "Qu")
            print(board)
            
    print("--------------")
           
print_smarter_boggle_board()


# --------------------------------
##### Start the game by giving word #####
# --------------------------------

end_game = False
score = 0

while end_game == False :
    # Ask for input
    print("Type 'exit!' to exit the game")
    word = input("Enter Word : \n").upper()
    
    if word == "EXIT!" :
        end_game = True
        continue
        
    while len(word) <= 1 :
        print_smarter_boggle_board()
        word = input("Enter more than 1 character ! : \n").upper()

    word_list = list(word)
    all_first_position = []
    first_char_horizontal = 0
    first_char_vertical = 0

    ##### Find first letter position in boggle board #####
    def get_first_char() :  
        
        for i in range(0, 1) :
            for j in range(0, len(boggle_board)) :
                for k in range(-1, len(boggle_board[j])) :    
                    try :
                        if boggle_board[j].index(word_list[i],k + 1) >= 0 :
                            first_char_horizontal = boggle_board[j].index(word_list[i],k + 1)
                            first_char_vertical = j
                            position = [first_char_vertical,first_char_horizontal]
                            all_first_position.append(position)
                            # print(f"k is : {k + 1}")
                            # print(f"index is : {boggle_board[j].index(word_list[i],k + 1)}")
                    except :
                        continue
        
        return all_first_position
        
    get_first_char()

    ##### Turn first characters to a list and make it unique #####
    unique_all_first_position = [list(item) for item in set(tuple(row) for row in all_first_position)]


    # --------------------------------
    ##### Check horizontal directions #####
    # --------------------------------
    def checkHorizontal() :
        
        match = False
        
        # check horizontal from left to right
        for i in range(0, len(unique_all_first_position)) :
            if match == True :
                return True
            else :    
                for j in range(1, len(word_list)) :
                    try :
                        if boggle_board[unique_all_first_position[i][0]][unique_all_first_position[i][1] + j] == word_list[j] :
                            match = True
                        else :
                            match = False
                            break
                            
                    except :
                        match = False
                            
        # check horizontal from right to left
        for i in range(0, len(unique_all_first_position)) :
            if match == True :
                return True
            else :    
                for j in range(1, len(word_list)) :
                    try:
                        if boggle_board[unique_all_first_position[i][0]][unique_all_first_position[i][1] - j] == word_list[j] :
                            match = True
                        else :
                            match = False
                            break
                    except: 
                        match = False
                        
        if match == False :
            return False
        else :
            return True
    
    
    
    if checkHorizontal() == True:
        print_smarter_boggle_board()
        print(f"You found the word horizontally !")
        score += 1
        print(f"Score: {score}")
        continue
     


    # --------------------------------
    ##### Check all vertical directions #####
    # --------------------------------

    def checkVertical () :
        match = False
        
        # check horizontal from left to right
        for i in range(0, len(unique_all_first_position)) :
            if match == True :
                return True
            else :    
                for j in range(1, len(word_list)) :
                    try :
                        if boggle_board[unique_all_first_position[i][0] + j][unique_all_first_position[i][1]] == word_list[j] :
                            match = True
                        else :
                            match = False
                            break
                            
                    except :
                        match = False
                            
        # check horizontal from right to left
        for i in range(0, len(unique_all_first_position)) :
            if match == True :
                return True
            else :    
                for j in range(1, len(word_list)) :
                    try:
                        if boggle_board[unique_all_first_position[i][0] - j][unique_all_first_position[i][1]] == word_list[j] :
                            match = True
                        else :
                            match = False
                            break
                    except: 
                        match = False
                        
        if match == False :
            return False
        else :
            return True
    
    if checkVertical() == True:
        print_smarter_boggle_board()
        print(f"You found the word vertically !")
        score += 1
        print(f"Score: {score}")
        continue
    


    # --------------------------------
    ##### Check all 8 directions #####
    # --------------------------------

    directions = [
        [+1, +0], #down
        [-1, +0], #up
        [+0, +1], #right
        [+0, -1], #left
        [+1, +1], #down right
        [-1, +1], #up right
        [-1, -1], #up left
        [+1, -1] #down left
    ]


    position = []
    next_position = []
    unique_next_position = []
    combined_results = []

    def checkAllDir (word, length, start) :
        count = length
        next_position = []
        unique_next_position = []
        
        if length <= 1 :
            return True
        else:     
            for i in range(0, len(start)) :           
                for j in range(0, len(directions)) :
                    
                        if boggle_board[min(3,max(0,start[i][0] + directions[j][0]))][min(3,max(0,start[i][1] + directions[j][1]))] == word[1] :
                            position = [min(3,max(0,start[i][0] + directions[j][0])),min(3,max(0,start[i][1] + directions[j][1]))]
                            next_position.append(position)
                            unique_next_position = [list(item) for item in set(tuple(row) for row in next_position)]
            
            del word[0]    
            
            if unique_next_position != [] :
                if checkAllDir(word, len(word), unique_next_position) == True :
                    return True
                else:
                    return False
                
            return False
    
    
    print_smarter_boggle_board()
    
    if checkAllDir(word_list, len(word_list), unique_all_first_position) == False:
        print(f"DEH! INCORRECT!")
        print(f"Score: {score}")

    else:
        print(f"You found the word ! (somehow...)")
        score += 1
        print(f"Score: {score}")




        
        
