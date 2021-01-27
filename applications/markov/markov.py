import random


def markov(words):
    split_words = words.split()
    # each word (word_key) has value dictionary
    # each dictionary stored under word_key holds key (next_word)
    # word_key.next_word counts the number of times `next_word` follows `word_key`
    word_dict = {}

    for i in range(len(split_words) - 1):
        word = split_words[i].lower().strip('":;,.!?-+=/\\|[]}{()*^&')
        next_word = split_words[i + 1].lower().strip('":;,.!?-+=/\\|[]}{()*^&')
        if not word_dict.get(word):
            word_dict[word] = {}

        if not word_dict[word].get(next_word):
            word_dict[word][next_word] = 0

        word_dict[word][next_word] += 1

    for word in word_dict:  # for each word in dict
        next_words = word_dict[word]
        total = 0
        for next_word in next_words:
            count = next_words[next_word]
            total += count

        for next_word_2 in next_words:
            next_words[next_word_2] /= total
            # percentage chance particular word will occur after given word

    return word_dict


with open("input.txt") as f:
    words = f.read()
    chain = markov(words)
    counter = 0

    while counter < 13:
        counter += 1
        sentence = ["the"]
        while len(sentence) < 8:
            rand = random.random()
            word = sentence[-1]
            total = 0
            for next_word in chain[word]:
                total += chain[word][next_word]
                if total > rand:
                    sentence.append(next_word)
                    break
        print(" ".join(sentence))
