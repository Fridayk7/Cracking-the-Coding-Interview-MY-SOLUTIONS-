# Clarifications:
# White space counts
# Case sensitive

# Assumptions:
# The characters set is ASCII


def permutation_character_count(s1,s2):
    letters = [0 for i in range(129)]

    # Check if lengths are equal
    # Since this takes O(n) is a freebee optimization
    if len(s1) != len(s2):
        return False

    # Fill letters array with the count of characters found
    for i in s1:
        letters[ord(i)] += 1
    # Remove from letters array each character found
    for i in s2:
        letters[ord(i)] -= 1
        if letters [ord(i)] < 0:
            return False

    return True


