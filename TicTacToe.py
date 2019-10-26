def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6), (9, 10, 11), (12, 13, 14), (15, 16, 17), (9, 12, 15), (10, 13, 16), (11, 14, 17), (9, 13, 17), (11, 13, 15), (18, 19, 20), (21, 22, 23), (24, 25, 26), (18, 21, 24), (19, 22, 25), (20, 23, 26), (18, 22, 26), (20, 22, 24), (0, 9, 18), (1, 10, 19), (2, 11, 20), (3, 12, 21), (4, 13, 22), (5, 14, 23), (6, 15, 24), (7, 16, 25), (8, 17, 26), (0, 10, 20), (20, 10, 0), (0, 12, 24), (24, 12, 0), (2, 14, 26), (26, 14, 2), (2, 10, 18), (18, 10, 2), (6, 12, 18), (18, 12, 6), (6, 16, 26), (26, 16, 6), (8, 14, 20), (20, 14, 8), (8, 16, 24), (24, 16, 8), (0, 13, 26), (26, 13, 0), (6, 13, 20), (20, 13, 6), (3, 13, 23), (23, 13, 3), (1, 13, 25), (25, 13, 1))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print(" ", board[9], board[10], board[11])
        print(" ", board[12], board[13], board[14])
        print(" ", board[15], board[16], board[17])
        print("    ", board[18], board[19], board[20])
        print("    ", board[21], board[22], board[23])
        print("    ", board[24], board[25], board[26])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 27):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()


tic_tac_toe()