# 1. Asked for user entered  movies name and stored in tuple
movies = []
name = str(input("enter the 1 Movie name: "))
name1 = str(input("enter the 2 Movie name: "))
name2 = str(input("enter the 3 Movie name: "))

movies.append(name)
movies.append(name1)
movies.append(name2)

print(movies)

# 2. check if a list contains a palindrome of elments


list = [1,2,1]
list1 =[1,2,4,5]
copy_list = list.copy()
copy_list.reverse()
if (copy_list == list):
    print("Palindrome")
else:print("Not Palindrome")

# 3. count the number of students with grade "A" with following tuple

tup = ("A","D", "A","E","B", "B",)
print(tup.count("B"))

# 4. store the tuples values in a list and sort them "A" to "D"

grade = ["A","D", "A","E","B", "B",]
print(grade.sort())
print(grade)







