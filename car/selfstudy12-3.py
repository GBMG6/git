import threading

class SumThread:
    def __init__(self, n):
        self.n = n

    def run(self):
        total = self.n * (self.n + 1) // 2
        print(f"1+2+3+...+{self.n} = {total}")

sum1 = SumThread(1000)
sum2 = SumThread(100000)
sum3 = SumThread(1000000)

th1 = threading.Thread(target=sum1.run)
th2 = threading.Thread(target=sum2.run)
th3 = threading.Thread(target=sum3.run)

th1.start()
th2.start()
th3.start()

