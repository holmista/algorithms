def canConstruct(ransomNote, magazine):
    for i in magazine: 
        if len(ransomNote)==0:
            return True
        try:
            ransomNote = ransomNote.replace(i, '', 1)
        except:
            pass
    if len(ransomNote)==0:
        return True
    return False

print(canConstruct("aa",
"ab"))