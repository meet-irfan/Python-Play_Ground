# Loops  Tasks

# 1.  print 1 to 50 numbers with using while loop and for loop

numbers = 0
while numbers <50:
    numbers+= 1
    print(numbers)

# for loop
for i in range(1,51):
    print(i)

# 2. print from 40 to 1
x = 40
while x >0:
    x-= 1
    print(x)


# 3. print the multiplication table of n numbers
n = int(input("Take a input :"))
i = 1
while i <10:
    i +=1
    print(n*i)

# 4. print the elements of following list using  a loop
#[1, 9,,13,16,2`1, 38,81,100]
list = [1, 9,13,16,21, 38,81,100],

idx = 0
while idx < len(list):
    print(list[idx])
    idx+=1


# 5. Search  for  a number  x in this tuple using loop

tup = (1, 2, 3, 90, 56, 23, 45, 90 )
x = 90
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found out idx :", i)
        break
    else:print("finding.....")

    i += 1
print(" End Loop ......")

# # 6. print the elements of following  using  a loop
list = [2, 3, 4, 1, 56,34,77,23,45, 99, 100]
for i in list:
    print(i)

# 7 .  Search  for  a number  x in this  using loop

tup = (2, 3, 4, 1, 56,34,77,23,45, 99, 100)
x = 4

for i in tup :
    if(i== x):
        print("Found out idx :" ,i)
        break
        i += 1


#  8 . print the number 1 to 100 through a range function

for i in range(1, 101):
    print(i)


# 9.  print the number 100 to 1 through a range function

for i in range(100, 0 , -1):

    print(i)

# 10 .  print the multiplication table of n numbers through a range function
n = int(input("take a input : "))
for i in range(1, 11):
    print(n*i)


# 11. find the sum of first n numbers using  while  loop

n = int(input(" Take a input : "))
sum = 0
i = 1
while i<=n:
    sum+=i
    i +=1
print("total sum is :", sum)

# 12. find the factoral of first n number through loop


n = int(input(" Take a input : "))
fac = 1
i =1
while i<=n:
    fac*=i
    i+=1

print("Factoral od number is : ", fac)


