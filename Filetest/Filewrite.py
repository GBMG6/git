OutFp= None
OutStr = ""

OutFp = open("C:\\Users\\USER\\Desktop\\파이썬\\Filetest\\data2.txt", "w", encoding="utf-8")

while True :
    OutStr = input("내용 입력 : ")
    if OutStr !="":
        OutFp.writelines(OutStr + "\n")

    else :
        break

OutFp.close()
print("-----정상적으로 파일에 씀------")