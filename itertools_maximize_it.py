from itertools import product

if __name__ == '__main__':
    k, m = input().split()
    k, m = int(k), int(m)
    arr = []
    for i in range(k):
        a = list(map(int, input().split()))
        a = a[1:]
        arr.append(a)

    max_sum = 0

    for l in product(*arr):
        s = sum([x**2 for x in l])%m
        max_sum = s if s > max_sum else max_sum

    print(max_sum)
