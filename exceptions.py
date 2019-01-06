if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        try:
            a, b = map(int, input().split())
        except Exception as e:
            print("Error code: ", e)
            continue

        try:
            print(int(a/b))
        except Exception as e:
            print("Error code: integer division or modulo by zero")