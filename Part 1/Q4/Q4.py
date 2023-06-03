import listofwords

word_lengths = [len(word) for word in listofwords.words]

max_value = max(word_lengths)
max_index = word_lengths.index(max_value)


print("Max value:  ", max_value,"Max value index:   ",max_index)