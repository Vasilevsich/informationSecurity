import sha_constants


def string_to_binary(string: str) -> str:
    output = ''
    for symbol in string:
        output += bin(ord(symbol))[2:].zfill(8)
    return output


def add_len(input_string: str, input_length: int) -> str:
    binary_length = bin(input_length)[2:].zfill(64)
    return input_string + binary_length


def format_input(input_string: str):
    LIMIT = 512 - 64
    input_string = string_to_binary(input_string)
    input_length = len(input_string)
    input_string += '1'
    while len(input_string) < LIMIT:
        input_string += '0'
    return add_len(input_string, input_length)


def create_message_schedule(message):
    message_schedule = []
    RECORD_LENGTH = 32
    for i in range(0, len(message), RECORD_LENGTH):
        message_schedule.append(message[i:i + RECORD_LENGTH])
    for i in range(48):
        word = ''
        for j in range(32):
            word += '0'
        message_schedule.append(word)
    return message_schedule


def change_indexes(message_schedule):
    for i in range(16, 64):
        tmp_1 = message_schedule[i - 15][-7:] + message_schedule[i - 15][:-7]
        tmp_2 = message_schedule[i - 15][-18:] + message_schedule[i - 15][:-18]
        tmp_3 = '000' + message_schedule[i - 15][:-3]
        s_0 = bin(int(tmp_1, 2) ^ int(tmp_2, 2) ^ int(tmp_3, 2))[2:]

        tmp_1 = message_schedule[i - 2][-17:] + message_schedule[i - 2][:-17]
        tmp_2 = message_schedule[i - 2][-19:] + message_schedule[i - 2][:-19]
        tmp_3 = '0' * 10 + message_schedule[i - 2][:-10]
        s_1 = bin(int(tmp_1, 2) ^ int(tmp_2, 2) ^ int(tmp_3, 2))[2:]

        res = int(message_schedule[i - 16], 2) + int(s_0, 2) + int(message_schedule[i - 7], 2) + int(s_1, 2)
        res %= 2 ** 32
        res = bin(res)[2:].zfill(32)

        message_schedule[i] = res
    return message_schedule


def compress(words):
    a = bin(sha_constants.h0)[2:].zfill(32)
    b = bin(sha_constants.h1)[2:].zfill(32)
    c = bin(sha_constants.h2)[2:].zfill(32)
    d = bin(sha_constants.h3)[2:].zfill(32)
    e = bin(sha_constants.h4)[2:].zfill(32)
    f = bin(sha_constants.h5)[2:].zfill(32)
    g = bin(sha_constants.h6)[2:].zfill(32)
    h = bin(sha_constants.h7)[2:].zfill(32)

    for i in range(64):
        # print(i)
        tmp_1 = e[-6:] + e[:-6]
        tmp_2 = e[-11:] + e[:-11]
        tmp_3 = e[-25:] + e[:-25]
        s_1 = bin(int(tmp_1, 2) ^ int(tmp_2, 2) ^ int(tmp_3, 2))[2:]
        ch = bin((int(e, 2) & int(f, 2)) ^ (~int(e, 2) & int(g, 2)))[2:]
        temp1 = int(h, 2) + int(s_1, 2) + int(ch, 2) + sha_constants.k[i] + int(words[i], 2)
        temp1 %= 2 ** 32

        tmp_1 = a[-2:] + a[:-2]
        tmp_2 = a[-13:] + a[:-13]
        tmp_3 = a[-22:] + a[:-22]
        s_0 = bin(int(tmp_1, 2) ^ int(tmp_2, 2) ^ int(tmp_3, 2))[2:]
        maj = bin((int(a, 2) & int(b, 2)) ^ (int(a, 2) & int(c, 2)) ^ (int(b, 2) & int(c, 2)))[2:]
        temp2 = int(s_0, 2) + int(maj, 2)
        temp2 %= 2 ** 32

        h = g
        g = f
        f = e
        e = int(d, 2) + temp1
        e %= 2 ** 32
        e = bin(e)[2:].zfill(32)

        d = c
        c = b
        b = a
        a = temp1 + temp2
        a %= 2 ** 32
        a = bin(a)[2:].zfill(32)

    # print(f'a: {hex(int(a,2))}, b: {hex(int(b,2))}, c: {hex(int(c,2))}, d: {hex(int(d,2))}, e: {hex(int(e,2))}, f: {hex(int(f,2))}, g: {hex(int(g,2))}, h: {hex(int(h,2))}')
    h0 = hex((sha_constants.h0 + int(a, 2)) % 2 ** 32)[2:]
    h1 = hex((sha_constants.h1 + int(b, 2)) % 2 ** 32)[2:]
    h2 = hex((sha_constants.h2 + int(c, 2)) % 2 ** 32)[2:]
    h3 = hex((sha_constants.h3 + int(d, 2)) % 2 ** 32)[2:]
    h4 = hex((sha_constants.h4 + int(e, 2)) % 2 ** 32)[2:]
    h5 = hex((sha_constants.h5 + int(f, 2)) % 2 ** 32)[2:]
    h6 = hex((sha_constants.h6 + int(g, 2)) % 2 ** 32)[2:]
    h7 = hex((sha_constants.h7 + int(h, 2)) % 2 ** 32)[2:]

    return h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7


def sha_256(message):
    formatted_message = format_input(message)
    schedule = create_message_schedule(formatted_message)
    changed_indexes = change_indexes(schedule)
    return compress(changed_indexes)
