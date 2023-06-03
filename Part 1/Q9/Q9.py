dict1 = {"name": "John", "age": 25}

dict2 = {"occupation": "Engineer", "hobby": "Reading"}

merged_dict = {**dict1, **dict2}


print(merged_dict)
print(merged_dict['name'])