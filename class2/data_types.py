x = 5 # int
x = "5" # string
x = 5.2 # float

x = () # Tuple - Array
x = [] # list

x = {} # dict


x = (1,2,3)
print(x[1])
print(len(x))

x = [1,2,3]
x.append(4)
x.pop(2)
print(x)

x = {"foo":"bar"}

print(x["foo"])
print(x.get("foo"))
print(x.get("f1oo"))
print(x.get("f1oo", "Hello"))