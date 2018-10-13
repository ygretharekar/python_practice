def main():
    n = int(input())
    integer_list = [i for i in input().split()]
    tup = tuple(int(i) for i in integer_list)
    print(hash(tup))

if __name__ == '__main__':
    main()