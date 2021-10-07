import mathRelated


class Subscriber:
    def __init__(self, g: int, p: int, name: str):
        self.g = g
        self.p = p
        self.name = name
        self.secret_number = mathRelated.generate_random_prime(1000000, 2000000)
        print(f'{self.name} generated secret number {self.secret_number}')
        self.package = self.g**self.secret_number % self.p
        print(f'{self.name} created package {self.package}')

    def calculate_secret_key(self, package: int):
        print(f"{self.name} received package {package}")
        result = package**self.secret_number % self.p
        print(f'{self.name} calculated secret key {result}')
        return result
