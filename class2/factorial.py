# a = 1
# for i in range(1,5):
#     a*=i
#
# print(a)

def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

print(factorial(5))