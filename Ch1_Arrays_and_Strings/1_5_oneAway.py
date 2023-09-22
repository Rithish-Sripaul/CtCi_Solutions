"""
1_5: One Away 
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 
"""

"""
Think about each of the operations:
1. Replacement: We have to replace only one charachter in the string. Meaning that the length of the strings
    will be equal
2. Insertion: The difference in length between the two strings will be one.
3. Removal: The difference will again be only one. We can use the same function for both 
    insertion and removal. Because removal is just the ivnerse of inserertion. Ensure that the parameters are sent in properly.

"""

def oneAway(s, t):
    if len(s) == len(t):
        return oneReplaceAway(s, t)
    elif len(s) - len(t) == 1:
        return oneInsertAway(s, t)
    elif len(t) - len(s) == 1:
        return oneInsertAway(t, s)

    return False

def oneReplaceAway(s, t):
    char_hash = {}

    for i in s:
        if i in char_hash:
            char_hash[i] += 1
        else:
            char_hash[i] = 1

    charReplaced = False
    for i in t:
        if i not in char_hash:
            if charReplaced:
                return False
            charReplaced = True
            continue
        char_hash[i] -= 1
    return sum(char_hash.values()) <= 1

def oneInsertAway(s, t):
    char_hash = {}

    for i in s:
        if i in char_hash:
            char_hash[i] += 1
        else:
            char_hash[i] = 1

    charInserted = False
    for i in t:
        if i not in char_hash:
            if charInserted:
                return True
            charInserted = True
            continue
        char_hash[i] -= 1
    return sum(char_hash.values()) <= 1
print(oneAway("pale", "pale"))
print(oneAway("pale", "ple"))

#######################################

"""
We can see that one edit replace and one edit insertion are very similar, by combining them
we can make a much shorter code
"""
def oneAway_shorter_version(s, t):
    if abs(len(s) - len(t)) <= 1:
        if len(s) < len(t):
            return oneEditAway(s, t)
        else:
            return oneEditAway(t, s)
        

def oneEditAway(s, t):
    char_hash = {}
    for i in s:
        if i in char_hash:
            char_hash[i] += 1
        else:
            char_hash[i] = 1
    editDone = False
    for i in t:
        if i not in char_hash:
            if editDone:
                return False
            editDone = True
            continue
        char_hash[i] -= 1
    return sum(char_hash.values()) <= 1       

print(oneAway_shorter_version("pale", "pale"))
print(oneAway_shorter_version("pale", "ple"))