import random
import sha


class Server:
    def __init__(self, n: int, g: int):
        self.N = n
        self.g = g
        self.k = 3

        self.users = {}

    def add_user(self, info):
        self.users[info[0]] = info[1:]

    def generate_b(self, message):
        if message[1] == 0:
            raise Exception('A is 0!')
        self.A = message[1]
        b = random.randint(1000, 2000)
        self.b = b
        s_v = self.users[message[0]]
        B = self.k * s_v[1] + self.g ** b % self.N
        self.B = B
        return [B, s_v[0]]

    def generate_server_session_key(self, username):
        u = int(sha.sha_256(hex(self.A)[2:] + hex(self.B)[2:]), 16)
        #s_s = (self.A * self.users[username][1] ** u % self.N) ** self.b % self.N
        s_s = pow(self.A * pow(self.users[username][1], u, self.N), self.b, self.N)
        self.s_s = s_s
        return s_s

    def compare_m_1(self, m_1_key):
        if sha.sha_256(str(self.A) + str(self.B) + str(self.s_s)) == m_1_key:
            print('Connection successful! M1 is right')
        else:
            print('Bad M1! Connection over!')