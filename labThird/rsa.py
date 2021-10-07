import mathRelated
import receiver
import sender

r = receiver.Receiver(mathRelated.generate_random_prime(1000, 2000), mathRelated.generate_random_prime(1000, 2000))
s = sender.Sender(r.public_key)
message = s.encrypt_message('Hello World')
print(f'Encrypted string: {message}')
print(f'Decrypted message: {r.decrypt_message(message)}')
