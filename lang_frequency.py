import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding="utf8") as file:
        data = file.read()
    return data


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    number_of_most_frequent_words = 10
    return Counter(words).most_common(number_of_most_frequent_words)


def print_the_words(words_frequency):
    print('The most frequent words in the text are:')
    for key, value in words_frequency:
        print(key, value)


if __name__ == '__main__':
    filepath = sys.argv[1]
    text = load_data(filepath)
    words_frequency = get_most_frequent_words(text)
    print_the_words(words_frequency)
