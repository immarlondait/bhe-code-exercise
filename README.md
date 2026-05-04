# BHE Software Engineer Coding Exercise

## The Sieve of Eratosthenes

Using **Python**, this project implements a Sieve of Eratosthenes to compute the **Nth prime number** using a segmented sieve and memory optimizations.

### O(n) 
* ~O(nloglog(n))

### Approach
1. Segmented Sieve - We generate an initial partial list of Primes to start with and utilize a segmented sieve in favor of memory usage and scalability.
2. bytearray Optimization - a `bytearray` is used instead of a boolean list for efficient memory usage.
3. Approximation Of Nth Prime - We utilize n(log(n) + loglog(n)) to have the attribute of being > the actual target Prime Number's value.

### Testing Strategy

* Unit Tests
  * Known prime values
  * Edge cases
  * Boundary cases
  * Data-driven Testing
* Fuzz Testing
  * Random values of `n`

### Design decisions
* Used segmented sieve to handle large values more efficiently
* used bytearray for memory optimization
* Used brute-force and filepath for fuzz testing validation

### Future optimizations
* Adjust for odds-only indexing
* Static segment size

### Requirements
* Python 3.11+
* Docker (optional)

### Run tests with Docker

* **Build image**: docker build -t sieve-tests .

* **Run tests**: docker run --rm sieve-tests