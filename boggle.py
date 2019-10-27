import random
import re
import string

boggle_board = [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
]

##### Part 1 : Not so smart boggle board #### 

# def print_boggle_board() :
    
#     for i in range (0, 4) :
#         for j in range (0,4) :
#             boggle_board[i][j] = random.choice(string.ascii_uppercase)
            
#     for rows in boggle_board :
#         print(' '.join(rows))
  
  
# print_boggle_board()



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
        
##### Shuffle the boggle board ####
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

##### Print the boggle board in 4 x 4 #####
def print_smarter_boggle_board() :
    
    print("--------------")
    
    for rows in boggle_board :
            # board = '  '.join(rows).replace("Q", "Qu")
            ## substitute all words except "Q" to letter + ' '(space), then replace "Q" with "Qu". "join()" makes list into strings
            board = re.sub(r'([^Q])',r'\1 ','|'.join(rows)).replace("Q", "Qu")
            print(board)
            
    print("--------------")
           
print_smarter_boggle_board()

##### Start the game by giving word #####
# Ask for input

word = input("Enter Word : \n").upper()

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


##### Check horizontal axis #####
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
        
print(f"Horizontal: {checkHorizontal()}")

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
    
print(f"Vertical: {checkVertical()}")

print(f"First position are : {unique_all_first_position}")
print(f"Word provided is : {word_list}")


##### Check all 8 directions #####

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

# print(directions)



# def checkAllDir() :
#     match = False
#     matches = []
    
#     # check horizontal from left to right
#     for i in range(0, len(unique_all_first_position)) :
#         if match == True :
#             return True
#         else :    
#             for j in range(1, len(word_list)) :
#                 for k in range(0, len(directions)) :
#                     if len(word_list) <=2 :
                        
#                         try :
#                             if boggle_board[unique_all_first_position[i][0] + directions[k][0]][unique_all_first_position[i][1] + directions[k][1]] == word_list[1] :
#                                 position = [unique_all_first_position[i][0] + directions[k][0],unique_all_first_position[i][1] + directions[k][1]]
#                                 matches.append(position)
#                                 print(f"first positions are : {unique_all_first_position[i][0]}, {unique_all_first_position[i][1]}")
#                                 print(f"{word_list[1]} matches are : {matches}")
#                             else :
#                                 continue
                                
#                         except :
#                             continue
                            
#                     else :
                        
                        
                
                        
#     if matches != [] :
#         return True
#     else :
#         return False
                        
# print(f"All matched directions: {checkAllDir()}")

dictOfWords = {}
position = []
next_position = []
unique_next_position = []
combined_results = []

def checkAllDir (word, length, start) :
    next_position = []

    if length <= 1 :
        return True
    else:
        for i in range(0, 1) :
            for j in range(0, len(directions)) :
                try:
                    if boggle_board[max(0,start[0][0] + directions[j][0])][max(0,start[0][1] + directions[j][1])] == word[1] :
                        position = [max(0,start[0][0] + directions[j][0]),max(0,start[0][1] + directions[j][1])]
                        next_position.append(position)
                        unique_next_position = [list(item) for item in set(tuple(row) for row in next_position)]
                        print(f"{start[0]} next is {unique_next_position}")
                        
                except :
                    continue
            
            del word[0]
            # unique_next_position = [list(item) for item in set(tuple(row) for row in next_position)]
            checkAllDir(word, len(word), unique_next_position)
    
    if unique_next_position != [] :
        combined_results.append(f"{start[0]} : True")
    else :
        combined_results.append(f"{start[0]} : False")
        
    return combined_results
    
    
    # if next_position != [] :
    #     return True
    # else :
    #     return False      
        
print(checkAllDir(word_list, len(word_list), unique_all_first_position))


    
    
