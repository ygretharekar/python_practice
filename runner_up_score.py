def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort(reverse = True)
    print(arr[1])

if __name__ == '__main__':
    main()