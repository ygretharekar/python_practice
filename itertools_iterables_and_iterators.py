from itertools import combinations

if __name__ == '__main__':
    n = input()
    arr = [i for i in input().split()]
    k = int(input())
    prob = 0
    for i in combinations(arr, k):
        prob += 'a' in i

    print(prob / len(list(combinations(arr, k))))
