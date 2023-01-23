def isAnagram(s, t):
    if not (len(s) == len(t)):
        return False
    sTracker = {}
    tTracker = {}
    for i in range(len(s)):
        if (s[i] not in sTracker):
            sTracker[s[i]] = 1
        else:
            sTracker[s[i]] = sTracker[s[i]] + 1
        if (t[i] not in tTracker):
            tTracker[t[i]] = 1
        else:
            tTracker[t[i]] = tTracker[t[i]] + 1
    for i in sTracker:
        print("i: " + str(i) + " v: " + str(sTracker[i]))
    print()
    for i in tTracker:
        print("i: " + str(i) + " v: " + str(tTracker[i]))
    return tTracker == sTracker

def test():
    input1a = "anagram"
    input1b = "nagaram"
    print(str(isAnagram(input1a, input1b)))

test()
