# Clarifications:
# White space does not count
# Non-case sensitive

# Assumptions:
# The characters set is ASCII

def pali_perm1(s):
    # O(n) frebee changing all letters to lower for simplicity
    s = s.lower()
    #O(n) freebee removing spaces for simplicity
    s = "".join([i for i in s if ord(i) != ord(' ')])

    mymap = [0 for i in range(ord('z')-ord('a') +1)]
    for i in s:
        print(i)
        mymap[ord(i)-ord('a')] +=1

    count = 0
    for i in mymap:
        if i%2 != 0:
            count +=1
            if count >=2:
                return False
    return True
