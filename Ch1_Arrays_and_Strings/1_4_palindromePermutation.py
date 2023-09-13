"""
1_4: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words. 

"""


"""
For a string to be a palindrome:
1. Strings of even length can't have charachters of odd count
2. Strings of odd length can have exactly one charachter of odd count

In the end, we can say that for a string to be a palindrome, it CANNOT have 
more than one charachter that is odd in count.  
"""

# Using hash table
# TC: O(N)
def palindromePermutation(s):
	char_hash = {}

	l = 0
	for i in s:
		if i != " ":
			l += 1

	for i in s:
		if i != " ":
			if i in char_hash:
				char_hash[i] += 1
			else:
				char_hash[i] = 1

	if l % 2 == 1:
		oddChar_present = False
		for i in char_hash:
			if char_hash[i] % 2 == 1:
				if oddChar_present:
					return False
				oddChar_present = True
	return True

# Using arrays
def palindromePermutation_using_arrays(s):
	table = [0 for _ in range(26)]
	countodd = 0
	for c in s:
		x = char_number(c)

		if x != -1:
			table[x] += 1
			if table[x] % 2 == 0:
				countodd -= 1
			else:
				countodd += 1
	return countodd <= 1
	
def char_number(c):
	a = ord("a")
	z = ord("z")
	A = ord("A")
	Z = ord("Z")
	val_c = ord(c)

	if a <= val_c <= z:
		return val_c - a

	if A <= val_c <= Z:
		return val_c - A

	return -1

	
print(palindromePermutation("tact coa"))
print(palindromePermutation("mem"))
print(palindromePermutation_using_arrays("tact coa"))
print(palindromePermutation_using_arrays("tact coa"))