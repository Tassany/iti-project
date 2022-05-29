




import string
from xml.etree.ElementTree import tostring


def ReadTxt():
    arg = open("test.txt","r")
    msg = []
    for linha in arg:
        msg.append(linha)
       


    print(msg)
    arg.close()
    return msg

def CompressLzw(dic,msg):
    code = []
    n = 1
    for i in range(len(msg[0])):
        for j in range(len(dic)):
            if i < (len(msg[0]) - 1):
                

                if msg[0][i] == dic[j]:
                    n = n + 1
                    newMsg = msg[0][i:n]
                    print("N " + str(n))
                    print("NewMsg " + newMsg)
                    try:
                        index_value = dic.index(newMsg)
                    except ValueError:
                        index_value = -1

                    if index_value != -1:
                        code.append(index_value)
                    
                    else:
                        code.append(j)
                        dic.append(newMsg)
                        print(dic)
                        


    
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
    msg = ReadTxt()
    dic = ["A","B","C","D","R"]
    CompressLzw(dic, msg)
    

if __name__ == "__main__":
    main()