from collections import deque

if __name__ == '__main__':
    n = int(input())
    dq = deque()
    for i in range(n):
        command = input().split()
        # i_val = int(val) if val else ''
        eval('dq.{0}({1})'.format(*command + ['']))

    print(*dq)
