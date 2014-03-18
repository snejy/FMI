def is_perfect(number):
    return sum(filter(lambda x: number % x == 0, range(1, number))) == number
