def longestPalindrome(s):
    if len(s) < 2:
        return s
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    builderStrings = []
    for i in dict:
        if dict[i] > 1:
            toget = dict[i] if dict[i] %2 == 0 else dict[i] - 1
            for k in range(toget):
                if k % 2 == 0:
                    builderStrings.append(i)
                else:
                    builderStrings.insert(0, i)
            dict[i] = dict[i] - toget

    for i in dict:
        if dict[i] == 1:
            builderStrings.insert(len(builderStrings)//2, i)
            break

    palindrome = ''.join(builderStrings)
    return palindrome

print(longestPalindrome("bb"))