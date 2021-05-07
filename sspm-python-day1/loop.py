my_list = ["apple", "cherry", "banana"]

for i in my_list:
    print(i)

for i in range(0,len(my_list)):
    print(my_list[i])
    if my_list[i] == "banana":
        print("I got", my_list[i])
    elif my_list[i] == "mango":
        print("I got", my_list)
    else:
        print("I have others fruits")


my_dict = {
    "name": "AV",
    "age": 30,
    "profession": "IT"
}

for i in my_dict:
    print(i)

for key, value in my_dict.items():
    print(key + ":" + str(value))