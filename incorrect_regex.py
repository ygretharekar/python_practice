import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        reg = True
        try:
            re.compile(input())
        except re.error:
            reg = False

        print(reg)
