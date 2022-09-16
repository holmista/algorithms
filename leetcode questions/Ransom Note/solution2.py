def canConstruct(ransomNote, magazine):
    dict = {}
    for i in magazine: 
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 0
    for i in ransomNote:
        if i in dict:
            if dict[i]>=0:
                dict[i] -=1
            else: return False
        else: return False
    return True

print(canConstruct(ransomNote = "a", magazine = "b"))
