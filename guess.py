print("*************************")
print("Welcome to Guess game!!!")
print("*************************")

control = True

while control:

    try:

        tentatives = 0
        secret_number = 19
        round_game = 3

        while tentatives < 3:

            print("Round: {} of {} \n".format(tentatives + 1, round_game))

            try:

                guess_from_user = int(input("Digit your number: "))

                win = guess_from_user == secret_number
                bigger = guess_from_user > secret_number
                less = guess_from_user < secret_number

                if win:
                    print("You Win!!!")
                    exit()

                else:
                    if bigger:
                        print("Your number is greater than the secret number...")

                    elif less:
                        print("Your number is less than the secret number...")
                print("You missed ):")
                tentatives += 1
            except KeyboardInterrupt:
                print("Incorrect Key!")
        print("Game Over!!!")
        control = False

    except ValueError:
        print("No valid number")

        while True:

            try:

                again = input("Try again?, y or n: ").lower()

                if again == "y":
                    print("Continue game")
                    break

                elif again == "n":
                    print("Game closed!!!")
                    control = False
                    break

            except KeyboardInterrupt:
                print("Incorrect Key!")

