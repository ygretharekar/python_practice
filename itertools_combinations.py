from itertools import combinations

if __name__ == '__main__':
    a, b = input().split()
    a, b = sorted(a), int(b)

    for i in range(1, b + 1):
        for j in combinations(a, i):
            print("".join(j))
