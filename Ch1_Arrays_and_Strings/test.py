def palindromePermutation(s):

    oddCharPresent = 0
    char_hash = {}
    
    for i in s:
        if i != " ":
            if i in char_hash:
                char_hash[i] += 1
                if char_hash[i] % 2 == 0:
                    oddCharPresent -= 1
                else:
                    oddCharPresent += 1
            else:
                char_hash[i] = 1
                oddCharPresent += 1
        
    return True if oddCharPresent <= 1 else False

print(palindromePermutation("tact coa"))
        