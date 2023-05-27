def sort_tuples(tuples_list):
    # Sort the list of tuples based on the second element of each tuple
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    return sorted_tuples

# List of tuples
tuples_list = [(1, 2), (3, 1), (4, 5), (6, 0), (7, 4)]

# Call the function and print the result
print(sort_tuples(tuples_list))
