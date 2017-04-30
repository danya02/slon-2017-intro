#!/usr/bin/python3
import sys

# Simple substitution cypher program
# Takes input on stdin, outputs on stdout.

rules = {  # Replacement rules
    "Р": "Л",
    "р": "л",
    "А": "АСА",
    "О": "ОСО",
    "У": "УСУ",
    "Ы": "ЫСЫ",
    "Э": "ЭСЭ",
    "И": "ИСИ",
    "Е": "ЕСЕ",
    "Я": "ЯСЯ",
    "Ю": "ЮСЮ",
    "Ё": "ЁСЁ",
    "а": "аса",
    "о": "осо",
    "у": "усу",
    "ы": "ысы",
    "э": "эсэ",
    "и": "иси",
    "е": "есе",
    "я": "яся",
    "ю": "юсю",
    "ё": "ёсё",
}

while True:                        # for every symbol do:
    char = sys.stdin.read(1)         # get the symbol
    if not char:                     # if it is invalid (i.e. EOF)
        break                          # break the cycle and quit
    if char in rules:                # if there is a substitution available
        sys.stdout.write(rules[char])  # write the replacement
        sys.stdout.flush()             # and make the output unbuffered
    else:                            # if not
        sys.stdout.write(char)         # output the symbol
        sys.stdout.flush()             # and make the output unbuffered
