a=int(input("입력 진수를 결정하세요 {16/10/8/2} : "))
b=input("값을 입력하세요 : ")
if (a==16) :
    c=int(b,16)

if (a==8) :
    c=int(b,8)

if (a==10) :
    c=int(b,10)

if (a==2) :
    c=int(b,2)


print("16진수 ==> " , hex(c))
print("10진수 ==> ",c)
print("8진수 ==> ",oct(c))
print("2진수 ==> ",bin(c))



