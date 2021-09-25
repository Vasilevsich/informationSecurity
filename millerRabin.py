import random


def miller_rabin(number: int):
    if number % 2 == 0:
        return False
    source_number = number
    number -= 1
    s = 0
    while number % 2 == 0:
        number //= 2
        s += 1
    d = number
    # print(f'd is {d}, s is {s}')
    for i in range(5):
        flag = False
        a = random.randint(1, source_number - 1)
        # print(f'a is {a}')
        x = a ** d % source_number
        if x == 1 or x == source_number - 1:
            continue
        for j in range(s):
            x = x ** 2 % source_number
            if x == 1:
                return False
            if x == source_number - 1:
                flag = True
                break
        if not flag:
            return False
    return True


def generate_random_prime(left_border: int, right_border: int) -> int:
    while True:
        number = random.randint(left_border, right_border)
        if miller_rabin(number):
            # print(number)
            return number
