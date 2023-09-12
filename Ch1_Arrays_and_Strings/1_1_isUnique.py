"""
1_1: 
"""

# Ask the interviewer if the string is of the format ASCII or Unicode
# ASCII has a size of 128

# TC: O(n)
# SC: O(1) (because the loop will never iterate for more than 128 times)
def isUnique_algorithmic(s):

	# Because the number of charachters in ASCII is 128
	if len(s) > 128: return False

	char_set = [False] * 128
	for i in range(len(s)):
		# Using ord() to get the ASCII equi. of a charachter
		if char_set[ord(s[i])] == True:
			return False
		char_set[ord(s[i])] = True
	return True


def isUnique_using_set(s):
	charachters_seen = set()
	for i in s:
		if i in charachters_seen:
			return False
		charachters_seen.add(i)
	return True

# TC: O(NlogN)
# SC: O(1)
def isUnique_chars_sorting(s):
	s_sorted = sorted(s)
	last_chars = None
	for i in s_sorted:
		if last_chars == i:
			return False
		last_chars = i
	return True

print(isUnique_algorithmic("abcdefghijklmnopqrstuvwxyz"))
print(isUnique_algorithmic("aabs"))
print(isUnique_using_set("abcdefghijklmnopqrstuvwxyz"))
print(isUnique_using_set("aabs"))
print(isUnique_chars_sorting("abcdefghijklmnopqrstuvwxyz"))
print(isUnique_chars_sorting("aabs"))


