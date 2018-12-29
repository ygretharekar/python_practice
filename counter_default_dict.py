from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())

    dd = defaultdict(list)

    for i in range(n):
        dd[input()].append(i + 1)

    for i in range(m):
        c = input()
        if dd[c]:
            print(*dd[c])
        else:
            print(-1)
