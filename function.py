# Function  Tasks

# 1. print the length of list. (list is parameter)
num = [1,2,5,6,7,7,8,9,0,35]
name =["irfan","Aamir", "khan ","bhai","j"]

def len_list(list):
    print(len(list))
len_list(num)
len_list(name)

# 2. print the elements of a list in single line.

name =["irfan","Aamir", "khan ","bhai","j"]
num = [1,2,5,6,7,7,8,9,0,35]

def print_list(list):
    for ele in list:
        print(ele, end="")

print(name)
print(num)

#3. WAF to find  the factorial of n numbers

def find_fac(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print(fac)
find_fac(6)

# 4.WAF to convert USD to INR
def convert_Con(usd):
    inr = usd*83
    print(usd,"USD =", inr ,"INR")
convert_Con(1)












