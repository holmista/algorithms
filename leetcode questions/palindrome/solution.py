def isPalindrome(word):
    newWord = ''
    for i in word:
        if i.isalnum(): newWord+=i.lower()
    for i in range(len(newWord)//2):
        if newWord[i]!=newWord[-i-1]: return False
    return True

print(isPalindrome('a,a'))