winner = False
full_board = False

class Player:
    def __init__(self, name):
        self.name = name

class Board:
    def __init__(self):
        self.board = []
    
    def create_board(self):
        board = []
        count = 0
        for x in range(7):
            if x % 2 == 0:
                rank = ['_' for _ in range(7)]
                board.append(rank)
            else:
                rank = ["|" if x % 2 == 0 else " " for x in range(7)]
                for i in range(len(rank)):
                    if rank[i] == " ":
                        count += 1
                        rank[i] = str(count)  # Ensure it's a string
                board.append(rank)
        return board
        
    def displayBoard(self):
        for row in self.board:
            print(" ".join(row))

    def checkIfBoardFull(self):
        number_of_open_squares = 0
        for row in self.board:
            for square in row:
                if str(square).isdigit():
                    number_of_open_squares += 1
        return number_of_open_squares == 0  # Returns True if board is full

    def chooseSpot(self, player):
        position = input(f"{player.name}, choose a square: ")
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == position:
                    self.board[row][column] = player.name
                    return player, row, column
        print("Square is occupied or invalid. Please select a different square.")
        return self.chooseSpot(player)

    def check_for_winner(self, player, row, column):
        symbol = player.name
        count = 1
        directions = [(0, -2), (2, 0), (2, 2), (-2, -2)]
        for dr, dc in directions:
            r, c = row + dr, column + dc
            while 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == symbol:
                count += 1
                r += dr
                c += dc
            r, c = row - dr, column - dc
            while 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == symbol:
                count += 1
                r -= dr
                c -= dc
            if count >= 3:
                print(f"{player.name} wins!")
                return True
            count = 1  # Reset for next direction
        return False

# Game setup
board1 = Board()
board1.board = board1.create_board()
board1.displayBoard()

playerX = Player('X')
playerO = Player('O')
player_list = [playerX, playerO]

switch_player = 0

while not winner and not full_board:
    player, row, column = board1.chooseSpot(player_list[switch_player])
    board1.displayBoard()
    winner = board1.check_for_winner(player, row, column)
    full_board = board1.checkIfBoardFull()
    switch_player = (switch_player + 1) % 2

if full_board and not winner:
    print("It's a draw!")
