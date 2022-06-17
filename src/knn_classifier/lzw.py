
import string
from pathlib import Path
from struct import *
import time
import os


def get_dict(size_dic):
    dictionary = {}
    for i in range(size_dic):
        dictionary[chr(i)] = i
    # print(dictionary)
    return dictionary

def lzw(filepath="corpus.txt"):
    # filepath = "~/Documentos/Old/Documentos/Projetos/projeto_iti/iti-project/src/knn_classifier/knn.py"
    target = Path(filepath)
    filename = target.name
    dirname = target.parent.name
    name, ext = filename.split(".")
    compressed_name = name + "_lzw"
    size = 256
    k = 16
    dictionary = get_dict(size)
    max_size = pow(2, k)
    coded_msg = []

    # compress
    print(target.resolve())
    file = open(target, encoding="latin-1")
    msg = file.read()

    previous = ""

    print("Comprimindo arquivo...")
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
    print("Codificado em ", round(end - start, 2), " s")

    out_path = Path("compressed_data", dirname, compressed_name)
    out_path.parent.mkdir(parents=True, exist_ok=True)  # creates directory if it does not exist
    out = open(out_path, "wb")

    for symb in coded_msg:
        out.write(pack('>H', int(symb)))

    out.close()
    file.close()
    print("Arquivo comprimido salvo.")
    # get outfile size in bytes
    size = os.stat(out_path).st_size
    return size, len(coded_msg)


if __name__ == '__main__':
    filepath = "/home/matheusmelo/Documentos/Old/Documentos/Projetos/projeto_iti/iti-project/src/knn_classifier/data/1/1.pgm"
    print(lzw(filepath))
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


