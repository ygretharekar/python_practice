if __name__ == '__main__':
    n_a = int(input())
    set_a = set(map(int, input().split()))

    for i in range(int(input())):
        op = input().split()[0]
        set_b = set(map(int, input().split()))
        eval('set_a.{0}({1})'.format(op, set_b))

    print(sum(set_a))
