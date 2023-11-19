from random import randint

def guessing_game():
    number = randint(0, 100)

    while True:
        guess = input("Guess what number has been chosen: ")

        try:
            isinstance(int(guess), int)
            break
        except ValueError:
            print('''You have typed something which is not an 
                  integer, please try again''')
            continue

    print(guess)

def main():
    guessing_game()

if __name__ == '__main__':
    main()
