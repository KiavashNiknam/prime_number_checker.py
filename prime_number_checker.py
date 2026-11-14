
def is_prime(n: int) -> bool:
    """
    Check whether a number is prime.
    """

    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


# Example
print(is_prime(17))  # True
print(is_prime(12))  # False
print(is_prime(2))   # True
