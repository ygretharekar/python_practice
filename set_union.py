if __name__ == '__main__':
    n1 = int(input())
    eng = set(map(int, input().split()))
    n2 = int(input())
    fre = set(map(int, input().split()))

    print(len(eng.union(fre)))
