
import string
from pathlib import Path
from struct import *
import glob
import time
import os


def get_dict(size_dic):
    dictionary = {}
    for i in range(size_dic):
        dictionary[chr(i)] = i
    # print(dictionary)
    return dictionary


def lzw_train(train_data):
    size = 256
    k = 16
    dictionary = get_dict(size)
    max_size = pow(2, k)
    for img in train_data:
        target_path = Path(img)

        coded_msg = []

        # compress
        file = open(target_path, encoding="latin-1")
        msg = file.read()

        previous = ""

        print("compressing...")
        start = time.time()
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
        end = time.time()
        print("compressed in ", round(end - start, 2), " s")
        file.close()

    return {"label": train_data[0].split("/")[1], "dictionary": dictionary}


def lzw_test(dictionary, test_sample):
    target = Path(test_sample)
    size = len(dictionary)
    k = 16
    max_size = pow(2, k)
    coded_msg = []

    # compress
    file = open(target, encoding="latin-1")
    msg = file.read()

    previous = ""

    print("compressing...")
    start = time.time()
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
    end = time.time()
    print("compressed in ", round(end - start, 2), " s")

    file.close()
    return len(coded_msg)


if __name__ == '__main__':
    pass
    # filepath = "/home/matheusmelo/Documentos/Old/Documentos/Projetos/projeto_iti/iti-project/src/knn_classifier/data/1/1.pgm"
    # print(lzw(filepath))
    # target = Path(filepath)
    # filename = target.name
    # dirname = target.parent.name
    # print(dirname)
    # print(filename)
    # name, ext = filename.split(".")
    # compressed_name = name + "_lzw"
    # print(compressed_name)
    # out_path = Path(dirname, "dir_test", compressed_name)
    # out_path.parent.mkdir(parents=True, exist_ok=True) # creates directory if it does not exist
    # out = open(out_path, "w")
    # out.write("Test")
    # out.close()
    # print(os.stat(out_path).st_size)


