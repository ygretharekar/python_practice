def main(string, k):
    for ss in zip(*[iter(string)] * k):
        d = {}
        print(''.join(d.setdefault(c, c) for c in ss if c not in d))

if __name__ == '__main__':
    string, k = input(), int(input())
    main(string, k)