def main():
    s = input()

    ans = False

    for c in s:
        if c.isalnum():
            ans = True
            break

    print(ans)
    
    ans = False

    for c in s:
        if c.isalpha():
            ans = True
            break

    print(ans)
    
    ans = False

    for c in s:
        if c.isdigit():
            ans = True
            break

    print(ans)
    
    ans = False

    for c in s:
        if c.islower():
            ans = True
            break

    print(ans)
    
    ans = False

    for c in s:
        if c.isupper():
            ans = True
            break

    print(ans)

if __name__ == '__main__':
    main()