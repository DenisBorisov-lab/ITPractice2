from math import *


def encode(file_name: str):
    text = read_file(file_name)
    count_words(file_name, text)


def read_file(file_name: str):
    file = open(file_name, 'r', encoding="utf8", newline='\n')
    return list(file.read())


def get_information(dictionary: dict):
    information = []
    keys = dictionary.keys()
    for key in keys:
        information.append(ord(key).to_bytes(4, "little"))
        information.append(dictionary[key].encode("utf-8"))
        information.append('$$'.encode('utf-8'))
    return information


def to_binary_view(l: int, number: float):
    counter = 0
    result = ""
    while counter != l and number != 0:
        number *= 2
        result += str(int(number))
        number -= int(number)
        counter += 1
    return result


def to_bytes(binary_string: str, file):
    for i in range(0, len(binary_string), 8):
        number = int(binary_string[i:i + 8], 2)
        file.write(number.to_bytes(1, 'little'))


def count_words(file_name: str, text):
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
    length = len(keys)
    for key in keys:
        dictionary[key] /= amount

    sorted_array = []
    sorted_letter_array = []
    while len(sorted_letter_array) != length:

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

    binary_dictionary = {sorted_letter_array[0]: str(summary[0]) * variations[0]}
    for i in range(1, len(summary)):
        binary_dictionary[sorted_letter_array[i]] = to_binary_view(variations[i], summary[i])

    result = ""
    for i in range(len(text)):
        result += binary_dictionary[text[i]]

    if len(result) % 8 != 0:
        result += "0" * (8 - (len(result) % 8))

    end_file = open(file_name[:-4] + ".pumrar", "wb")
    for item in get_information(binary_dictionary):
        end_file.write(item)
    end_file.write("####".encode("utf-8"))
    to_bytes(result, end_file)
    end_file.close()
