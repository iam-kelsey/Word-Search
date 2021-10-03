# Project 4 - Word Search
#
# Name: Kelsey Nguyen
# Instructor: Workman


from funcs import *


def main():

    strings = input()
    words = input()

    puzzle = organize_puzzle(strings)
    word_list = organize_words(words)

    print("Puzzle:\n")
    for x in puzzle:
        print(x)
    print()
    for word in word_list:
        result1 = go_forward(puzzle, word)
        if result1 != (-1, -1):
            print(word + ": (FORWARD)", "row:", result1[0], "column:", result1[1])
        result2 = go_backward(puzzle, word)
        if result2 != (-1, -1):
            print(word + ": (BACKWARD)", "row:", result2[0], "column:", result2[1])
        result3 = go_down(puzzle, word)
        if result3 != (-1, -1):
            print(word + ": (DOWN)", "row:", result3[0], "column:", result3[1])
        result4 = go_up(puzzle, word)
        if result4 != (-1, -1):
            print(word + ": (UP)", "row:", result4[0], "column:", result4[1])
        result5 = go_diagonal(puzzle, word)
        if result5 != (-1, -1):
            print(word + ": (DIAGONAL)", "row:", result5[0], "column:", result5[1])
        if result1 == result2 == result3 == result4 == result5 == (-1,-1):
            print(word + ": " + "word not found")











if __name__ == '__main__':
   main()