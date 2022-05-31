import string
from symtable import Symbol
import os


def DecompressLzw(dic,code):
    for i in range(len(dic)):
        pass


def CompressLzw():
    print("Comprimindo arquivo!")
    file = open("dados.txt",encoding="latin-1")
    msg = file.read()
    maximum_size = pow(2,14) 
    dic_size = 256
    dic = []
    for i in range(dic_size):          
        dic.append(i)
    print(dic)
    code = []
    msg_plus = ""

    for i in range(len(msg)-1):
        auxMsg = msg[i]
        oneMsg = msg[i+1]
        msg_plus = auxMsg + oneMsg

        try:
            index_value = dic.index(msg_plus)
        except ValueError:
            index_value = -1

        if index_value != 1:
            auxMsg += oneMsg
        else:
            code.append(i)
        dic.append(auxMsg)
        auxMsg = oneMsg

    print("Codigo: ")
    print(code)


def main():

    CompressLzw()
    
    

if __name__ == "__main__":
    main()