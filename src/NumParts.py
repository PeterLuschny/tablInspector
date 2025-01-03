from Partition import partition

"""Partition numbers A000041

[1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101]
"""

# #@


def part_num(n: int) -> int:
    return sum(partition(n))


if __name__ == "__main__":

    from functools import cache

    @cache
    def sigma(n: int) -> int:
        return sum(d for d in range(n, 0, -1) if n % d == 0)

    @cache
    def PartNum(n: int) -> int:
        if n == 0:
            return 1
        return sum(sigma(j) * PartNum(n - j) for j in range(1, n + 1)) // n

    @cache
    def A000041(n: int) -> int:
        if n == 0: return 1
        s = 0; j = n - 1; k = 2
        while 0 <= j:
            t = A000041(j)
            s  = s + t if (k//2) & 1 else s - t
            j -= k     if (k)    & 1 else k // 2
            k += 1
        return s


    from timeit import default_timer as timer

    print([part_num(n) for n in range(14)])

    start = timer()
    [part_num(n) for n in range(1000)]
    end = timer()
    print(end - start)

    print([PartNum(n) for n in range(14)])

    start = timer()
    [PartNum(n) for n in range(1000)]
    end = timer()
    print(end - start)

    print([A000041(n) for n in range(14)])

    start = timer()
    [A000041(n) for n in range(1000)]
    end = timer()
    print(end - start)
