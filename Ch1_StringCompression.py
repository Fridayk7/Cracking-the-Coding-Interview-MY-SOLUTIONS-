def compression(s):
    mymap = [0 for i in range(ord('z')-ord('A'))]
    for i in s:
        mymap[ord(i)-ord('A')] += 1
    final =[]
    for i in range(ord('z')-ord('A')):
        if mymap[i] > 0:
            final.append(chr(i+ord('A')))
            final.append(str(mymap[i]))
    final = "".join(final)
    if len(s) > len(final):
        return final
    else:
        return s
