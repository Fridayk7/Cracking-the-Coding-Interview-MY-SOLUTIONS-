# Assumptions:
# The characters set is ASCII


def urlify(s,length):
    snew = ""
    for i in range(length):
        if ord(s[i]) == ord(" "):
            snew += "%20"
        else:
            snew += s[i]
    return snew


print(urlify("Hello my name is michael    ",24 ))
