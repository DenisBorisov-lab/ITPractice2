from math import *

def encode(file_name: str):
    text = read_file(file_name)
    count_words(text)


def read_file(file_name: str):
    file = open(file_name, 'r')
    return list(file.read())


def count_words(text):
    global variations
    dictionary = {}
    amount = 0
    for letter in text:
        amount += 1
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    keys = dictionary.keys()
    lenght = len(keys)
    for key in keys:
        dictionary[key] /= amount

    sorted_array = []
    sorted_letter_array = []
    while len(sorted_letter_array) != lenght:

        max_value = -1
        max_letter = ""
        for key in keys:
            if dictionary[key] > max_value:
                max_letter = key
                max_value = dictionary[key]
        sorted_letter_array.append(max_letter)
        sorted_array.append(max_value)
        dictionary.pop(max_letter, max_value)
        keys = dictionary.keys()
        variations = []
    for integer in sorted_array:
        variations.append(abs(floor(log(integer, 2))))
    summary = []
    for i in range(len(sorted_array)):
        n = 0
        for j in range(0, i):
            n += sorted_array[j]
        summary.append(n)
    print(summary)


