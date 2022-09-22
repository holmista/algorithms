def isBadVersion(version):
    if version in range(2,20):
        return True
    return False

def firstBadVersion(n):
    l, r = 1, n
    bad = -1
    a = True
    while a:
        a = l<r
        m = (l+r)//2
        if isBadVersion(m):
            bad = m
            r = m
        else:
            l = m+1
    return bad
print(firstBadVersion(2))
