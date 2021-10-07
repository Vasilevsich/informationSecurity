class Sender:
    def __init__(self, public_key: list):
        self.receiver_public_key = public_key

    def encrypt_message(self, text: str):
        output = []
        for character in text:
            output.append(ord(character) ** self.receiver_public_key[0] % self.receiver_public_key[1])
        return output
