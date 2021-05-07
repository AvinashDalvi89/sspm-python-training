my_list = ["apple", "cherry", "banana"]

print("Show me second element : ", my_list[1])

my_list.append("mango")
print(my_list)

my_dict = {
    "name": "AV",
    "age": 30,
    "profession": "IT"
}
print(my_dict)

print(my_dict['name'])
print(my_dict.get("age"))
#print(my_dict['surname'])
print(my_dict.get("year"))
my_dict["year"] = 1989
print(my_dict)
my_list.remove("banana")
print(my_list)


my_tuple = ("apple", "cherry", "banana")
print(my_tuple)
#my_tuple.append("orange") # This will raise an error

print(my_tuple)

my_tuple = list(my_tuple)
my_tuple.append("orange")
print(my_tuple)
print(tuple(my_tuple))
