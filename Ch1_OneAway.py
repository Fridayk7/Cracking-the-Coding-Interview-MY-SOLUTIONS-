def one_away(s1,s2):
    if len(s1) == len(s2):
        return replace(s1,s2)
    elif len(s1) == len(s2) +1:
        return remove_add(s1,s2)
    elif len(s1) == len(s2)-1:
        return remove_add(s2,s1)
    else:
        return False


def replace(s1,s2):
    flag = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if flag:
                return False
            else:
                flag = True
    return True


def remove_add(s1,s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 +=1
        else:
            index1 += 1
            index2 += 1
    return True



