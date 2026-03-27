import random
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Round:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.winner = self.find_winner()


    def find_winner(self):
        PLAYER_WINS = {(1, 3), (2, 1), (3, 2)}
        player_choice, computer_choice = self.player.value, self.computer.value
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice, computer_choice) in PLAYER_WINS:
            return "player"
        else:
            return "computer"

rounds = []
for i in range(0,3):
    player = Choice[input().upper()]
    computer = random.choice(list(Choice))
    rounds.append(Round(player, computer))
    print(f"Round {i+1}: ")
    print("\tPlayer choice: " + player.name)
    print("\tComputer choice: " + computer.name)
    print("\tWinner: " + rounds[i].winner)

player_wins = sum(1 for r in rounds if r.winner == "player")
print(player_wins)

computer_wins = sum(1 for r in rounds if r.winner == "computer")
print(computer_wins)

draws = sum(1 for r in rounds if r.winner == "draw")
print(draws)