val = input("Enter your value: ")


new_val = [val[len(val)-i-1] for i in range(len(val))]
new_val_string = "".join(new_val)



print(val)
print(new_val)
print(new_val_string)