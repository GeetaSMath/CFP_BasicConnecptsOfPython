# --Dictionary Comprehension---
# key = ['a', 'b', 'c']              # created list key elements
# values = ["hii", "hello", "good"]   # created list values
# my_dict = {key: values for (key, values) in zip(key, values)}  # Dictionary Comprehension
# print(my_dict)
my_dict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}  # dictionary Comprehension printing Square number of the list
print(my_dict)
s_dict = {x.upper(): x * 3 for x in 'coding'}  # dictionary Comprehension printing Uppercase letter printing thrice
print(s_dict)

empty_dict = {}
for n in range(10):
    if n % 2 == 0:
        empty_dict[n] = n * 2
print(empty_dict)

# --list comprehension--------
numbers = []             # created empty list
for i in range(1, 6):    # 1 to 6 range that is range of the list
  numbers.append(2**i)   # by suing append added 2**i
print(numbers)

#--list Comprehension to find Square numbers--
square = []
for i in range(1, 10, 2):
   square.append(i**2)
print(square)

# ---create student data list---
student_data_list = [("Geeta", 121), ("Aishu", 122), ("Vidhy", 123)]   # created student list and id
student_id= [id for (name , id) in student_data_list if id > 121]      # list comprehension to access students id
print(student_id)
