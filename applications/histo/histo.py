# Your code here
def histogram():
    with open("./robin.txt", "r") as file_output:
        read_file = file_output.read()
        split_words = read_file.split()
        word_dict = {}
        for word in split_words:
            word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')
            if not word_dict.get(word):
                word_dict[word] = []

            word_dict[word].append("#")

        return word_dict


histo = histogram()
for word in histo:
    print("".join(histo[word]), word)
