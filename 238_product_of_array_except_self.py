def productExceptSelf(nums):
    results = [1] * len(nums)
    temp = 1

    for i in range(len(nums)):
        results[i] = temp
        temp = temp * nums[i]

    temp = 1

    for i in range(len(nums)-1, -1, -1):
        results[i] *= temp
        temp *= nums[i]

    return results

def test():
    input1 = [1, 2, 3, 4]
    res1 = productExceptSelf(input1)
    print(input1)
    print(res1)

test()
