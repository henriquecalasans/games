import random as rd


def play():
    print("*************************")
    print("Welcome to Guess game!!!")
    print("*************************")

    control = True

    lv_easy = 10
    lv_medium = 5
    lv_hard = 3

    score = 1000
    tentatives = 0

    while control:

        try:
            level = int(input("Choose the level  {}1 - Easy {}2 - Medium {}3 - Hard {}:"
                              .format("\n", "10 Rounds\n", "5 Rounds\n", "3 Rounds\n")))

            if level == 1:
                round_game = lv_easy
            elif level == 2:
                round_game = lv_medium
            else:
                round_game = lv_hard

            secret_number = rd.randrange(1, 101)

            while tentatives < round_game:

                print("Round: {} of {} \n".format(tentatives + 1, round_game))

                try:
                    print("Score: {}".format(score))
                    guess_from_user = int(input("Enter a number between 1 and 100: "))

                    win = guess_from_user == secret_number
                    bigger = guess_from_user > secret_number
                    less = guess_from_user < secret_number

                    if guess_from_user < 1 or guess_from_user > 100:
                        continue

                    elif win:
                        print("You Win!!!{}Your Score: {}".format("\n", score))
                        exit()

                    else:
                        if bigger:
                            print("Your number is greater than the secret number...")

                        elif less:
                            print("Your number is less than the secret number...")
                    print("You missed ):")
                    tentatives += 1
                    lost_points = abs(secret_number - guess_from_user)
                    score -= lost_points

                except KeyboardInterrupt:
                    print("Incorrect Key!")

            print("Game Over!!!")
            print("Secret number is: {}".format(secret_number))
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


if __name__ == '__main__':
    play()
