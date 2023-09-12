"""
1_3: URLify
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.) 
"""

# We will replacing the spaces from the end of the string

def URLify(s, truelength):
	char_list = list(s)
	new_index = len(char_list)

	for i in reversed(range(truelength)):

		if char_list[i] == " ":
			# Replacing the spaces
			char_list[new_index - 3 : new_index] = "%20"
			new_index -= 3
		else:
			# Moving charachters to the end
			char_list[new_index - 1] = char_list[i]
			new_index -= 1
	return "".join(char_list)


print(URLify("Mr John Smith    ", 13))
print(URLify("much ado about nothing      ", 22))