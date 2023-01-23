
def isPalindrome(s):
    # format string
    s = s.lower()
    s = [char for char in s if (char.islower() or char.isdigit())]
    # iterate through formatted string
    for i in range(len(s)//2):
        if not (s[i] == s[len(s) - i - 1]):
            return False
    return True

def isPalindrome2(s):
    # format string
    s = s.lower()
    s = [char for char in s if char.islower()]
    # create tracker stack
    tracker = []
    # iterate through formatted string
    for char in s:
        # if it is empty, add
        if (tracker == []):
            tracker.append(char)
        else:
            print(tracker[-1])
            if (char == tracker[-1]):
                tracker.pop()
            else:
                tracker.append(char)
    print(tracker)
    return tracker == []

def test():
    input1 = "A man. A plan. A canal. Panama"
    #input2 = "SDLF#@)( )"
    print(isPalindrome(input1))
    #print(isPalindrome(input2))
    return None

test()
