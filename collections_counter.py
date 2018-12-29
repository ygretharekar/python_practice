from collections import Counter

if __name__ == '__main__':
    shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    # print(Counter(shoe_sizes))
    counter_dict = Counter(shoe_sizes)
    n = int(input())
    cust = []
    amount = 0

    for i in range(n):
        size, price = map(int, input().split())
        cust.append((size, price))
        amount += price if counter_dict[size] else 0
        counter_dict[size] = counter_dict[size] - 1 if counter_dict[size] else 0

    print(amount)
