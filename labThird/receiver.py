import mathRelated


class Receiver:
    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q
        print(f'P is {self.p}, Q is {self.q}')
        self.module = self.p * self.q
        print(f'Module is {self.module}')
        self.f = mathRelated.euler_function(self.p, self.q)
        print(f'Euler function is {self.f}')
        self.e = mathRelated.generate_open_exponent(self.f)
        self.public_key = [self.e, self.module]
        self.private_key = [self.correct_secret_key(list(self.generate_secret_key(self.e, self.f))[1]), self.module]
        print(f'public key is {self.public_key}, private key is {self.private_key}')

    def decrypt_message(self, encrypted_text) -> str:
        output = ''
        for character in encrypted_text:
            print(f'Current encrypted character: {character}')
            # output += chr(character ** self.private_key[0] % self.private_key[1])
            output += chr(pow(character, self.private_key[0], self.private_key[1]))
        return output

    def generate_secret_key(self, a: int, b: int):
        if a == 0:
            return b, 0, 1
        gcd, xn, yn = self.generate_secret_key(b % a, a)

        x = yn - (b // a) * xn
        y = xn

        return gcd, x, y

    def correct_secret_key(self, secret_key: int) -> int:
        if secret_key >= 0:
            return secret_key
        return self.f+secret_key
