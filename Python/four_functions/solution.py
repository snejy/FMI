import collections

ALPHABET = 'абвгдежзийклмнопрстуфхцчшщьюяъ'


def is_pangram(phrase):
    return len(set([x for x in list(phrase.lower()) if x in ALPHABET])) == 30


def char_histogram(sentence):
    return collections.Counter(list(sentence))


def sort_by(function, arguments):
    for i in range(len(arguments)-1):
        for i in range(len(arguments)-1):
            if function(arguments[i], arguments[i+1]) > 0:
                arguments[i], arguments[i+1] = arguments[i+1], arguments[i]
    return arguments


def group_by_type(dictionary):
    grouped_items = collections.defaultdict(dict)
    for key, value in dictionary.items():
        grouped_items[type(key)][key] = value
    return grouped_items


def anagrams(words):
    anagrams = collections.defaultdict(list)
    for word in words:
        without_signs = filter(lambda x: x.isalpha(), word.lower())
        anagrams[tuple(sorted(without_signs))].append(word)
    return list(anagrams.values())