# 1-check even-odd number task
value = int(input("Take a input:"))

if value%2 == 0:
    print("This is even number ")
else:
    print("This is odd number ")

# 2-range-task
name = input("Enter the Name :")
num = int(input("Enter the number :"))

for i in range(0,num):
    print(name)

# 3-range_task
number = int(input("Enter the Number: "))
name = input("Enter the name:")
for i in range(0,number):
    for x in name:
        print(x)

# 4- while loop task
total = 0
while total <= 50:
 num = int(input("Enter the Number :"))
 otal = total + num
print("Total number is ",total)


# 5-ramdon program

import  random
num = random.random()
value = num * 555
print(value)






