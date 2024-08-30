# func_py_find_twin_primes.py
def func_py_find_twin_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    twin_primes = [(n, n+2) for n in range(2, limit) if is_prime(n) and is_prime(n+2)]
    return twin_primes

print(func_py_find_twin_primes(100))
