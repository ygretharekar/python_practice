def sym_diff(s1, s2):
    uni = s1.union(s2)
    inter = s2.intersection(s1)
    sd = list(uni.difference(inter))
    sd.sort()
    for i in sd:
        print(i)


if __name__ == '__main__':
    n, a1, m, a2 = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
    sym_diff(a1, a2)
