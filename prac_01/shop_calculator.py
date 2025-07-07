def main():
    """ Take valid user input and return valid price and then calculate total price.
     based on total price apply discount    """
    number_of_items = get_valid_number()
    total_price = 0.0
    for i in range(number_of_items):
        total_price += get_valid_price()  # Get price of each item and add  to total price
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


def get_valid_number():
    """Take valid user input and return valid number."""
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    return number_of_items

def get_valid_price():
    """Take valid user input and return valid price."""
    price = float(input("Enter price: "))
    while price <= 0:
        print("Invalid price!")
        price = float(input("Enter price: "))
    return price



# Run the program
main()
