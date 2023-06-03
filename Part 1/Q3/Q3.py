
def fun():
    inp = input('Write string:  ')
    lowercase_letter_number=0
    uppercase_letter_number=0
    for i in inp:
        letter_count=i.isupper()
        if letter_count==1:
            uppercase_letter_number=uppercase_letter_number+1
        else:
            lowercase_letter_number=lowercase_letter_number+1
    print(inp)
    return lowercase_letter_number,uppercase_letter_number

print(fun())

