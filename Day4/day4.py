number = [1,2,3,4]
fruites = ['apple', 'banana', 'cherry', 'date']
mixed = [1, 'apple', 2, 'banana', 3, 'cherry',True]
# print(number[2])
# print(fruites[3])
# print(mixed[1])

fruites.append("mango")
print(fruites)
fruites.insert(1, "orange")
print(fruites)
# fruites.remove("banana")
del fruites[4]
print(fruites)
fruites.pop()
print(fruites)