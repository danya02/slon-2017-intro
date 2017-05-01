#!/usr/bin/python3
import re
# Simple statistical analyser of text
# Is defined by means of functions that can be used elsewhere.
# When run, takes input from file called `text.txt` and outputs to stdout.


def split_by_sentences(text):
    text = re.split("[].!?\n]", text)  # Split text by sentences
    text = list(filter(lambda i: i != '', text))  # Remove empty strings
    return text


def split_by_words(text):
    for i in [',', ';', ':', '—', "'"]:
        text.replace(i, "")
    return text.split()


def get_longest_sentences(text, n):
    assert(isinstance(text, str))
    text = split_by_sentences(text)
    text = [split_by_words(i) for i in text]
    text = sorted(text, key=len)
    return reversed(text[-n:])


def get_average_length_of_sentence(text):
    assert(isinstance(text, str))
    text = split_by_sentences(text)
    text = [split_by_words(i) for i in text]
    total_len = 0
    for i in text:
        total_len += len(i)
    avg_len = float(total_len)/float(len(text))
    return avg_len

if __name__ == '__main__':
    with open("text.txt") as o:
        text = o.read()
    print("The longest sentences are:")
    for i, j in zip(get_longest_sentences(text, 3), range(3)):
        print(j+1, ". ", " ".join(i), " (", len(i), " words)", sep="")
    print()
    print("The average length of sentence is: ", end="")
    print(get_average_length_of_sentence(text), "words.")
