def isValid(s):
    tracker = []
    for character in s:
        if (character == '(' or character == '[' or character == '{'):
            tracker.append(character)
        else:
            lastChar = tracker.pop()
            if (character == ')' and not lastChar == '('):
                return False
            elif (character == ']' and not lastChar == '['):
                return False
            elif (character == '}' and not lastChar == '{'):
                return False
    if (tracker == []):
        return True
    else:
        return False

def test():
    input1 = "()"
    input2 = "()[]{}"
    input3 = "(]"
    print(isValid(input1))
    print(isValid(input2))
    print(isValid(input3))

test()
