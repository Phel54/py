from timeit import timeit
import csv

import numpy as np

a = np.array([[1, 2, 3, 4], [2, 4, 52, 4], [2, 4, 52, 4]])
b = np.array([[1, 4, 3, 5], [2, 7, 52, 4], [2, 9, 52, 2]], np.int32)
# print(a)
#
# np.savetxt('text1.txt', b)
# y1 = np.loadtxt('text1.txt')
# print('Text1  : \n', y1)
# # print(np.shape(a))
# print(a.shape)

# myArray = np.arange(0, 1000, 2)
# myArray2 = [x ** 2 for x in myArray]
# print(myArray)
# print(myArray2)
# print(timeit(setup='myArray = range(1000)', stmt='[x ** 2 for x in myArray]', number=1000))


with open('flintstones.csv', newline='') as f:
    reader = csv.DictReader(f)
    people17 = np.empty((0, 6))
    for row in reader:
        oneRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        people17 = np.append(people17, oneRow, axis=0)

print(people17)
print(people17.ndim)
print(people17.shape)

with open('flintstines1.csv', newline='') as f:
    reader = csv.DictReader(f)
    people16 = np.empty((0, 2))
    for row in reader:
        oneRow = np.array([[row['Adj Close'], row['Volume']]])
        people16 = np.append(people16, oneRow, axis=0)

print(people16)
print(people16.ndim)
print(people16.shape)
print(people16.sum())




