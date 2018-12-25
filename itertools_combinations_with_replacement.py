from itertools import combinations_with_replacement

if __name__ == '__main__':
    a, b = input().split()
    a, b = sorted(a), int(b)

    for j in combinations_with_replacement(a, b):
        print("".join(j))
