import random

# Game constants and winning relations
CHOICES = ["rock", "paper", "scissors"]
WIN_CONDITIONS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

# Visual representations for UI feedback
CHOICE_EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}


def get_user_choice():
    """Prompts and validates the user's move selection."""
    while True:
        print("\nChoose your move:")
        print("  [1] Rock 🪨")
        print("  [2] Paper 📄")
        print("  [3] Scissors ✂️")
        choice = (
            input("Enter your choice (1/2/3 or rock/paper/scissors): ")
            .strip()
            .lower()
        )

        if choice in ["1", "rock", "r"]:
            return "rock"
        elif choice in ["2", "paper", "p"]:
            return "paper"
        elif choice in ["3", "scissors", "s"]:
            return "scissors"
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


def determine_winner(user_choice, computer_choice):
    """Determines round outcome: 'tie', 'user', or 'computer'."""
    if user_choice == computer_choice:
        return "tie"
    elif WIN_CONDITIONS[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"


def play_game():
    user_score = 0
    computer_score = 0
    ties = 0
    round_num = 1

    print("========================================")
    print("    🎮 ROCK, PAPER, SCISSORS GAME 🎮    ")
    print("========================================")

    while True:
        print(f"\n--- ROUND {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = random.choice(CHOICES)

        # Display Choices
        print("\n" + "-" * 35)
        print(
            f" You chose:     {user_choice.capitalize()} {CHOICE_EMOJIS[user_choice]}"
        )
        print(
            f" Computer chose: {computer_choice.capitalize()} {CHOICE_EMOJIS[computer_choice]}"
        )
        print("-" * 35)

        # Game Logic & Outcome
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            ties += 1
            print(" Result: It's a TIE! 🤝")
        elif result == "user":
            user_score += 1
            print(" Result: YOU WIN THIS ROUND! 🎉")
        else:
            computer_score += 1
            print(" Result: COMPUTER WINS THIS ROUND! 💻")

        # Display Score Tracking
        print(
            f"\n📊 SCOREBOARD | You: {user_score} | Computer: {computer_score} | Ties: {ties}"
        )

        # Play Again Prompt
        play_again = (
            input("\nDo you want to play another round? (y/n): ")
            .strip()
            .lower()
        )
        if play_again not in ["y", "yes"]:
            print("\n========================================")
            print("           FINAL GAME SUMMARY           ")
            print("========================================")
            print(f" Total Rounds Played: {round_num}")
            print(
                f" Final Score        : You [{user_score}] vs Computer [{computer_score}]"
            )

            if user_score > computer_score:
                print(" Overall Winner     : YOU ARE THE CHAMPION! 🏆")
            elif computer_score > user_score:
                print(" Overall Winner     : COMPUTER TOOK THE VICTORY! 🤖")
            else:
                print(" Overall Winner     : IT'S AN OVERALL DRAW! 🤝")

            print("\nThanks for playing! Goodbye!\n")
            break

        round_num += 1


if __name__ == "__main__":
    play_game()