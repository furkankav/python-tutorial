import datetime
import os

print (datetime.datetime.now())

dir(int)
dir(list)
dir(__builtins__)
dir(str)
help(str.upper)
help(str.title)
type(5) # int
type("ss") # str

print("upper ", 'hello'.upper())
print("title ", 'title'.title())


student_grades = [8.1, 3.2, 10.0, 5.6]
print("Student grades ", student_grades)
def mean(my_list):
    list_sum = sum(my_list)
    num = len(my_list)
    return list_sum / num

mean = mean(student_grades)
print("mean ", mean)

dict_students = { "Marry": 9.8, "John": 5.1, "Kiki": 3.4}
print("Student dictionary ", dict_students )

monday_temperatures = (65, 79, 46)
print("This is a tuple ", monday_temperatures)
# Lists are mutable, tuples are immutable
# Tuples are a little bit faster than lists

test_list = [5.8, 6.4, 9.2, 4.7]
test_list.append(3.8)
test_list.pop()
# pop will remove the last element from the list
test_list.index(6.4)

# this would return 1 
#test_list.index(6.4, 2) 
# 2 is the index it will start searching from you can add 3rd parameter to specify stopping index
# this would return ValueError: 6.4 is not in list
test_list[2] # will return 9.2


user_input = input("Enter your name: ")
print("Hello %s" % user_input)
temp_surname = "Test"
print("Hello %s %s" % (user_input, temp_surname))

#Works only after python 3.6 
print(f"Hello {user_input} {temp_surname}")

print("isinstance method helps you verify var type : isinstance('test', str) -> {} ".format(isinstance('test', str)))


# Iterating through dictionary 
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

# if this is list startswith will give error it needs to be tuple
interrogatives = ("how", "why", "when", "who", "what")
phrase = "why are you here"
if phrase.startswith(interrogatives):
    print("{}?".format(phrase))

print(" ".join(interrogatives))


# List comprehension
# leaving data [22.1, 41.2, 10.8] like this would use a lot of memory(in hard disk)
# In your code save hard coded variables like this instead [221, 412, 108]
# In your code change this list to desired format easy way to do is
temps = [221, 412, 108]
temps = [temp/10 for temp in temps]
print("Temp list after comprehension {}".format(temps)) 
# You can have a condition during comprehension
temps = [100, 241, 440, 340, 90, 510]
temps = [temp/10 for temp in temps if temp < 400]
print(f"Temps below 40 {temps}")
arr = [1,2,10,4, "test", "ki"]
print([num if isinstance(num, int) else 0 for num in arr ])


# use *args and **kwargs for indefinite # of parameters

#args would be a tuple
def find_sum_args(*args):
    return sum(args)

#kwargs would be a dictionary
def find_sum_kwargs(**kwargs):
    return sum(kwargs.values())

find_sum_args(1, 2, 5, 6, 7)
find_sum_kwargs(num1 = 1, num2 = 2, num3 = 6)

# You can read a file like this
# myfile = open("files/fruits.txt")
# content = myfile.read()
# myfile.close() 
# However this is a better way to read it
with open("files/fruits.txt") as myfile:
    content = myfile.read()
# it closes automatically
print(content)

# It creates the file if it exists it overrides it
with open("files/data.txt", "w") as data:
    data.write("Furkan\n")

# a gives you option to write where file is ended (append)
# + gives you read option
# when you open the file cursor is at the and so it moves it to 
# start with seek
with open("files/data.txt", "+a") as data:
    data.seek(0)
    content = data.read()
    data.write(content * 2)
    data.seek(0)
    print(data.read())

# you can check if file exists with
# don't forget to import os
doesExist = os.path.exists("files/data.txt")
print(f"Does file files/data.txt exists: {doesExist}")
    
