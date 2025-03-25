# Primitive data types ( int, float,lone etc..)

student_name = "Mayank"
print(f"{student_name} and data type is {type(student_name)}")
roll_number = 20
print(f"{roll_number} and data type is {type(roll_number)}")
grade = 8
print(f"{grade} and data type is {type(grade)}")
weight = 45.8
print(f"{weight} and data type is {type(weight)}")
elligible_for_voting = False
print(f"{elligible_for_voting} and data type is {type(elligible_for_voting)}")


# Non - Primitive data types ( List,Tuple,Set,Dictionary)

# List - Ordered collection of items that can be changed ( Mutable)
#====================================================================
# 1.a) Ordered means - the order in which elements(items) are inserted is maintained and can ve
# accessed in the same order.
# 1.b) Insertion order is prevered
# 2. Mutable ( changeable) - Once list is defined, we can always change the elements in the list( add , remove elements)
# 3. List in python is denoted by [] square bracket
# 4. The elements in the list can be accessed(fecthed) using indexes
# 5. Index is the logical location in of an element in list which always starts with 0 and ends
# 6. List can contain duplicate values
#    with length of the list -1
names = ["Ram","Shyam","Ghanshyam"]

length = 3
indexes = [0,1,2]

# Access all the elements form the list
print(names)
# Access individual elements from the list
print(names[0])

# adding element
names.append("Rajesh")
print(names)

# remove element
names.remove("Ghanshyam")
print(names)


names = ["Ram","Shyam","Ghanshyam"]

# Print all the items from the list === Way 1=====
for name in names:
    print(name)

# Print all the items from the list === Way2=====
names = ["Ram","Shyam","Ghanshyam","Shyam"]
length = len(names)
print((length))
for idx in range(0,length,1):
    print(names[idx])

# print first 2 items from the list
#for idx in range(0,2,1):
 #   print(names[idx])


names = ["Ram","Shyam","Ghanshyam","Shyam"]
print(names)
names.remove("Shyam")
print(names)



# Tuple - Ordered collection of items that can be not changed ( Immutable)
#====================================================================
# 1.a)  Ordered means - the order in which elements(items) are inserted is maintained and can ve
# accessed in the same order .
# 1.b) Insertion order is preserved.
# 2. Immutable ( changeable) - Once list is defined, we can not be change the elements in the tuple
# 3. Tuple in python is denoted by () round bracket
# 4. The elements in the tuple can be accessed(fecthed) using indexes
# 5. Index is the logical location in of an element in tuple which always starts with 0 and ends
# 6. Tuple can contain duplicate values
# 7. Tuple is faster than List because the contents are static in Tuple whereas contents in the list are dynamic

names = ("Ram","Shyam","Ghanshyam","Shyam")
print(type(names))
for name in names:
    print(name)



# Set - Unordered collection of unique items that can be be changed( mutable).
#====================================================================
# 1. UnOrdered means - Insertion order is not preserved. the order in which insertion happens is not guranteed to stored/accessed
# accessed in the same order
# 2. mutable ( changeable) - Once set is defined, we can the elements in the set
# 3. Set in python is denoted by {} curly bracket
# 4. The elements in the set can not be accessed(fecthed) using indexes
# 5. Set can not contain duplicate values.

#names = {"Ram","Shyam","Ghanshyam","Shyam","Ghanshyam"}
#print(names)

roll_nums =[1,2,23,3,3,2,4,5,6,7,7,7,7,2,3,6,1,1,1,1,1,11,1]
roll_nums_set = set(roll_nums)
print(roll_nums_set)


# 4 - Dictonary is Mapping data type ( eno -> ename ) - it unordered
# cardinality ( 1:1, 1:m,m:1,m:m)
# emp : project ( m:m)
# in python, we call it dictionary ( dict)
# dictinary is a key value pair which an item ( key-vaue)

employees = {1:"Ajay",2:"Akshay",3:"Amit",1:"Pankaj",4:"Pankaj",}
print(len(employees))
print(employees)

employees[5]= "Rajesh"
employees[2]= "Ramesh"
print(employees)

# names = ["Rankesh","Pankaj","Mahesh","Rankesh","Pankaj","Ranjan"]
# Rankesh : 2
# Pankaj : 2
# Mahesh : 1


# Strings
name = "Amit Katkar"
l = len(name)
print(l)

# way 1
#for ch1 in name:
#    print(ch1)
 # way 2 ( amit) range(4) => range(0,4,1)
for idex in range(len(name)):
    print(name[idex])


# Slicing is helpful to extract part of string ( substring )

# Get the first 4 characters from the string
name = "Amit Katkar"
name_first4 = name[0:4:1]
#print(name_first4)


# Get the first 8 characters from the string
name = "Amit Katkar"
name_first8 = name[0:8:1]
#print(name_first8)

# Get the first 8 alternate characters from the string
name = "Amit Katkar"
name_first8 = name[0:8:2]
#print(name_first8)

# if step is postive means the control will go from left to right and negative step will move from right to left
name = "Amit Katkar"
reverse_name = name[3::-1]
print(reverse_name)

# split function
name = "Amit_Katkar"
name_list =name.split("_")
print(name_list)
print(name_list[0])

print(name_list[1])

name = "Amit Katkar"
name_first8 = name[0:8:2]
print(name_first8,len(name_first8))














