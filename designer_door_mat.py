def main(n, m):
    pattern = [('.|.'*(i*2 + 1)).center(m, '-') for i in range(n//2)]
    welcome = ['WELCOME'.center(m, '-')]
    print('\n'.join(pattern + welcome + pattern[::-1]))

if __name__ == '__main__':
    [n, m] = input().split()
    main(int(n), int(m))