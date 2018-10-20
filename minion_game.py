def main():
    st = input()
    stu_score = 0
    kev_score = 0
    for i in range(len(st)):
        if st[i] in "AEIOU":
            kev_score += len(st) - i
        else:
            stu_score += len(st) - i

    if stu_score == kev_score:
        print('Draw')
    elif stu_score > kev_score:
        print(f'Stuart {stu_score}')
    else:
        print(f'Kevin {kev_score}')

if __name__ == '__main__':
    main()