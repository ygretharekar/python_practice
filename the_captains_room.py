if __name__ == '__main__':
    num = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)
    print((num * sum(s) - sum(arr)) / (num - 1))
