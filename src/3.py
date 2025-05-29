memo = {0: 1, 1: 3}

def f(n):
    if n in memo:
        return memo[n]
    memo[n] = 5 * f(n - 1) + f(n - 2)
    return memo[n]


def main():
    A = []
    n = 0
    while len(A) < 40:
        value = f(n)
        if value % 2 != 0:
            A.append(value)
        n += 1
    print(f"A[39] = {A[39]}")

if __name__ == '__main__':
    main()