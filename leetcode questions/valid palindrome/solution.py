def isPalindrome(s):
    cleared = [i.lower() for i in s if i.isalnum()]
    for i in range(len(cleared)//2):
        if cleared[i] != cleared[len(cleared)-i-1]:
            return False
    return True




