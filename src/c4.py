# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
import math


def is_prime(n: int) -> bool:
    for i in range(n, 2):
        if n % i == 0:
            return False
    return True


# The code is not mine, was posted by @sven-marnach. The original post: check-input-that-belong-to-fibonacci-numbers-in-python
def is_fib(n: int) -> bool:
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n


def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False


def format_string_prime_fib_even(n: int) -> str:
    return f"{n} is{' not' if not is_prime(n) else ''} prime, " \
           f"is{' not' if not is_fib(n) else ''} fibonacci " \
           f"and is {'even' if is_even(n) else 'odd'}"


def main() -> None:
    print(format_string_prime_fib_even(2))
    print(format_string_prime_fib_even(7))


if __name__ == '__main__':
    main()
