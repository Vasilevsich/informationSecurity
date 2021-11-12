def hash_function(string: str):
    binary_string = ''
    for char in string:
        binary_string += bin(ord(char))[2:].zfill(8)
    source_bin_string = binary_string
    binary_string = bin(len(binary_string) % int(binary_string, 2))[2:]
    while not len(binary_string) % 128 == 0:
        binary_string = '0' + binary_string

    tmp = source_bin_string * (len(binary_string) // len(source_bin_string)) + source_bin_string[:len(binary_string) % len(source_bin_string)]
    tmp = bin(int(tmp, 2) ^ int(binary_string, 2))[2:]
    while len(tmp) < len(binary_string):
        tmp = '0' + tmp
    tmp = tmp[-len(source_bin_string):] + tmp[:-len(source_bin_string)]
    #tmp = pow(int(source_bin_string, 2), int(tmp, 2), 128)
    #print(hex(int(tmp, 2)))
    tmp = pow(int(tmp, 2), 10, int(source_bin_string, 2))
    #print(hex(tmp))
    return tmp
