if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    t = int(input())
    ans = True

    print(all((set_a > set(map(int, input().split()))) for _ in range(t)))
    # for i in range(t):
    #     set_b = set(map(int, input().split()))
    #     ans &= set_b.issuperset(set_a)
    # print(ans)
