import guess as gs

if __name__ == '__main__':
    game = int(input("Which game do you want to play?{}{}{}{}".
                     format("\n", "1 - Guess game", "\n2 - Soccer" "\n3 - Skyrim ", "\n:")))

    if game == 1:
        print("Playing Guess game...")
        gs.play()

    elif game == 2:
        print("Playing Soccer...")
        exit()

    elif game == 3:
        print("Playing Skyrim...")
