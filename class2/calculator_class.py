class Calculator(object):

    def __init__(self, num1, num2, num3=0):
        self.x = num1
        self.__y = num2
        self.z = num3

    def add(self):
        return self.x + self.__y + self.z

    def sub(self):
        return self.x - self.__y

    def multi(self):
        return self.x * self.__y

    def divide(self):
        return self.x/self.__y


class AdvancedCalculator(Calculator):
    def modulo(self):
        return self.x % self.__y
    def divide(self):
        print(__y)
        try:
            return self.x/self.__y
        except:
            print("you cannot divide by zero")

# cal1 = AdvancedCalculator(1)
# print(cal1.divide())
cal2 = Calculator(1,2)
print(cal2.add())
cal3 = Calculator(1,2,3)
print(cal3.add())