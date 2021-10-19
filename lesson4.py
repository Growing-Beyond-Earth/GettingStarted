# the + operator in python is overloaded!
print(3+5)
print(type(3), type(5), type(3+5))

print(3+5.0)
print(type(3), type(5.0), type(3 + 5.0))

print("3" + "5")
print(type(3), type(5), type("3" + "5"))

print([1,2,3]+[4,5])
print(type([1,2,3]), type([4,5]), type([1,2,3]+[4,5]))

#what is range?
print(range(5))

# range(stop)
for i in range(5):
    print(i)

#range(start, stop)
range_as_list = [i for i in range(3, 10)]
print(range_as_list)

# range(start, stop, step)
print([i for i in range(3, 5, .5)])
