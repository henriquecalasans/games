import guess as gs
import soccer as sc


def choose_game():
    if __name__ == '__main__':
        game = int(input("Which game do you want to play?{}{}{}{}{}".
                         format("\n", "1 - Guess game", "\n2 - Soccer" "\n3 - Skyrim ", "\n4 - Exit", "\n:")))

        if game == 1:
            print("Playing Guess game...")
            gs.play()

        elif game == 2:
            print("Playing Soccer...")
            sc.play()

        elif game == 3:
            print("Playing Skyrim...")

        else:
            exit()


if __name__ == "__main__":
    choose_game()
