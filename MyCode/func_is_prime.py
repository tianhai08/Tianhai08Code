# func_is_prime.py
def func_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(func_is_prime(11))
print(func_is_prime(4))
