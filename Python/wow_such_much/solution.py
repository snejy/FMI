DOGE_WORDS = ['wow', 'lol', 'so', 'such', 'much', 'very']

def wow_such_much(start, end):
    result = []
    for number in range(start, end):
        if number % 15 == 0:
            result.append('suchmuch')
        elif number % 3 == 0:
            result.append('such')
        elif number % 5 == 0:
            result.append('much')
        else:
            result.append(str(number))
    return result

def count_doge_words(string):
    return len([x for x in string.split() if x in DOGE_WORDS])