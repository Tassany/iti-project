import string

def ReadTxt():
    arg = open("dados.txt","r")
    msg = []
    for linha in arg:
        msg.append(linha)
    print(msg)
    arg.close()
    return msg


def DecompressLzw(dic,code):
    for i in range(len(dic)):
        pass

def verifyDIC(dic, messageToVerify):
    try:
        index_value = dic.index(messageToVerify)
    except ValueError:
        index_value = -1

    return index_value  

def CompressLzw(dic,msg):
    code = []
    i = 0
    n = n+1

    while i < len(msg):
        for j in range(len(dic)):

            #issaqui vai virar uma recursividade INIT
            if msg[i] == dic[j]:
                # dessa forma, o array msg vai de i até n
                newMsg = msg[i:n]
                print(newMsg)
            #issaqui vai virar uma recursividade END

                index_value = verifyDIC(dic, newMsg)

                if index_value != -1:
                    code.append(index_value)
                    print("achou")
                    n = n + 1
                    i = i + 1
                    #ToDo: colocar a recursividade da interação com o próximo caractere
                else:
                    code.append(j)
                    dic.append(newMsg)
                    print(dic)

        i = i + 1
    print(code)

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
#            oxe, deveria estar no dic ERRO DIC

#marconetsf@gmail.com



def main():
    # msg = ReadTxt()
    dic = ["a","b"]
    msg = "aabababaaa"
    CompressLzw(dic, msg)
    

if __name__ == "__main__":
    main()