inFp, outFp = None, None
inStr = ""

inFp = open
OutFp = open("C:\\Users\\USER\\Desktop\\파이썬\\Filetest\\data3.txt", "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList : 
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("------파일이 정상적으로 복사되었음------")