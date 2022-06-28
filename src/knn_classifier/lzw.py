
import string
from pathlib import Path
from struct import *
import glob
import time
import os

K = 16


def get_dict(size_dic):
    dictionary = {}
    for i in range(size_dic):
        dictionary[chr(i)] = i
    # print(dictionary)
    return dictionary


def lzw_train(train_data):
    size = 256
    k = K
    dictionary = get_dict(size)
    max_size = pow(2, k)
    for img in train_data:
        target_path = Path(img)

        coded_msg = []

        # compress
        file = open(target_path, encoding="latin-1")
        msg = file.read()

        previous = ""

        for i in range(len(msg)):
            current = msg[i] + previous
            if current in dictionary:
                previous = current
            else:
                coded_msg.append(dictionary[previous])
                if len(dictionary) <= max_size:
                    dictionary[current] = size
                    size += 1
                previous = msg[i]
        if previous in dictionary:
            coded_msg.append(dictionary[previous])
        file.close()

    return {"label": train_data[0].split("/")[1], "dictionary": dictionary}


def lzw_test(dictionary, test_sample):
    target = Path(test_sample)
    size = len(dictionary)
    k = K
    max_size = pow(2, k)
    coded_msg = []

    # compress
    file = open(target, encoding="latin-1")
    msg = file.read()

    previous = ""

    for i in range(len(msg)):
        current = msg[i] + previous
        if current in dictionary:
            previous = current
        else:
            coded_msg.append(dictionary[previous])
            previous = msg[i]
    if previous in dictionary:
        coded_msg.append(dictionary[previous])

    file.close()
    return len(coded_msg)


if __name__ == '__main__':
    pass


