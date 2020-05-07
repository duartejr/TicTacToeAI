from random import randint

class TicTacToe:
    table = []
    status = 0  # status 0 = unfinished, 1 = win, 2 = draw
    winner = ''
    
    def __init__(self, init_table):
        if not init_table:
            self.table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        else:
            for i in range(0, len(init_table), 3):
                line = init_table[i:i+3].replace('_', ' ')
                self.table.insert(0, list(line))

    def print_table(self):
        print('-'*9)
        for line in range(len(self.table)-1, -1, -1):
            print('| '+' '.join(self.table[line])+' |')
        print('-'*9)

    def make_move(self, coords, char, msg=True):

        if len(coords) == 1:
            print("You should enter numbers!")
            self.is_finished(char)
            return False

        y, x = coords[0], coords[1]

        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
            self.is_finished(char)
            return False

        y = int(coords[0]) - 1
        x = int(coords[1]) - 1

        if not(-1 < x < 3) or not(-1 < y < 3):
            print("Coordinates should be from 1 to 3!")
            self.is_finished(char)
            return False

        if self.table[x][y] != " ":
            if msg:
                print("This cell is occupied! Choose another one!")
            self.is_finished(char)
            return False

        self.table[x][y] = char
        self.is_finished(char)

        return True

    def is_finished(self, char):
        n_occurrences = self.count_moves(char)
        for l in self.table:
            if l.count(char) == 3:
                self.status = 1
        # check columns
        for i in range(3):
            if self.table[0][i] == self.table[1][i] == self.table[2][i] == char:
                self.status = 1
        # check main diagonal
        if self.table[0][0] == self.table[1][1] == self.table[2][2] == char:
            self.status = 1
        if self.table[0][2] == self.table[1][1] == self.table[2][0] == char:
            self.status = 1
        n = 0
        for i in self.table:
            n += i.count(" ")
        if n == 0:
            self.status = 2

        if self.status == 1:
            self.winner = f"{char} wins"
        if self.status == 2:
            self.winner = "Draw"

    def count_moves(self, char):
        n = []

        count_lines = []
        for l in self.table:
            count_lines.append(str(l).count(char))
        n.append(count_lines)

        count_columns = []
        for c in range(3):
            x = []
            for l in range(3):
                x.append(self.table[l][c])
            count_columns.append(str(x).count(char))
        n.append(count_columns)

        count_diagonal = []
        diagonal = [self.table[0][0], self.table[1][1], self.table[2][2]]
        count_diagonal.append(str(diagonal).count(char))
        diagonal = [self.table[0][2], self.table[1][1], self.table[2][1]]
        count_diagonal.append(str(diagonal).count(char))
        n.append(count_diagonal)

        return n


class User:

    def __init__(self, mode, char):
        self.mode = mode
        self.char = char

    def __human_mode(self, game):
        while True:
            coords = tuple(input('Enter the coordinates: ').split(' '))
            user_movement = game.make_move(coords, self.char)
            if user_movement:
                break

    def __easy_mode(self, game):
        print('Making move level "easy"')
        while True:
            coords = (str(randint(1, 3)), str(randint(1, 3)))
            easy_movement = game.make_move(coords, self.char, False)
            if easy_movement:
                break

    def __medium_mode(self, game):
        print('Making move level "medium"')
        while True:
            break

    def move(self, game):
        movements = {'user': self.__human_mode, 'easy': self.__easy_mode}
        movements[self.mode](game)


def gaming(use01, use02):
    user_01 = User(use01, 'X')
    user_02 = User(use02, 'O')
    game = TicTacToe("")
    game.print_table()

    while game.status == 0:
        user_01.move(game)
        game.print_table()
        if game.status != 0:
            break
        user_02.move(game)
        game.print_table()
        print(game.count_moves('X'))

    print(game.winner)


while True:
    command = input("Input command: ")

    if command == "exit":
        break

    if command.split(" ")[0] == "start":
        if len(command.split(" ")) != 3:
            print("Bad parameters!")
        else:
            _, user01, user02 = command.split(" ")
            gaming(user01, user02)
    else:
        print("Invalid command")
