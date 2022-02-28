import sys


def main():
    qnt_right = 0
    qnt_left = 0

    right_char = '}'
    left_char = '{'

    good_formated = 'S'
    bad_formated = 'N'

    for line in sys.stdin:
        line = line[:-1]

        if len(line) == 0:
            print(good_formated)
        else:
            for char in line:
                if char is right_char:
                    qnt_right += 1
                if char is left_char:
                    qnt_left += 1

            if qnt_right == qnt_left:
                print(good_formated)
            else:
                print(bad_formated)


if __name__ == '__main__':
    main()
