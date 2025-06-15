inFp=None
inStr=""

inFp = open("C:\\Users\\USER\\Desktop\\파이썬\\Filetest\\data1.txt", "r", encoding="utf-8")
j=0


while True:
    inStr=inFp.readline()
    j+=1
    if inStr=="":
        break;
    print(j,":", inStr,end="")
inFp.close()