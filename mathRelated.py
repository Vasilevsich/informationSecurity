import math
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
    for i in range(10):
        flag = False
        a = random.randint(2, source_number - 1)
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


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def generate_open_exponent(f: int) -> int:
    while True:
        open_exponent = generate_random_prime(2, f - 1)
        if math.gcd(f, open_exponent) == 1:
            return open_exponent


# For safe primes
def calculate_primitive_root(modulo: int):
    #print('Calculating primitive root')
    prime_multipliers_set = set(factorize_number(modulo-1))

    for g in range(1, modulo):
        for m in prime_multipliers_set:
            if g ** ((modulo - 1) / m) % modulo == 1:
                break
            return g


def generate_safe_prime(left_border: int, right_border: int) -> int:
    while True:
        q = generate_random_prime(left_border, right_border)
        n = 2 * q + 1
        if miller_rabin(n):
            return n


# Pollard algorithm
def calculate_multiplier(number: int):
    x = [random.randint(2, 20)]
    while True:
        x.append((x[-1] ** 2 - 1) % number)
        for j in range(len(x) - 1):
            gcd = math.gcd(number, abs(x[-1] - x[j]))
            if gcd != 1:
                return gcd


def factorize_number(number: int):
    multipliers = []
    buf = number
    while not miller_rabin(buf):
        multiplier = calculate_multiplier(buf)
        multipliers.append(multiplier)
        buf = int(buf / multiplier)
    multipliers.append(buf)
    flag = True
    while flag:
        for multiplier in multipliers:
            if not miller_rabin(multiplier) and multiplier > 2:
                flag = True
                print('Non prime multiplier: ', multiplier)
                multipliers.remove(multiplier)
                buf = []
                while not miller_rabin(multiplier) and multiplier > 2:
                    tmp_multiplier = calculate_multiplier(multiplier)
                    while tmp_multiplier == multiplier:
                        tmp_multiplier = calculate_multiplier(multiplier)
                    print('tmp multiplier:', tmp_multiplier)
                    buf.append(tmp_multiplier)
                    multiplier = int(multiplier/tmp_multiplier)
                    print('multiplier: ', multiplier)
                buf.append(multiplier)
                multipliers += buf
            flag = False
            for m in multipliers:
                if not miller_rabin(m) and m > 2:
                    flag = True
    return sorted(multipliers)

def modular_pow(base, index_n, modulus):
    c = 1
    for i in range(1, index_n):
        print(i)
        c = (c * base) % modulus
    return c