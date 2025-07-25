
def main():
    """This function takes password from user and print asterisk"""
    password= get_password()
    print_asterisk(password)


def get_password():
    """Take a valid password from user"""
    MIN_LENGTH = 8
    password=input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Your password must be at least {MIN_LENGTH} characters long")
        password = input("Enter your password: ")
    return password

def print_asterisk(password):
    """ Print asterisk same length as password"""
    print('*' * len(password))


main()