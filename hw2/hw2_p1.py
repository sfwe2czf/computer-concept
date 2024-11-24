"""
Programming assignment # 2
- Problem # 1: Hangman Game
"""
import random

word = 'white cucumber length computer ask crocodile celebrity drive zoo eight'


def game_start():
    token = int(input("Start game? "))
    """ Implement here """
    if token == 1:
        print("Start game")
    elif token == -1:
        print("Bye")
        return 0
    else:
        print("Not valid")
        return game_start()
    """ Do not modify function parameters and return """


def guess_letter(answer, guess_list, miss_list):
    letter = str(input("Guess a letter: "))
    """ Implement here """
    if (letter in guess_list) or (letter in miss_list):
        print("Not valid")
        guess_letter(answer, guess_list, miss_list)
    if letter in answer and letter not in guess_list:
        for i in range(0, len(answer)):
            if letter == answer[i]:
                guess_list[i] = letter
    elif letter not in answer and letter not in miss_list:
        miss_list.append(letter)
    """ Do not modify function parameters and return """


def draw_hangman(miss_list):
    if len(miss_list) == 0:
        print("")
    elif len(miss_list) == 1:
        print("  O  ")
    elif len(miss_list) == 2:
        print("   O  ")
        print(" --   ")
    elif len(miss_list) == 3:
        print("   O  ")
        print(" -- -- ")
    elif len(miss_list) == 4:
        print("   O  ")
        print(" --|-- ")
    elif len(miss_list) == 5:
        print("   O  ")
        print(" --|-- ")
        print("  /   ")
    elif len(miss_list) == 6:
        print("   O  ")
        print(" --|-- ")
        print("  / \  ")
        print("GAME OVER")


def print_letter(answer, guess_list, miss_list):
    """ Implement here """
    for i in range(0, len(guess_list)-1):
        print(f"{guess_list[i]}", end=" ")
    print(guess_list[-1])
    print(f"Wrong Letter: {miss_list}")
    for i in range(0, len(answer)):
        if guess_list[i] != answer[i]:
            return 0
    else:
        return 1

    """ Do not modify function parameters and return """

def random_generate(word_list):
    answer = word_list[random.randint(0, len(word_list) - 1)]
    return answer


def main():
    word_list = word.split(" ")
    print("HANGMAN GAME")

    while 1:
        guess_list = []
        miss_list = []
        """ Implement here """
        if game_start() == 0:
            break
        answer = random_generate(word_list)
        for i in range(0, len(answer)):
            guess_list.append("_")
        while 1:
            draw_hangman(miss_list)
            if len(miss_list) == 6:
                break
            elif print_letter(answer, guess_list, miss_list) == 1:
                print("Find answer")
                break
            guess_letter(answer, guess_list, miss_list)

        """ Do not modify function parameters and return """


if __name__ == "__main__":
    main()
