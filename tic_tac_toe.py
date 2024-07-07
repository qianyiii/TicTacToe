
class TicTacToe:
    def __init__(self):
        self.board = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' '
        }
        self.current_player = 'X'
        self.log_file = "tic_tac_toe_log.txt"
        self.init_log_file()

    def init_log_file(self):
        with open(self.log_file, 'w') as file:
            file.write("Tic-Tac-Toe Game Log\n")
            file.write("====================\n")

    def log_to_file(self, message):
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')

    def plain_text_board(self):
        board_state = (
            f"{self.board['top-l']} | {self.board['top-c']} | {self.board['top-r']}\n"
            "--+---+---\n"
            f"{self.board['mid-l']} | {self.board['mid-c']} | {self.board['mid-r']}\n"
            "--+---+---\n"
            f"{self.board['bot-l']} | {self.board['bot-c']} | {self.board['bot-r']}\n"
        )
        return board_state

    def color_text(self, text, color):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'reset': '\033[0m'
        }
        return f"{colors[color]}{text}{colors['reset']}"

    def print_board(self):
        def colored_cell(cell):
            if self.board[cell] == 'X':
                return self.color_text(self.board[cell], 'red')
            elif self.board[cell] == 'O':
                return self.color_text(self.board[cell], 'blue')
            else:
                return self.board[cell]

        board_state = (
            f"{colored_cell('top-l')} | {colored_cell('top-c')} | {colored_cell('top-r')}\n"
            "--+---+---\n"
            f"{colored_cell('mid-l')} | {colored_cell('mid-c')} | {colored_cell('mid-r')}\n"
            "--+---+---\n"
            f"{colored_cell('bot-l')} | {colored_cell('bot-c')} | {colored_cell('bot-r')}\n"
        )
        print(board_state)
        self.log_to_file(self.plain_text_board())

    def check_winner(self):
        lines = [
            # rows
            ['top-l', 'top-c', 'top-r'],
            ['mid-l', 'mid-c', 'mid-r'],
            ['bot-l', 'bot-c', 'bot-r'],
            # columns
            ['top-l', 'mid-l', 'bot-l'],
            ['top-c', 'mid-c', 'bot-c'],
            ['top-r', 'mid-r', 'bot-r'],
            # diagonals
            ['top-l', 'mid-c', 'bot-r'],
            ['top-r', 'mid-c', 'bot-l']
        ]
        
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return self.board[line[0]]
        return None

    def is_board_full(self):
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

    def play_game(self):
        welcome_message = self.color_text("Welcome to Tic-Tac-Toe!", 'blue')
        print(welcome_message)
        self.log_to_file("Welcome to Tic-Tac-Toe!")
        print()
        print("Positions are as follows:")
        self.log_to_file("Positions are as follows:")
        print()
        positions = (
            "top-l|top-c|top-r\n"
            "-----+-----+-----\n"
            "mid-l|mid-c|mid-r\n"
            "-----+-----+-----\n"
            "bot-l|bot-c|bot-r\n"
        )
        print(positions)
        self.log_to_file(positions)
        print()
        start_message = self.color_text("Let's start the game!", 'yellow')
        print(start_message)
        self.log_to_file("Let's start the game!")
        print()

        while True:
            self.print_board()
            print(f"Player {self.current_player}, enter your move (e.g., top-l, mid-c):", end=' ')
            move = input().strip()

            if move not in self.board:
                error_message = self.color_text("Invalid move! Try again.", 'red')
                print(error_message)
                self.log_to_file("Invalid move! Try again.")
                continue
            
            if self.board[move] != ' ':
                error_message = self.color_text(f"Position {move} already taken! Please try another move.", 'red')
                print(error_message)
                self.log_to_file(f"Position {move} already taken! Please try another move.")
                continue

            self.board[move] = self.current_player
            self.log_to_file(f"Player {self.current_player} moved to {move}")
            winner = self.check_winner()

            if winner:
                self.print_board()
                win_message = self.color_text(f"Congratulations! Player {winner} wins!", 'green')
                print(win_message)
                self.log_to_file(f"Congratulations! Player {winner} wins!")
                break
            elif self.is_board_full():
                self.print_board()
                draw_message = "Draw!"
                print(draw_message)
                self.log_to_file("Draw!")
                break
            else:
                # Switch turn
                self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
