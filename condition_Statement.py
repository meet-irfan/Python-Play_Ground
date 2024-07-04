# String and If else condition statement

# 1. take a input by user's Name and print the length

name = str(input("Input the name :"))
print(len(name))

# 2. Find the occurrence of $ in a string

str = '$hello , $125 , $khan, $irfan'
print(str.count("$"))

# 3. Student Marks sheet program

grade = int(input("Take a number:"))
if (grade>=90):
    print("A")
elif(grade>=80):
    print("B")
elif(grade>=70):
    print("C")
else:print("F")

# 4. find the grestest number of enetered by user

a = int(input("Take first number:"))
b = int(input("Take second number:"))
c = int(input("Take third number:"))
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
else:print(c)


# 5. check the number mutiply by 7 or not
num = int(input("Take a input :"))
if(num%7==0):
    print("This number mutiply by 7 :",num)
else:print("Not")









