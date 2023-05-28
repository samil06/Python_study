def takeSecond(elem):
    return elem[1]

# List of tuples
list = [1, 3, 4, 6, 7,7]

for i in list:
    Counter=list.count(i)
    if Counter != 1:
        #print(Counter)
        print("Not unique: ", i)


# Call the function and print the result
