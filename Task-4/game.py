import random

class RockPaperScissorsGame:

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def display_score(self):
        print(f"\nScore:\nYou: {self.user_score}\nComputer: {self.computer_score}\n")

    def play_round(self):
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please select rock, paper, or scissors.")
            return

        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = self.determine_winner(user_choice, computer_choice)
        print(result)
        self.display_score()

    def play_game(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (Y/N): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()
