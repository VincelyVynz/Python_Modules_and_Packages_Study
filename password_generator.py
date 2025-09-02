import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def generate_password(c=4, d=3, s=3):
    """
    Generates a random password.

    Args:
        c (int): Number of alphabet characters to include. Default set to 4.
        d (int): Number of digits to include. Default set to 3.
        s (int): Number of special characters to include. Default set to 3.

    Returns:
        str: A randomly generated password combining letters, digits, and special characters.
    """
    pd_list = []

    for _ in range(c):
        char = random.choice(alphabets)
        pd_list.append(char)

    for _ in range(d):
        char = random.choice(digits)
        pd_list.append(char)

    for _ in range(s):
        char = random.choice(special_chars)
        pd_list.append(char)

    random.shuffle(pd_list)
    pd_str = "".join(pd_list)
    return pd_str



