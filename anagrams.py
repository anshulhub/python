#Checks to see if two strings are anagrams
def anagram(s, t):
    if (len(s) != len(t)):
        return False
    s = sorted(s)
    t = sorted(t)
    for i in range(0, len(s)):
        if (s[i] != t[i]):
            return False
    return True

print(anagram("hello", "hi"))
print(anagram("hello", "elloh"))
print(anagram("", ""))