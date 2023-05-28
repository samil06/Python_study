
def takeSecond(elem):
    return elem[1]

# List of tuples
tuples_list = [(1, 2), (3, 1), (4, 5), (6, 0), (7, 4)]
tuples_list.sort(key=takeSecond)
# Call the function and print the result
print(tuples_list)

