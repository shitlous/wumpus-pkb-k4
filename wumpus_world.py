import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.place_pits()
        self.place_wumpus()
        self.place_gold()
        self.agent_x = random.randint(
            0, self.size - 1)  # Koordinat X awal agen
        self.agent_y = random.randint(
            0, self.size - 1)  
        
        while self.board[self.agent_x][self.agent_y] != ' ':
            self.agent_x = random.randint(0, self.size - 1)
            self.agent_y = random.randint(0, self.size - 1)
        
    # Koordinat Y awal agen

    def place_pits(self):
        num_pits = self.size
        pits_placed = 0

        while pits_placed < num_pits:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if self.board[x][y] == ' ':  # Jika sel masih kosong
                self.board[x][y] = 'P'
                pits_placed += 1
                
    def place_wumpus(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        if self.board[x][y] == ' ':  # Jika sel masih kosong
            # Inisialisasi papan dengan ukuran yang telah ditentukan
            self.board[x][y] = 'W'
    
    def place_gold(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if self.board[x][y] == ' ':  # Jika sel masih kosong
                self.board[x][y] = 'G'
                break

    def a_star_search(self):
        start_state = {
            'position': (self.agent_x, self.agent_y),
            'explored': set(),
            'path': [],
            'cost': 0
        }

        goal = 'G'

        frontier = [start_state]

        while frontier:
            current_state = frontier.pop(0)
            current_position = current_state['position']

            # Print the current position being explored
            print(f"Exploring position: {current_position}")

            if self.board[current_position[0]][current_position[1]] == goal:
                print("Goal reached!")
                return current_state['path'], current_position  # Return the path and final position

            if current_position not in current_state['explored']:
                current_state['explored'].add(current_position)
                for action in self.get_valid_actions(current_position):
                    new_state = self.get_successor_state(current_state, action)
                    if new_state:
                        frontier.append(new_state)
                frontier.sort(key=lambda x: x['cost'])

        print("Goal not reachable!")
        return None, None  # Return None for path and position if the goal is not reachable

    def get_valid_actions(self, position):
        valid_actions = []
        x, y = position
        if x > 0 and self.board[x - 1][y] != 'P':
            valid_actions.append((-1, 0))
        if x < self.size - 1 and self.board[x + 1][y] != 'P':
            valid_actions.append((1, 0))
        if y > 0 and self.board[x][y - 1] != 'P':
            valid_actions.append((0, -1))
        if y < self.size - 1 and self.board[x][y + 1] != 'P':
            valid_actions.append((0, 1))
        return valid_actions

    def get_successor_state(self, state, action):
        x, y = state['position']
        dx, dy = action
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < self.size) or not (0 <= new_y < self.size):
            return None

        new_position = (new_x, new_y)
        if new_position in state['explored']:
            return None

        new_board = [row[:] for row in self.board]
        new_state = {
            'position': new_position,
            'explored': set(state['explored']),
            'path': list(state['path']),
            'cost': state['cost'] + 1
        }

        new_state['path'].append(new_position)
        new_state['explored'].add(new_position)

        return new_state

    def get_board(self):
        # Menambahkan agen ke papan permainan
        self.board[self.agent_x][self.agent_y] = 'A'

        # Menambahkan wumpus ke papan permainan
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'W':
                    self.board[i][j] = 'W'

        for i in range(self.size):
            for j in range(self.size):
            # Cek lokasi pits
                if self.board[i][j] == 'P':
                    # Mengecek seluruh sekitar pits untuk menambahkan breeze
                    if i > 0 and self.board[i - 1][j] != 'P' and 'B' not in self.board[i - 1][j] and self.board[i - 1][j] != 'W':
                        self.board[i - 1][j] += 'B'  # Breeze
                    if i < self.size - 1 and self.board[i + 1][j] != 'P' and 'B' not in self.board[i + 1][j] and self.board[i + 1][j] != 'W':
                        self.board[i + 1][j] += 'B'  # Breeze
                    if j > 0 and self.board[i][j - 1] != 'P' and 'B' not in self.board[i][j - 1] and self.board[i][j - 1] != 'W':
                        self.board[i][j - 1] += 'B'  # Breeze
                    if j < self.size - 1 and self.board[i][j + 1] != 'P' and 'B' not in self.board[i][j + 1] and self.board[i][j + 1] != 'W':
                        self.board[i][j + 1] += 'B'  # Breeze
                
                # Cek lokasi wumpus
                if self.board[i][j] == 'W':
                    # Mengecek seluruh sekitar wumpus untuk menambahkan stench
                    if i > 0 and self.board[i - 1][j] != 'W' and 'S' and 'G' not in self.board[i - 1][j] and self.board[i - 1][j] != 'P':
                        self.board[i - 1][j] += 'S'  # Stench
                    if i < self.size - 1 and self.board[i + 1][j] != 'W' and 'S' and 'G' not in self.board[i + 1][j] and self.board[i + 1][j] != 'P':
                        self.board[i + 1][j] += 'S'  # Stench
                    if j > 0 and self.board[i][j - 1] != 'W' and 'S' and 'G' not in self.board[i][j - 1] and self.board[i][j - 1] != 'P':
                        self.board[i][j - 1] += 'S'  # Stench
                    if j < self.size - 1 and self.board[i][j + 1] != 'W' and 'S' and 'G' not in self.board[i][j + 1] and self.board[i][j + 1] != 'P':
                        self.board[i][j + 1] += 'S'  # Stench

        return self.board
