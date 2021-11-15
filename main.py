import sha
import mathRelated
import hash_function
import heffner
start_message = 'Приеду завтра в полдень, Гушель Василий Олегович'
print(f'Input message is: {start_message}')
encrypted = heffner.encrypt_heffner(start_message)
encrypted_message = encrypted[0]
key = encrypted[1]
print(f'Encrypted message is: {hex(int(encrypted_message, 2))}.\nKey is: {hex(int(key, 2))}')
decrypted = heffner.decrypt_heffner(encrypted_message, key)
print(f'Decrypted message is: {decrypted}')
hash_list = []
for i in range(1, 1000):
    print(f'Hash-function argument is: {str(i)}')
    print('Hash is: ', hex(hash_function.hash_function(str(i))))
    hash_list.append(hash_function.hash_function(str(i)))
print('Len of hash list: ', len(hash_list))
print('Len of hash set: ', len(set(hash_list)))

print(f"Hash-function with argument 'Привет': {hex(hash_function.hash_function('Привет'))}")
print(f"Hash-function with argument 'hello world':{hex(hash_function.hash_function('hello world'))}")
