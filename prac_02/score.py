import random

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

def main():
    """ Take a score between 0 and 100 and output the result."""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    # Generate a random score and print its result
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(get_result(random_score))

main()
