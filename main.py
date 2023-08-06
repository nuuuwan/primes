

def is_prime(x: int) -> bool:
    """Returns True if x is prime."""
    if x < 2:
        return False
    x2 = int(x**0.5) + 1
    for i in range(2, x2):
        if x % i == 0:
            return False
    return True


def get_y(k):
    s_list = []
    for i in range(1, k + 1):
        s = str((i + 1) % 2)
        s_list.append(s)
    # s_list += reversed(s_list[:-1])
    return int(''.join(s_list))


if __name__ == '__main__':
    for k in range(1, 1000):
        y = get_y(k)
        prime_str = '🔴' if is_prime(y) else " "
        print(f"{prime_str} {y}")
