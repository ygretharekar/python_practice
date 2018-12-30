import sys
from collections import deque

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        dq = deque(map(int, input().split()))

        max_length = sys.maxsize
        ans = 'Yes'

        while len(dq) > 0:
            if len(dq) == 1:
                item = dq.pop()
            else:

                if dq[0] > dq[-1]:
                    item = dq.popleft()
                else:
                    item = dq.pop()

                if max_length < item:
                    ans = 'No'
                else:
                    max_length = item

        print(ans)
