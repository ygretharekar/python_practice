from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Row = namedtuple('Row', list(input().split()))
    total_marks = 0

    for i in range(n):
        r = Row(*list(input().split()))
        total_marks += int(r.MARKS)

    print(total_marks / n)
