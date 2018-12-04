''' Misha and Changing Handles'''


def main():
    usedMap = {}
    wordMap = {}

    q = int(input())

    while (q > 0):
        old, new = (x for x in input().split())

        if old not in usedMap:
            usedMap[old] = old
            usedMap[new] = old
            wordMap[old] = new
        else:
            usedMap[new] = usedMap[old]
            wordMap[usedMap[old]] = new

        q -= 1

    count = len(wordMap)
    print(count)

    for first, second in wordMap.items():
        print(first, second)


if __name__ == '__main__':
    main()
