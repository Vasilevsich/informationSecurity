import subscriber


class Cryptanalyst:
    def __init__(self, g: int, p: int, name: str):
        self.g = g
        self.p = p
        self.name = name
        self.key_list = []

    def catch_package(self, sender: subscriber):
        print(f"{self.name} knows, that {sender.name}'s public key is {sender.name[0]} = {self.g}^{sender.name.lower()[0]} mod {self.p} = {sender.package}")
        self.key_list.append([sender.name.lower()[0], sender.package])

    def show_secret_key_equality(self):
        print(f"{self.name} knows that s = {self.key_list[1][1]}^{self.key_list[0][0]} mod {self.p} = {self.key_list[0][1]}^{self.key_list[1][0]} mod {self.p}")