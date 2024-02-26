array = [3, 2, 1]
newArray = [1] * len(array)

for i in range(len(array)):
  for j in range(len(array)):
    if i != j:
      newArray[i] *= array[j]


print(newArray)