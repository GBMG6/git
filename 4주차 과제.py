

calculate=int(input("어떤 계산을 원하시나요>>"))




if calculate == 1 :
    math1 = (input('수식을 입력하세요'))
    math2=eval(math1)
    print(f"결과: {math2}")

if calculate == 2 :
  math1=float(input("수식을 입력하세요"))
  math2=float(input("수식을 입력하세요"))
  math3=0
  while math2>=math1:
     math3+=math2
     math2=math2-1
  print(math3)