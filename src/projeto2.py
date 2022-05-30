




import string


def ReadTxt():
    arg = open("dados.txt","r")
    msg = []
    for linha in arg:
        msg.append(linha)
    print(msg)
    arg.close()
    return msg

def CompressLzw(dic,msg):
    code = []
    n = 1
    i = 0
    while i < len(msg):
        for j in range(len(dic)):
            # if i < (len(msg[0]) - 1):
            if msg[i] == dic[j]:

                n = n + 1
                # dessa forma, o array msg vai de i até n
                newMsg = msg[i:n]
                print(newMsg)

                # O try serve para garantir que a func index não retorne um erro
                try:
                    index_value = dic.index(newMsg)
                except ValueError:
                    index_value = -1  

                if index_value != -1:
                    code.append(index_value)
                    print("achou")
                    n = n + 1
                    i = i + 1
                    break
                
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
#         oxe, deveria estar no dic ERRO DIC
   








def main():
    # msg = ReadTxt()
    dic = ["A","B","C","D","R"]
    msg = "ABRACADABRA"
    CompressLzw(dic, msg)
    

if __name__ == "__main__":
    main()