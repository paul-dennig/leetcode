def twoSum(nums, target):
    compliments = {}
    for i, num in enumerate(nums):
        compliment = target-num
        if num in compliments:
            return [compliments[num], i]
        else:
            compliments[compliment] = i
    return compliments

def test():
    input1a = [2, 7, -1, 11]
    input1b = 9
    res1 = twoSum(input1a, input1b)
    #print(res1)

test()
