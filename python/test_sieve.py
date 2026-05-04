import unittest
import random
from python.sieve import Sieve

class SieveTest(unittest.TestCase):

    def test_sieve_nth_prime(self) -> None:
        sieve = Sieve()

        self.assertEqual(2, sieve.nth_prime(0))
        self.assertEqual(71, sieve.nth_prime(19))
        self.assertEqual(541, sieve.nth_prime(99))
        self.assertEqual(3_581, sieve.nth_prime(500))
        self.assertEqual(7_793, sieve.nth_prime(986))
        self.assertEqual(17_393, sieve.nth_prime(2_000))
        self.assertEqual(15_485_867, sieve.nth_prime(1_000_000)) # 5s 300ms
        self.assertEqual(179_424_691, sieve.nth_prime(10_000_000)) # 1m 7s
        self.assertEqual(2_038_074_751, sieve.nth_prime(100_000_000)) # # 15m 24s

        self.assertEqual(-1, sieve.nth_prime(-1))
        self.assertEqual(61, sieve.nth_prime(17))
        self.assertEqual(113, sieve.nth_prime(29))
        self.assertEqual(7_919, sieve.nth_prime(999))


    def test_sieve_fuzz_nth_prime(self) -> None:
        sieve = Sieve()
        fuzz_min = -100
        fuzz_max = 300
        fuzz_amount = 2_000

        samples = self.random_ints(fuzz_min, fuzz_max, fuzz_amount)

        primes_list = sieve.generate_partial_prime_list(fuzz_max * fuzz_max)

        for n in samples:
            expected = self.brute_force_nth_prime(n)
            if n < 0:
                actual = -1
            else:
                actual = primes_list[n]

            self.assertEqual(expected, actual)


    def test_sieve_boundaries(self) -> None:
        sieve = Sieve()

        boundaries = [10, 11, 12, 13, 14, 19, 20, 21, 22,
                      98, 99, 100, 101, 9_998, 9_999, 10_000,10_001]

        for n in boundaries:
            self.assertEqual(self.brute_force_nth_prime(n), sieve.nth_prime(n))

    def test_from_file(self) -> None:
        sieve = Sieve()

        with open("data/primes.txt", "r") as f:
            file_primes = [int(x) for x in f.read().split(",")]

        for i in range(len(file_primes)):
            expected = file_primes[i]
            actual = sieve.nth_prime(i)
            self.assertEqual(expected, actual)

    @staticmethod
    def random_ints(minimum: int, maximum: int, amount: int):
        return [random.randint(minimum, maximum) for _ in range(amount)]

    @staticmethod
    def brute_force_nth_prime(n: int):
        if n < 0:
            return -1

        primes = []
        num = 2

        while len(primes) <= n:
            is_prime = True

            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

            num += 1

        return primes[len(primes) - 1]