from random import randint

def guessing_game():
    number = randint(0, 100)

    while True:
        guess = input("Guess what number (integer) has been chosen: ")

        try:
            if (isinstance(int(guess), int)):
                guess = int(guess)

            if guess > number:
                print('Too high, try again\n')
                continue
            elif guess < number:
                print('Too low, try again\n')
                continue
            else:
                print(f'Just right, the number is {number}\n')
                break

        except ValueError:
            print('''You have typed something which is not an integer, please try again\n''')
            continue

def main():
    guessing_game()

if __name__ == '__main__':
    main()
