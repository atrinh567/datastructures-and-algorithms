from datastructuremodules.array import Array

arr = Array()

for i in range(0, 10):
    arr.append(i)

print(arr)

arr.push(5)
print(arr)

arr.pop()
arr.pop(2)
print(arr)

arr.delete(6)
print(arr)

print(arr.find(9))

print(arr.index(5))

print(len(arr))