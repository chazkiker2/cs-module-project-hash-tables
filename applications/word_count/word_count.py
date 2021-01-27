from collections import Counter
import re


def word_count(s):
    split_s = s.lower().strip('":;,.!?-+=/\\|[]}{()*^&').split()
    word_dict = {}
    for out_word in split_s:
        word = re.sub('[^a-zA-Z]', '', out_word)
        if not word_dict.get(word):
            word_dict[word] = 0

        word_dict[word] += 1

    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test, of the emergency broadcast network. This is only a test.'))
