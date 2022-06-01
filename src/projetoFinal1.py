
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

# Estamos utilizando a lib struct do python para interpretar bytes como objetos do python e fazer a interpretacão correta de uma quantidade pre definida de bits no arquivo.
# Ao utilizar o Formato "H" (unsigned short em C), estamos definindo usar 2 bytes para salvar cada pacote binário no arquivo
# Ao utilizar o Formato "i" (int em C), estamos definindo usar 4 bytes para salvar cada pacote binário no arquivo

class LZW:
    def __init__(self, filename, k):
        # initial dictionary is a list from 0 to 255
        self.size = 256
        self.dictionary = self.getDict(self.size)
        # print(self.dictionary)
        # self.dictionary = {"a":0,"b":1,"c":2,"d":3,"r":4}
        self.max_size = pow(2, k)
        self.filename = filename
        self.coded_msg = []
        self.decoded_msg = ""
    


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

        # print("Codigo: ")
        # print(self.coded_msg)
        file.close()

    def decompress(self, compressedMsgFile):

        # Ler o arquivo comprimido
        self.read_compressed(compressedMsgFile)

        # Reiniciar o dicionário
        self.size = 256
        self.dictionary = self.getDict(self.size)

        previous = ""
        next_index = 256

        # Para cada índice da mensagem decodificada, verificar o seu valor no dicionário
        # Se não encontrar, inserir no dicionário
        for index in self.coded_msg:
            if not (index in self.dictionary):
                print(previous)
                self.dictionary[index] = previous + (previous[0])
            self.decoded_msg += self.dictionary[index]
            if not(len(previous) == 0):
                dictionary[next_index] = previous + (self.dictionary[index][0])
                next_index += 1
            previous = self.dictionary[index]

        # Resultado em "decompressed.txt"
        file = (Path(Path(__file__).parent, "decompressed.txt"), "w")
        for data in decompressed_data:
            file.write(data)
            
        file.close()

    def save(self, output_name):
        out = open(Path(Path(__file__).parent, output_name), "wb")
        for symb in self.coded_msg:
            out.write(pack('>H', int(symb)))
        out.close()

    def read_compressed(self, filename):
        file = open(Path(Path(__file__).parent, filename), "rb")
        self.coded_msg = []
        # Salvamos cada índice da mensagem codificada utilizando 2 bytes, assim precisamos ler cada 2 bytes do arquivo
        while True:
            index = file.read(2)
            if len(index) != 2:
                break
            (data,) = unpack('>H', index)
            self.coded_msg.append(data)
        file.close()




if __name__ == '__main__':
    k = 14
    coder = LZW("corpus.txt", k)
    print("Comprimindo arquivo...")
    coder.compress()
    coder.save("corpusCompressed")
    print("Arquivo comprimido salvo.")

    print("Descomprimindo arquivo...")
    coder.decompress("corpusCompressed")
    print("Arquivo descomprimido salvo.")
