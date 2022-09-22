def longestPalindrome(s):
    if len(s) < 2:
        return len(s)
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    length = 0
    for i in dict:
        if dict[i] > 1:
            toget = dict[i] if dict[i] %2 == 0 else dict[i] - 1
            length += toget
            dict[i] = dict[i] - toget

    for i in dict:
        if dict[i] == 1:
            length += 1
            break

    return length

print(longestPalindrome("bb"))