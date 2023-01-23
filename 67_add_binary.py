def addBinary(a: str, b: str) -> str:
    return self.toBinary(self.toBaseTen(a) + self.toBaseTen(b))

def toBaseTen(number: str) -> int:
    total = 0
    numberLength = len(number) - 1
    currentDigit = len(number) - 1
    while (currentDigit >= 0):
        currentValue = int(number[currentDigit])
        total += currentValue * (2**(numberLength-currentDigit))
        currentDigit -= 1
    return total

def toBinary(number: int) -> str:
    if number == 0:
        return "0"
    binaryRep = ""
    while (number > 0):
        remainder = number % 2
        binaryRep = str(remainder) + binaryRep
        number = number // 2
    return binaryRep

def test():
    print(toBaseTen("11010100101"))
    print(toBinary(2))

test()
