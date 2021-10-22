import random
import string
import sha

class Client:
    def __init__(self, n: int, g: int, username: str, password: str):
        self.username = username
        self.password = password
        self.N = n
        self.g = g
        self.k = 3

        self.s = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(10, 15)))
        print(f'Salt is: ', self.s)
        self.x = int(sha.sha_256(self.s + self.password), 16)
        self.v = pow(self.g, self.x, self.N)

    def send_reg_message(self):
        return [self.username, self.s, self.v]

    def generate_a(self):
        a = random.randint(1000, 2000)
        A = self.g ** a % self.N
        self.A = A
        self.a = a
        return [self.username, A]

    def generate_client_session_key(self, message):
        if message[0] == 0:
            raise Exception(' B is 0!')
        self.B = message[0]
        u = int(sha.sha_256(hex(self.A)[2:] + hex(self.B)[2:]), 16)

        tmp1 = pow(self.g, self.x, self.N)
        tmp1 *= self.k
        tmp1 = self.B - tmp1

        tmp2 = u * self.x
        s_c = pow(tmp1, self.a + tmp2, self.N)
        self.s_c = s_c
        return s_c

    def generate_m_1(self):
        return sha.sha_256(str(self.A) + str(self.B) + str(self.s_c))
