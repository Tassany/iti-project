


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


def CompressLzw(dic,msg):







def main():
    # msg = ReadTxt()
    dic = ["a","b"]
    msg = "aabababaaa"
    CompressLzw(dic, msg)
    

if __name__ == "__main__":
    main()