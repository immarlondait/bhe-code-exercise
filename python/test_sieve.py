import unittest
from python.sieve import Sieve

class SieveTest(unittest.TestCase):

    def test_sieve_nth_prime(self) -> None:
        sieve = Sieve()

        # print("Starting here!")
        # print("0th prime, ", f"{sieve.nth_prime(0):_}")
        # print("19th prime, ", f"{sieve.nth_prime(19):_}")
        # print("99th prime, ", f"{sieve.nth_prime(99):_}")
        # print("500th prime, ", f"{sieve.nth_prime(500):_}")
        # print("986th prime, ", f"{sieve.nth_prime(986):_}")
        # print("2_000th prime, ", f"{sieve.nth_prime(2_000):_}")
        # print("1_000_000th prime, ", f"{sieve.nth_prime(1_000_000):_}")
        # print("10_000_000th prime, ", f"{sieve.nth_prime(10_000_000):_}")
        # print("10_000_000th prime, ", f"{sieve.nth_prime(100_000_000):_}")


        self.assertEqual(2, sieve.nth_prime(0))
        self.assertEqual(71, sieve.nth_prime(19))
        self.assertEqual(541, sieve.nth_prime(99))
        self.assertEqual(3_581, sieve.nth_prime(500))
        self.assertEqual(7_793, sieve.nth_prime(986))
        self.assertEqual(17_393, sieve.nth_prime(2_000))
        # self.assertEqual(15_485_867, sieve.nth_prime(1_000_000)) # TODO
        # self.assertEqual(179_424_691, sieve.nth_prime(10_000_000)) # TODO
        # self.assertEqual(2_038_074_751, sieve.nth_prime(100_000_000)) # TODO


    def test_sieve_fuzz_nth_prime(self) -> None:
        sieve = Sieve()
        fuzz_max = 200

        self.assertEqual(-1, sieve.nth_prime(-1))

        # TODO make a loop to generate random ints up to fuzz_max

