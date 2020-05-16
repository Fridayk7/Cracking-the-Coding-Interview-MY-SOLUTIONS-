def string_rotation(s1,s2):
    return is_substring(s1,s2+s2)

def is_substring(s1,s2):
    return s1 in s2


print(string_rotation("waterbottle","bocr"))