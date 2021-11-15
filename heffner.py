import random
from textwrap import wrap


def encrypt_heffner(message: str):
    binary = ''
    for symbol in message:
        binary += bin(ord(symbol))[2:].zfill(19)
    key = bin(random.getrandbits(len(binary)))[2:]
    result = bin(int(binary, 2) ^ int(key, 2))[2:].zfill(len(binary))
    return [result, key]


def decrypt_heffner(encrypted_message, key):
    tmp = bin(int(encrypted_message, 2) ^ int(key, 2))[2:].zfill(len(encrypted_message))
    tmp = wrap(tmp, 19)
    result = ''
    for t in tmp:
        result += chr(int(t, 2))
    return result
