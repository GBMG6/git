inFp, outFp = None, None
inStr = ""
i=input("소스 파일명을 입력하세요 :")
l=input("타킷 파일명을 입력하세요 :")

inFp = open(i)
OutFp = open(l, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList : 
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("------",i," 파일이 ",l, "파일로 정상적으로 복사되었음------")