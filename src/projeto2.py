import string
from pathlib import Path
from struct import *


class LZW:
    def __init__(self, filename, k):
        # initial dictionary is a list from 0 to 255
        self.size = 256
        self.dictionary = {chr(i): i for i in range(self.size)}
        self.max_size = pow(2, k)
        self.filename = filename
        self.coded_msg = []

    def compress(self):
        file = open(Path(Path(__file__).parent, self.filename), encoding="latin-1")
        msg = file.read()
        previous = ""

        for symb in msg:
            current = previous + symb
            if current in self.dictionary:
                previous = current
            else:
                self.coded_msg.append(self.dictionary[previous])
                if len(self.dictionary) <= self.max_size:
                    self.dictionary[current] = self.size
                    self.size += 1
                previous = symb
        if previous in self.dictionary:
            self.coded_msg.append(self.dictionary[previous])
        file.close()

    def save(self, output_name):
        out = open(Path(Path(__file__).parent, output_name + ".lzw"), "wb")
        for symb in self.coded_msg:
            out.write(pack('>H', int(symb)))
        out.close()


# LZW RESUMINDO
# começa com o um dicionário inicial
# lê o caracter
#     ela está no dicionario?
#         se sim:
#             procura se a proxima letra mais ela está no dic
#                 se sim:
#                     coloca o codigo
#                 se não:
#                     coloca o codigo apenas do caracter
#                     add no dic
#         se não:
#         oxe, deveria estar no dic ERRO DIC


if __name__ == '__main__':
    coder = LZW("corpus2.txt", 15)
    coder.compress()
    coder.save("awesome")
