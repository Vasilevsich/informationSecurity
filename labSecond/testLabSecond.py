import unittest
import subscriber
import cryptanalyst


class SecondLabTest(unittest.TestCase):
    def setUp(self):
        p = 3500
        g = 27
        print(f'p is {p}, g is {g}. All know that')
        alice = subscriber.Subscriber(g, p, 'Alice')
        bob = subscriber.Subscriber(g, p, 'Bob')
        eve = cryptanalyst.Cryptanalyst(g, p, 'Eve')
        eve.catch_package(alice)
        eve.catch_package(bob)

        alice.calculate_secret_key(bob.package)
        bob.calculate_secret_key(alice.package)
        eve.show_secret_key_equality()

    def test_package(self):
        ...
