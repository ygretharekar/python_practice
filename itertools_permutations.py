from itertools import permutations

if __name__ == '__main__':
    a, b = input().split()
    b = int(b)

    for i in permutations(sorted(a), b):
        print(''.join(i))
