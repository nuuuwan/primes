class Integer:
    def __init__(self, i: int):
        self.i = i

    @property
    def is_prime(self):
        if self.i <= 1:
            return False
        d = 2
        while True:
            if d * d > self.i:
                break
            if self.i % d == 0:
                return False
            d += 1
        return True


if __name__ == '__main__':
    for i in range(0, 100):
        if Integer(i).is_prime:
            print(i)
