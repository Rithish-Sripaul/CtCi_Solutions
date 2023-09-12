"""
1_2: Given two strings, write a method to decide if one is a permutation of the other.
"""

# Confirming Questions:
# 1. is it Case sensitive? -> is Abc different from Bac
# 2. is whitespace significant? -> is "abc    " different from "bac"

# For the following answers, we are assuming that it is case sensitive and whitespace is significant

#TC: O(N)
#SC: O(N)
def checkPermutation(s, t):
	if len(s) != len(t): return False
	char_hash = {}
	for i in s:
		if i in char_hash:
			char_hash[i] += 1
		else:
			char_hash[i] = 1

	for i in t:
		if i not in char_hash:
			return False
		if char_hash[i] < 0:
			return False
		char_hash[i] -= 1

	for char in char_hash:
		if char_hash[char] > 0:
			return False
	return True

#TC: O(NlogN)
#SC: O(N)
def checkPermutation_using_sorting(s, t):
	if len(s) != len(t): return False
	sorted_s = sorted(s)
	sorted_t = sorted(t)

	for i in range(len(s)):
		if sorted_s[i] != sorted_t[i]:
			return False
	return True


print(checkPermutation("abc", "bac"))
print(checkPermutation("abcs", "bac"))
print(checkPermutation("abcs", "bsac"))
print(checkPermutation_using_sorting("abcs", "bsac"))
print(checkPermutation_using_sorting("abc", "bsac"))

