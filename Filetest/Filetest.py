inFp=None
inStr=""

inFp = open("C:\\Users\\USER\\Desktop\\파이썬\\Filetest\\data1.txt", "r", encoding="utf-8")



inStr=inFp.readline()
print(inStr,end = "")

inStr=inFp.readline()
print(inStr,end = "")

inStr=inFp.readline()
print(inStr,end = "")

inFp.close()