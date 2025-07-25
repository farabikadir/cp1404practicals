def main():
    """Main function to run the score menu program."""
    score = get_valid_score()
    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Your result: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell! Have a great day.")
        else:
            print("Invalid choice, please try again.")


def print_menu():
    """Prints the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompts the user until a valid score (0–100) is entered."""
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or  score > 100:
            print("Invalid score.")
            score = int(input("Enter a valid score (0-100): "))
    return score 


def get_result(score):
    """Determine the result message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Prints a line of stars equal to the score."""
    print("*" * score)

main()