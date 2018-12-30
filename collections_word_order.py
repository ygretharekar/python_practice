from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    wordLog = OrderedDict()

    for i in range(n):
        word = input()
        wordLog[word] = wordLog[word] + 1 if word in wordLog else 1

    print(len(wordLog))
    for word in wordLog:
        print(wordLog[word], end=" ")
    print()
