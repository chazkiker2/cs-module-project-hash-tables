# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from collections import Counter


def caesar_cipher():
    most_freq_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                         'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    with open("./ciphertext.txt", "r") as file_output:
        read_output = file_output.read()
        letters = [letter for letter in read_output]
        letter_freq_dict = {}

        for letter in letters:
            if letter not in most_freq_letters:
                continue

            if not letter_freq_dict.get(letter):
                letter_freq_dict[letter] = 0

            letter_freq_dict[letter] += 1

        ordered_freq = [letter for letter in letter_freq_dict]

        def sorter(letter):
            return letter_freq_dict[letter]

        # https://docs.python.org/3/howto/sorting.html FOR FUN!
        ordered_freq.sort(key=sorter, reverse=True)

        story = ""
        for letter in letters:
            if letter not in ordered_freq:
                story += letter
                continue
            index = ordered_freq.index(letter)
            new_letter = most_freq_letters[index]
            story += new_letter

        return story


def caesar_cipher_new():
    most_freq_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                         'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    with open("./ciphertext.txt", "r") as file_output:
        all_letters = [letter for letter in file_output.read()]
        alpha_count = Counter([letter for letter in all_letters if letter in most_freq_letters])
        alphas_by_freq = [letter for (letter, count) in alpha_count.most_common()]

        story = ""
        for letter in all_letters:
            if letter not in alphas_by_freq:
                story += letter
            else:
                story += most_freq_letters[alphas_by_freq.index(letter)]

        return story


# print(caesar_cipher())
# print(caesar_cipher_new())
# print(caesar_cipher() == caesar_cipher_new())
