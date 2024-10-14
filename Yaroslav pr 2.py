hello = "Hello World"
name = "Yaroslav"
prizv = "Grishuk"
age = 16

print(hello)
print(name)
print(prizv)
print(age)

types_list = [type(hello), type(name), type(prizv), type(age)]

print("Types of variables:", types_list)


if all(t == types_list[0] for t in types_list):
    print("Good")
else:
    common_type = types_list[0]
    filtered_types = [t for t in types_list if t == common_type]
    print("Filtered types:", filtered_types)
