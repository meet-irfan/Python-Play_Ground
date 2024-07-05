#  set and Dictionary Problems

# 1. store  following words meanings in python dictionary

dictionary = {
    "table" :  [" a piece of furniture ", " lists of facts & figures " ],

    "cat" : "a small animal "
}

print(dictionary)



# 2. you are given a list of subjects for students . Assume that on classroom is required 1 subjects . How many classroom are needed by all students

subjects ={
"python","jave","c++","python","js","jave","python", "jave", "c++","c"
}
print(subjects)
print(len(subjects))

# 3. enter the marks of 3 subjects from  the user & store them in a dictionary
# start with empty dictionary & add one by one . use subjects names as keys and marks as value

marks ={}

value = int(input("Enter the  marks of first sub:"))
marks.update({"math":value})

value= int(input("Enter the  marks od second sub :"))
marks.update({"chemistry":value})

value= int(input("Enter the marks of third sub :"))
marks.update({"English": value})

print(marks)

# 4. figure out of way  to store 9 and 9.0 as separate values in the set

num = {
    ("float", 9.0),
    ("int",9)
}
print(num)

