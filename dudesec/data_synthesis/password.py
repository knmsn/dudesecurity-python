from random import choice
import string


def generator_password(size):
    password = ""

    values = string.ascii_letters + string.digits + '@#&$'

    for i in range(size):
        password += choice(values)

    print(password)
    return password