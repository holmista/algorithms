def canConstruct(ransomNote, magazine):
    dict1 = {}
    dict2 = {}
    for idx, val in enumerate(ransomNote): 
        if val in dict1:
            dict1[val]+=1
        else:
            dict1[val] = 0
    for idx, val in enumerate(magazine): 
        if val in dict2:
            dict2[val]+=1
        else:
            dict2[val] = 0
    for i in dict1:
        if i in dict2 and dict2[i]>=dict1[i]:
            continue
        else:
            return False
    return True

print(canConstruct("bg",
"efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
