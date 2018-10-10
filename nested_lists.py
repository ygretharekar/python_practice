def main():
    arr = [[input(), float(input())] for _ in range(int(input()))]
    arr.sort(key = lambda x: x[0])
    arr.sort(key = lambda x: x[1], reverse = True)

    l = [v for n, v in arr ]
    l = list(set(l))
    l.sort()

    for name, score in arr:
        if score == l[1]:
            print(name)

if __name__ == '__main__':
    main()