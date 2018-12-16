from cmath import phase

if __name__ == '__main__':
    # st = input().split('+')
    # x = int(st[0])
    # y = int(st[1][:-1])
    c_no = complex(input())
    print(abs(c_no))
    print(phase(c_no))
