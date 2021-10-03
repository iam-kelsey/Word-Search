# Project 4 - Word Search
#
# Name: Kelsey Nguyen
# Instructor: Workman

def organize_puzzle(strings):
    list_of_chars = []
    for i in range(0, 100, 10):
        x = strings[i:i+10]
        list_of_chars.append(x)
    return list_of_chars


def organize_words(words):
    x = words.split()
    return x


def go_forward(puzzle, word):
    row_count = -1
    col_count = -1
    for i in range(10):
            col = puzzle[i].find(word)
            if col != -1:
                row_count = i
                col_count = col
                return row_count, col_count
    return row_count, col_count
            

    

def go_backward(puzzle, word):  
    row_count = -1
    col_count = -1
    word = word[::-1]
    for i in range(10):
        col = puzzle[i].find(word)   
        if col != -1:
            col = col + len(word) - 1
            row_count = i
            col_count = col
            return row_count, col_count
    return row_count, col_count

    

def go_down(puzzle, word):
    row_count = -1
    col_count = -1
    new_puzzle = []
    for i in range(len(puzzle[0])):     #transpose puzzle
        row = ""
        for item in puzzle:
            row = row + item[i]
        new_puzzle.append(row)
    for i in range(10):
        col = new_puzzle[i].find(word)
        if col != -1:
            row_count = col
            col_count = i
            return row_count, col_count
    return row_count, col_count
   


def go_up(puzzle, word):
    row_count = -1
    col_count = -1
    new_puzzle = []
    for i in range(len(puzzle[0])):
        row = "" 
        for item in puzzle:
            row = row + item[i]
        new_puzzle.append(row)
    for i in range(10):
        col = new_puzzle[i].find(word[::-1])
        if col != -1:
            col = col + len(word) - 1
            row_count = col
            col_count = i
            return row_count, col_count
    return row_count, col_count    


def go_diagonal(puzzle,word):
    row_count = -1
    col_count = -1
    #new_puzzle = []
    for i in range(10):     
            #col = 0
            #row = i
            #puzzle[row][col]
            letters = ""
            for j in range(i, 10):
                letters = letters + puzzle[j][j-i]
            if letters.find(word) != -1:
                col_count = letters.find(word)
                row_count = i + col_count
                return row_count, col_count
    for i in range(10):     
        #col = 0
        #row = i
        #puzzle[row][col]
        letters = ""
        for j in range(i, 10):
            letters = letters + puzzle[j-i][j]    
        if letters.find(word) != -1:
            row_count = letters.find(word)
            col_count = i + row_count
            return row_count, col_count
    return row_count, col_count


        
            






        












        












    
