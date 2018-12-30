from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    od = OrderedDict()
    for i in range(n):
        data = input().split()
        item, price = " ".join(data[:-1]), int(data[-1])
        od[item] = od[item] + price if item in od else price

    for i in od:
        print(i, od[i])
