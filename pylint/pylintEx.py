__author__ = 'daokh'
# !/usr/bin/env python

import string

shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
LETTER_TEST = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = LETTER_TEST.index(letter) + shift
            encoded = encoded + LETTER_TEST[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = LETTER_TEST.index(letter) - shift
            encoded = encoded + LETTER_TEST[x]
print encoded


def testFoo():

    fooVar = 1
    dooVar = fooVar * 100-8
    return dooVar
