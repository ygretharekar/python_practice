
def find_intersection(eng1, fre1):
    return eng1 & fre1


if __name__ == '__main__':
    n = input()
    eng = set(map(int, input().split()))
    d = input()
    fre = set(map(int, input().split()))
    print(len(find_intersection(eng, fre)))
