x = 12.23 #float
print(type(x))

my_class = complex(1,3)
print(type(my_class))

#rules for creating variable
my_list = [1,35,65, "you are not performing well"]
print(my_list)


my_list.append(1)
print(my_list)

my_list.insert(3,45)
print(my_list)


b2 = [1,2,3, "Abinash"]
print(type(b2))

b3=(1,2,3,"Abi")
print(type(b3))


#3c dictionary

my_dictionary ={'name': "Abinash",'age':20, 'city': 'Delhi'}
print(type(my_dictionary))

# 4d. sets 
my_sets ={1,2,3,"Abi"}
print(type(my_sets))


my_list = [1,35,65,"you are not performing well"]
print(my_list)
# removing elements in List
my_list.remove(65) # remove by element
my_list.pop() #last element
del my_list[0] #by indexing


my_list = [1,35,65,"you are not performing well"]
my_list.remove(65)
print(my_list)

my_list = [1,35,65,"you ate not performing well"]
del my_list[3]
print(my_list)

my_list = [1,35,65,"you are not performing well"]
del my_list[3]
print(my_list)

#age category

age = int (input("Enter your age: "))
if age < 18:
    print("You are a child.")
elif age < 25:
    print("You are a Teen ager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

a='1'
b="3"
print(a+b)


a=("it's a rainy day \nyou ate a Bad man") #\n new for new line
print(a)

x= "honey singh"  #repetation string
print(x*5)

a=("it's a rainy day   you are a Bad ") #tittle string
print(a.title())

a=("it's a rainy day   you are a Bad ") #strip string
print(a.strip())

a=(" 'Hello world' ")
print(a.strip())

