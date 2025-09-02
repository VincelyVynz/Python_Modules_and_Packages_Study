import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def generate_password(c, d, s):
    pd_list = []

    for _ in range(c):
        char = random.choice(alphabets)
        if char not in pd_list:
            pd_list.append(char)

    for _ in range(d):
        char = random.choice(digits)
        if char not in pd_list:
            pd_list.append(char)

    for _ in range(s):
        char = random.choice(special_chars)
        if char not in pd_list:
            pd_list.append(char)

    print(pd_list)
    random.shuffle(pd_list)
    print(pd_list)
    pd_str = "".join(pd_list)
    print(pd_str)


#Testing
generate_password(c=3, d=2, s=1)
generate_password(c=3, d=2, s=1)
generate_password(c=3, d=2, s=1)

