from collections import Counter

if __name__ == '__main__':
    name = sorted(input().strip())
    most_common = Counter(name).most_common()

    most_common = sorted(most_common, key=lambda x: (x[1] * -1, x[0]))

    for i in range(3):
        print(most_common[i][0], most_common[i][1])
