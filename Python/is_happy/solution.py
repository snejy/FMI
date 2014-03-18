def is_happy(number):
    if number < 10:
        return number == 1 or number == 7
    else:
        return is_happy(sum([x*x for x in number_to_list(number)]))


def number_to_list(number):
    return list(map(int, list(str(number))))


def is_prime(number):
    return len(list(filter(lambda x: number % x == 0, range(1, number)))) == 1


def happy_primes(numbers):
    return [x for x in numbers if is_happy(x) and is_prime(x)]
