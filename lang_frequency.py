import re
from collections import Counter
import sys


def load_text_file(filepath):
    with open(filepath, 'r', encoding="utf8") as file:
        text_string = file.read()
    return text_string


def get_most_frequent_words(text):
    word_list = re.findall(r'\w+', text.lower())
    number_of_most_frequent_words = 10
    return Counter(word_list).most_common(number_of_most_frequent_words)


def print_the_words(words_frequency):
    print('The most frequent words in the text are:')
    for word, word_quantity in words_frequency:
        print(word, word_quantity)


if __name__ == '__main__':
    filepath = sys.argv[1]
    words_frequency = get_most_frequent_words(load_text_file(filepath))
    print_the_words(words_frequency)
