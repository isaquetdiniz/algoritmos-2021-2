import sys


def main():
    largest = ''
    length = -1

    for line in sys.stdin:
        line = line[:-1]
        qnt = line.count(",")

        if line != '[]':
            qnt += 1

        if qnt > length:
            largest = line
            length = qnt

    print(largest)


if __name__ == '__main__':
    main()
