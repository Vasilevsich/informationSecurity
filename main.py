import sha
import mathRelated
import hash_function

# print(sha.sha_256('hello world'))
# print(mathRelated.factorize_number(1000000))
# print(mathRelated.calculate_primitive_root(1000))
print(hash_function.hash_function('q'))
for i in  range(1, 101):
    print(str(i))
    hash_function.hash_function(str(i))

"""for i in 'abcdefghijklmnopqrstuvwxyz':
    print(i)
    hash_function.hash_function(i)"""
