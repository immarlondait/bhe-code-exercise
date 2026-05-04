import math

class Sieve:

    def __init__(self) -> None:
        pass

    @staticmethod
    def find_upper_limit(n: int) -> int:
        """
        Applying the Prime Number Theorem for the approximation for the nth prime number nlog(n).
        The approx nlog(n) can fall below the actual prime number, so we add a loglog(n) buffer.
        https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number

        :param n: The 0-indexed Nth target number.
        :return: The approximation of the Prime Number's value,
                 with the attribute of being strictly > actual prime value.
        """
        return int(n * (math.log(n) + math.log(math.log(n))))


    @staticmethod
    def generate_partial_prime_list(limit: int) -> list[int]:
        """
        We generate a partial primes list up to the sqrt(limit) in favor of using less memory for larger amounts of N.

        :param limit: A number > the actual prime number value.
        :return: A list of primes up to the sqrt(limit).
        """
        is_prime = bytearray([1]) * limit

        is_prime[0] = 0
        is_prime[1] = 0

        for i in range(2, int(math.sqrt(limit))):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = 0

        primes = []

        for i in range(2, limit):
            if is_prime[i]:
                primes.append(i)

        return primes

    def nth_prime(self, n: int) -> int:
        """
        Returns the Nth prime number's numerical value.

        :param n: The 0-indexed Nth target number.
        :return: The Nth prime number's value.
        """
        if n < 0:
            return -1

        # Small n catches
        # n < 13 chosen due to find_upper_limit() formula needing a buffer until the 0-indexed 13th prime number
        #   n=12, prime_value=41, upper_limit=40, fails up to here
        #   n=13, prime_value=43, upper_limit=45, succeeds going forward
        if n < 13:
            return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41][n]

        target = n + 1

        upper_limit = self.find_upper_limit(target) # n(log(n) + loglog(n))

        primes_list = self.generate_partial_prime_list(upper_limit)

        # A composite number (n = a x b) will have either factor a or b < sqrt(n)
        # With our upper_limit, we grab the "upper limit" of the small factor number
        # We don't need the higher factor number, as that would be covered by other iterations of the sieve
        small_factor_limit = int(math.sqrt(upper_limit))

        prime_count = 0
        lower_seg_bound = 2
        higher_seg_bound = lower_seg_bound + small_factor_limit

        while lower_seg_bound < upper_limit:

            if higher_seg_bound > upper_limit:
                higher_seg_bound = upper_limit

            is_prime = bytearray([1]) * (higher_seg_bound - lower_seg_bound)
            # is_prime = [1] * (higher_seg_bound - lower_seg_bound) # Debugger purposes

            for prime in primes_list:
                if prime*prime > higher_seg_bound:
                    break
                start = max(prime * prime, math.ceil(lower_seg_bound/prime) * prime)
                for j in range(start, higher_seg_bound, prime):
                    is_prime[j-lower_seg_bound] = 0

            for i in range(lower_seg_bound, higher_seg_bound):
                if is_prime[i - lower_seg_bound]:
                    if prime_count == n:
                        return i
                    prime_count += 1

            lower_seg_bound = higher_seg_bound
            higher_seg_bound += small_factor_limit

        return -1

