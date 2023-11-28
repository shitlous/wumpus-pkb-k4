import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QSplitter

from wumpus_world import WumpusWorld


class WumpusWorldSetup(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Wumpus World')
        self.setGeometry(150, 150, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QHBoxLayout(self.central_widget)

        # Left side layout for the game board
        self.game_board_widget = QWidget()
        self.game_board_layout = QGridLayout()
        self.game_board_widget.setLayout(self.game_board_layout)
        layout.addWidget(self.game_board_widget)

        # Right side layout for buttons
        self.button_widget = QWidget()
        self.button_layout = QVBoxLayout()
        self.button_widget.setLayout(self.button_layout)

        self.label = QLabel('Masukkan ukuran papan (5x5-10x10):')
        self.input_box = QLineEdit()
        self.submit_button = QPushButton('Mulai Permainan')
        self.simulate_button = QPushButton('Mulai Simulasi')
        self.restart_button = QPushButton('Mulai Ulang')
        self.simulate_button.hide()
        self.restart_button.hide()

        self.submit_button.clicked.connect(self.start_game)
        self.restart_button.clicked.connect(self.restart_game)
        self.simulate_button.clicked.connect(self.start_simulation)

        self.button_layout.addWidget(self.label)
        self.button_layout.addWidget(self.input_box)
        self.button_layout.addWidget(self.submit_button)
        self.button_layout.addWidget(self.simulate_button)
        self.button_layout.addWidget(self.restart_button)

        # Set the right side layout minimum width to 1/3 of the window
        self.button_widget.setMinimumWidth(self.width() // 5)
        layout.addWidget(self.button_widget)

        self.setFixedSize(1280, 720)  # Set a fixed window size

        self.show()

    def start_game(self):
        input_text = self.input_box.text().strip()

        if input_text:
            board_size = int(input_text)

            if 5 <= board_size <= 10:
                self.wumpus_world = WumpusWorld(board_size)
                board = self.wumpus_world.get_board()

                self.display_board(board, board_size)
                self.hide_start_game_elements()
                self.simulate_button.show()
                self.restart_button.show()
            else:
                print("Ukuran papan tidak valid. Masukkan ukuran antara 5 hingga 10.")
        else:
            print("Masukkan ukuran papan (5-10) sebelum memulai permainan.")

    def hide_start_game_elements(self):
        self.label.hide()
        self.input_box.hide()
        self.submit_button.hide()

    def display_board(self, board, board_size):
        for i in range(board_size):
            for j in range(board_size):
                
                if board[i][j] == 'A':  # If the cell contains the agent
                    label = QLabel('A')
                    label.setStyleSheet("border: 1px solid black;")
                    label.setAlignment(QtCore.Qt.AlignCenter)  # Display 'A'
                else:
                    label = QLabel(str(board[i][j]))
                    label.setStyleSheet("border: 1px solid black;")
                    label.setAlignment(QtCore.Qt.AlignCenter)

                self.game_board_layout.addWidget(label, i, j)

        # Unhide the board and adjust its layout
        self.game_board_widget.show()

    def update_agent_position(self, new_position):
        # Remove existing widgets from the grid layout
        for i in reversed(range(self.game_board_layout.count())):
            widget = self.game_board_layout.itemAt(i).widget()
            self.game_board_layout.removeWidget(widget)
            widget.deleteLater()

        # Display the updated board with the new agent position
        board = self.wumpus_world.get_board()  # Retrieve the current board
        self.display_board(board, self.wumpus_world.size)

    def restart_game(self):
        # Remove existing widgets from the grid layout
        for i in reversed(range(self.game_board_layout.count())):
            widget = self.game_board_layout.itemAt(i).widget()
            self.game_board_layout.removeWidget(widget)
            widget.deleteLater()

        self.label.show()
        self.input_box.show()
        self.submit_button.show()
        self.simulate_button.hide()
        self.restart_button.hide()
        self.game_board_widget.hide()

    def start_simulation(self):
        print("Simulation started!")
        path, final_position = self.wumpus_world.a_star_search()

        if final_position:
            self.update_agent_position(final_position)





def main():
    app = QApplication(sys.argv)
    window = WumpusWorldSetup()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
