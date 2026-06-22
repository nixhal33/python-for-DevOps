# This program demonstrates how to split a string into a list of substrings using the split() method in Python.
text = "I am gonna be DevOps Engineer"
split_text = text.split(" ")
print("Splited Texts:", split_text)

#output: Splited Texts: ['I', 'am', 'gonna', 'be', 'DevOps', 'Engineer'] which means the string has been split into a list of substrings based on the space character.

# word strip
word = "  !!!Funk The World!!!   "
stripped_word = word.strip(" ! ")
print("Stripped Word:", stripped_word)  

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)