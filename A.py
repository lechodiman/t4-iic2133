def main():
    arr = []
    n = int(input())
    arr.extend([int(x) for x in input().split()])

    arr.sort()

    output = ""
    for i in range(len(arr) - 1):
        output += str(arr[i]) + " "

    output += str(arr[-1])

    print(output)


if __name__ == "__main__":
    main()
