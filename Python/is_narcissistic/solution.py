def is_narcissistic(number, base=10):
  return int(number, base) == sum(list_of_powered_digits(number, base))

def list_of_powered_digits(number,base):
    convert_number = list(map(lambda x: int(x, base), list(number)))
    return list(map(lambda x: x**len(number), convert_number))
