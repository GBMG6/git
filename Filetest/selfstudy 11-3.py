OutFp= None
OutStr = ""
fName = input("파일명을 입력하세요 : ")
OutFp = open(fName, "w", encoding="utf-8")

while True :
    OutStr = input("내용 입력 : ")
    if OutStr !="":
        OutFp.writelines(OutStr + "\n")

    else :
        break

OutFp.close()
print("-----정상적으로 파일에 씀------")