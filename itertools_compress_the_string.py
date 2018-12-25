from itertools import groupby

if __name__ == '__main__':
    a = input()
    print(*[(len(list(c)), int(k)) for k, c in groupby(a)])
