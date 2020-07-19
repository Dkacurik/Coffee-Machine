
n = int(input())
mylist = []

for x in range(0, n):
    number = int(input())
    if(number % 7 == 0):
        mylist.append(number)

for y in mylist:
    print(y*y)
