# check off
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    while pos1 < len(s1):
        found = False
        pos2 = 0
        while pos2 < len(s2):
            if s1[pos1] == alist[pos2]:
                alist[pos2] = None
                found = True
            else:
                pos2 += 1
        if found == False:
            return False
        pos1 += 1
    return True

# sort and compare
def anagramSolution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    pos = 0
    while pos < len(s1):
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            return False
    return True

# Solution 3: brute force
# Enumerate all permutation of s1 and compare with s2

# Count and compare
def anagramSolution4(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1
    
    j = 0
    while j < 26:
        if c1[j] == c2[j]:
            j += 1
        else:
            return False
    return True
        
print(anagramSolution4('pythonn', 'ttyphon'))
