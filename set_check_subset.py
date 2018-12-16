if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        len_a = int(input())
        set_a = set(map(int, input().split()))
        len_b = int(input())
        set_b = set(map(int, input().split()))
        print(set_a >= set_b)
