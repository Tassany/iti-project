
import string
from pathlib import Path
from struct import *

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

class LZW:
    def __init__(self, filename, k):
        # initial dictionary is a list from 0 to 255
        self.size = 5
        # self.dictionary = self.getDict(self.size)
        # print(self.dictionary)
        self.dictionary = {"a":0,"b":1,"c":2,"d":3,"r":4}
        self.max_size = pow(2, k)
        self.filename = filename
        self.coded_msg = []
    


    def getDict(self,size_dic):
        dictionary = {}
        for i in range(size_dic):
            dictionary[chr(i)] = i
        # print(dictionary)
        return dictionary


    def compress(self):
        file = open(Path(Path(__file__).parent, self.filename), encoding="latin-1")
        msg = file.read()
        # print(msg)

        previous = "" 

        for i in range(len(msg)):
            current = msg[i] + previous
            # print("current :")
            # print(current)
            if current in self.dictionary:
                # print("ACHOU!")
                previous = current
                # print("previous:")
                # print(previous)
            else:
                # print("Dicionario:")
                # print(self.dictionary[previous])
                self.coded_msg.append(self.dictionary[previous])
                if len(self.dictionary) <= self.max_size:
                    self.dictionary[current] = self.size
                    self.size += 1
                previous = msg[i]
        if previous in self.dictionary:
            self.coded_msg.append(self.dictionary[previous])

        print("Codigo: ")
        print(self.coded_msg)
        file.close()

    def decompress(self, compressedMsgFile):
        # file = open(Path(Path(__file__).parent, compressedMsgFile),"rb")
        # file_object = open('sample.txt', 'w')
        # msg = file.read()
        # print(msg)
        # previous= ""
        # aux =""

        
        input_file = ("msgCompressed")           
        maximum_table_size = pow(2,9)
        file = open(input_file, "rb")
        compressed_data = []
        next_code = 6
        decompressed_data = ""
        string = ""

        # Reading the compressed file.
        while True:
            rec = file.read(2)
            if len(rec) != 2:
                break
            (data, ) = unpack('>H', rec)
            compressed_data.append(data)

        # Building and initializing the dictionary.
        dictionary_size= 6
        dictionary = {"a":0,"b":1,"c":2,"d":3,"r":4}

        # iterating through the codes.
        # LZW Decompression algorithm
        for code in compressed_data:
            if not (code in dictionary):
                dictionary[code] = string + (string[0])
            decompressed_data += dictionary[code]
            if not(len(string) == 0):
                dictionary[next_code] = string + (dictionary[code][0])
                next_code += 1
            string = dictionary[code]

        # storing the decompressed string into a file.

        output_file = (Path(Path(__file__).parent, "decompressed.txt" ), "w")
        for data in decompressed_data:
            output_file.write(data)
            
        output_file.close()
        file.close()

                


    def save(self, output_name):
        out = open(Path(Path(__file__).parent, output_name ), "wb")
        for symb in self.coded_msg:
            out.write(pack('>H', int(symb)))
        out.close()





if __name__ == '__main__':
    coder = LZW("dados.txt", 14)
    coder.compress()
    coder.save("msgCompressed")
    coder.decompress("msgCompressed")
