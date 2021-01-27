from collections import Counter

def no_dups(s):
    split_s = s.split()
    output = ""
    for word in split_s:
        if output.find(word) == -1:  # if word not in output
            output += f"{word} "

    return output.strip(" ")


def no_dups_better(s):
    split_s = s.split()
    s_counter = Counter(split_s)
    return " ".join(s_counter.keys())


if __name__ == "__main__":
    print(no_dups_better(""))
    print(no_dups_better("hello"))
    print(no_dups_better("hello hello"))
    print(no_dups_better("cats dogs fish cats dogs"))
    print(no_dups_better("spam spam spam eggs spam sausage spam spam and spam"))
