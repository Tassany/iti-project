
import string
from pathlib import Path
from struct import *
import time

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


def get_dict(size_dic):
    dictionary = {}
    for i in range(size_dic):
        dictionary[chr(i)] = i
    # print(dictionary)
    return dictionary


# initial dictionary is a list from 0 to 255
filename = "disco.mp4"
name, ext = filename.split(".")
compressed_name = name + "_compressed"
decompressed_name = name + "_decompressed" + "." + ext
size = 256
k = 16
dictionary = get_dict(size)
# print(self.dictionary)
# self.dictionary = {"a":0,"b":1,"c":2,"d":3,"r":4}
max_size = pow(2, k)
coded_msg = []
decoded_msg = ""


# Comprimir
file = open(Path(Path(__file__).parent, filename), encoding="latin-1")
msg = file.read()
# print(msg)

previous = ""

print("Comprimindo arquivo...")
start = time.time()
for i in range(len(msg)):
    current = msg[i] + previous
    # print("current :")
    # print(current)
    if current in dictionary:
        # print("ACHOU!")
        previous = current
        # print("previous:")
        # print(previous)
    else:
        # print("Dicionario:")
        # print(dictionary[previous])
        coded_msg.append(dictionary[previous])
        if len(dictionary) <= max_size:
            dictionary[current] = size
            size += 1
        previous = msg[i]
if previous in dictionary:
    coded_msg.append(dictionary[previous])
end = time.time()
print("Codificado em ", round(end - start, 2), " s")
# Salvar arquivo comprimido
out = open(Path(Path(__file__).parent, compressed_name), "wb")
for symb in coded_msg:
    out.write(pack('>H', int(symb)))
out.close()
file.close()
print("Arquivo comprimido salvo.")


# Descomprimir

# Ler o arquivo comprimido
file = open(Path(Path(__file__).parent, compressed_name), "rb")
coded_msg = []
print("Descomprimindo arquivo...")
start = time.time()
# Salvamos cada índice da mensagem codificada utilizando 2 bytes, assim precisamos ler cada 2 bytes do arquivo
while True:
    index = file.read(2)
    if len(index) != 2:
        break
    (data,) = unpack('>H', index)
    coded_msg.append(data)
file.close()

# Reiniciar o dicionário
size = 256
dictionary = dict([(x, chr(x)) for x in range(size)])

previous = ""
next_index = 256

# Para cada índice da mensagem decodificada, verificar o seu valor no dicionário
# Se não encontrar, inserir no dicionário
for index in coded_msg:
    if not (index in dictionary):
        dictionary[index] = previous + (previous[0])
    decoded_msg += dictionary[index]
    if not (len(previous) == 0):
        dictionary[next_index] = previous + (dictionary[index][0])
        next_index += 1
    previous = dictionary[index]
end = time.time()
print("Decodificado em ", round(end - start, 2), " s")

# Resultado em "decompressed.txt"
decompressed_file = open(Path(Path(__file__).parent, decompressed_name), "w", encoding="latin-1")
for data in decoded_msg:
    decompressed_file.write(data)

decompressed_file.close()

print("Arquivo descomprimido salvo.")

