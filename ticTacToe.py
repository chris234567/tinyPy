class TicTacToe:
    symbols = ['X', 'O']
    field = ['  |   |  ', '  |   |  ', '  |   |  ']
    finished = False


    def printField(self):
        for y in self.field:
            print(y)


    def checkWin(self):
        for c in self.symbols:
            if self.finished:
                break

            # winningLines = [
            #     [f'{char} | {char} | {char}', f'  |   |  ', f'  |   |  '],  # top line
            #     [f'  |   |  ', f'{char} | {char} | {char}', f'  |   |  '],  # middle line
            #     [f'  |   |  ', f'  |   |  ', f'{char} | {char} | {char}'],  # bottom line
            #     [f'{char} |   |  ', f'{char} |   |  ', f'{char} |   |  '],  # left line
            #     [f'  |   | {char}', f'  |   | {char}', f'  |   | {char}'],  # right line
            #     [f'  | {char} |  ', f'  | {char} |  ', f'  | {char} |  '],  # center line
            #     [f'{char} |   |  ', f'  | {char} |  ', f'  |   | {char}'],  # left diagonal
            #     [f'  |   | {char}', f'  | {char} |  ', f'{char} |   |  '],  # right diagonal
            # ]

            pattern = f'{c} | {c} | {c}'

            if self.field[0] == pattern or self.field[1] == pattern or self.field[2] == pattern:
                self.finished = True  # top, middle and bottom line
            elif self.field[0][0] == c and self.field[1][0] == c and self.field[2][0] == c:
                self.finished = True  # left line
            elif self.field[0][8] == c and self.field[1][8] == c and self.field[2][8] == c:
                self.finished = True  # right line
            elif self.field[0][4] == c and self.field[1][4] == c and self.field[2][4] == c:
                self.finished = True  # center line
            elif self.field[0][0] == c and self.field[1][4] == c and self.field[2][8] == c:
                self.finished = True  # left diagonal
            elif self.field[0][8] == c and self.field[1][4] == c and self.field[2][0] == c:
                self.finished = True  # right diagonal

            player = 1 if c == 'X' else 'O'

            if self.finished:  # should not print again if game already won
                print(f'Congratulations Player {player} won')


    def gameInput(self):
        print('Y-Koordinate: ', end='')
        y = input()
        print('X-Koordinate: ', end='')
        x = input()

        while self.checkNone(y) or self.checkNone(x):
            print('Y-Koordinate: ', end='')
            y = input()
            self.checkNone(y)
            print('X-Koordinate: ', end='')
            x = input()

        return (int(y), int(x))


    def checkInput(self, y, x):
        b = False
        if not type(y) is int or not type(x) is int:
            b = True
        elif not 0 <= y <= 2 or not 0 <= x <= 2:
            b = True
        if b:
            print('Achtung! Ungueltige Eingabe.')
            return b
        return b


    def checkNone(self, a):
        if a == None or a == '':
            print('Achtung! Keine Eingabe!')
            return True
        return False


    def shiftIndex(self, x: int):
        if x == 1:  # change x to proper string index
            return 4
        elif x == 2:
            return 8
        else:
            return 0


    def makeMove(self, y: int, x: int, sym: str):
        # possible positions: (0, 0), (0, 4), (0, 8), (1, 0), (1, 4), (1, 8), (2, 0), (2, 4), (2, 8)
        temp = ''
        moves = (y, x)
        while self.checkInput(y, x):
            moves = self.gameInput()
            y = moves[0]
            x = moves[1]

        y = moves[0]
        x = self.shiftIndex(moves[1])

        if self.field[y][x] != ' ':  # loop to cover invalid input
            invalid = True
            while invalid:
                print('Position schon besetzt! Bitte neuen Spielzug eingeben:')
                moves = self.gameInput()
                y = moves[0]
                x = moves[1]
                while not self.checkInput(y, x):
                    moves = self.gameInput()
                x = self.shiftIndex(moves[1])
                if self.field[moves[0]][x] == ' ':
                    invalid = False

        for c in range(len(self.field[y])): # build string as new line for field
            if c == x:
                temp += sym
                continue
            temp += self.field[y][c]

        self.field[y] = temp  # update field with move
        self.printField()
        self.checkWin()


def game():
    spiel = TicTacToe()
    spiel.printField()
    while not spiel.finished:
        print('Bitte Sieler 1 (X) Spielzug eingeben: ')
        moves = spiel.gameInput()
        spiel.makeMove(moves[0], moves[1], spiel.symbols[0])
        if spiel.finished:
            break
        print('Bitte Sieler 2 (O) Spielzug eingeben: ')
        moves = spiel.gameInput()
        spiel.makeMove(moves[0], moves[1], spiel.symbols[1])


if __name__ == '__main__':
    game()