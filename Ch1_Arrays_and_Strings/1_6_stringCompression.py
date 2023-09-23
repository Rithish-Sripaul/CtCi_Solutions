"""
1_6: String Compression: 

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""

def stringCompression(s):

    countChar = 0
    resultArr = []

    for i in range(len(s)):
        
        countChar += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            resultArr.append(f"{s[i]}{countChar}")
            countChar = 0
    resultStr = "".join(resultArr)
    return s if len(s) <= len(resultStr) else resultStr

print(stringCompression("aaabbcccccaa"))
print(stringCompression("abcccc"))