''' BerSu Ball Problem '''


def main():
    n = int(input())
    boys = [int(x) for x in input().split()]
    m = int(input())
    girls = [int(x) for x in input().split()]

    boys.sort()
    girls.sort()

    count = 0
    for i in range(len(boys)):
        for j in range(len(girls)):
            if (abs(boys[i] - girls[j])) <= 1:
                count += 1
                girls[j] = 1000
                break

    print(count)


if __name__ == '__main__':
    main()
