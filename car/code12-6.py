class Car :
    color = ""
    speed = 0
    count = 0

    def __init__(self):
        self.Speed = 0
        Car.count +=1

myCar1,myCar2 = None,None

myCar1 =Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %dkm,생산된 자동차는 총 %d대입니다." %(myCar1.speed,myCar2.count))
myCar2 =Car()
myCar2.speed = 30
print("자동차2의 현재 속도는 %dkm,생산된 자동차는 총 %d대입니다." %(myCar2.speed,myCar2.count))