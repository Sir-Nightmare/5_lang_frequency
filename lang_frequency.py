import re
from collections import Counter


def load_data(filepath):
    data = ""
    with open(filepath, 'r', encoding="utf8") as file:
        data = file.read()
    return data


def get_most_frequent_words(text):
    words = re.findall(r'\w+', data.lower())
    ten_words = Counter(words).most_common(10)
    print('Ten the most popular words in the text')
    for key, value in ten_words:
        print(key, value)


if __name__ == '__main__':
    # data = load_data('text.txt')
    data = load_data(input('Type the path to text file'))
    get_most_frequent_words(data)
