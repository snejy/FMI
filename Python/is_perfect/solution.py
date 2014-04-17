def is_perfect(number):
    return sum(filter(lambda x: number % x == 0, range(1, number))) == number

def main():
    print(is_perfect(6))
    print(is_perfect(10))
    print(is_perfect(1))
    print(is_perfect(-3))
    print(is_perfect(16))
    print(is_perfect(10323228))


if __name__ == '__main__':
    main()