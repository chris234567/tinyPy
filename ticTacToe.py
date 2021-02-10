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
            char = c
            winningLines = [
                [f'{char} | {char} | {char}', f'  |   |  ', f'  |   |  '],  # top line
                [f'  |   |  ', f'{char} | {char} | {char}', f'  |   |  '],  # middle line
                [f'  |   |  ', f'  |   |  ', f'{char} | {char} | {char}'],  # bottom line
                [f'{char} |   |  ', f'{char} |   |  ', f'{char} |   |  '],  # left line
                [f'  |   | {char}', f'  |   | {char}', f'  |   | {char}'],  # right line
                [f'  | {char} |  ', f'  | {char} |  ', f'  | {char} |  '],  # center line
                [f'{char} |   |  ', f'  | {char} |  ', f'  |   | {char}'],  # left diagonal
                [f'  |   | {char}', f'  | {char} |  ', f'{char} |   |  '],  # right diagonal
            ]

            if self.field[0] == winningLines[0][0]:
                self.finished = True  # top line
            elif self.field[1] == winningLines[1][1]:
                self.finished = True  # middle line
            elif self.field[2] == winningLines[2][2]:
                self.finished = True  # bottom line
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

        player = 1 if char == 'X' else 'O'

        if self.finished:  # should not print again if game already won
            print(f'Congratulations Player {player} won')

    # def checkInput(self,y , x):
    #     if not type(x) is int:
    #         print

    def gameInput(self):
        print('Y-Koordinate: ', end='')
        y = int(input())
        print('X-Koordinate: ', end='')
        x = int(input())
        return (y, x)

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
        x = self.shiftIndex(x)

        if self.field[y][x] != ' ':  # loop to cover invalid input
            invalid = True
            while invalid:
                print('Position schon besetzt! Bitte neuen Spielzug eingeben:')
                moves = self.gameInput()
                y = moves[0]
                x = moves[1]
                x = self.shiftIndex(x)
                if self.field[y][x] == ' ':
                    invalid = False

        for c in range(len(self.field[y])):
            if c == x:
                temp += sym
                continue
            temp += self.field[y][c]

        self.field[y] = temp  # update field with move
        self.printField()
        self.checkWin()


def main():
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
    main()