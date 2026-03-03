s1 =[1, 2, 3, 5, 11]
s2 =[9, 7, 3, 5, 2]


def duplicati(s1, s2):
    if len(s1) != len(set(s2)):
        return False
    return True

print(duplicati(s1, s2))             

