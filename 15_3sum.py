def threeSum(nums):

    results = set()
    positive, negative, zeros = [], [], []

    for num in nums:

        if num > 0:
            positive.append(num)
        elif num < 0:
            print(num)
            negative.append(num)
        else:
            zeros.append(num)

    print(positive)
    print(negative)
    print(zeros)

    if len(zeros) > 2:
        results.add(tuple([0, 0, 0]))

    pos_set = set(positive)
    neg_set = set(negative)

    if len(zeros) > 0:
        for num in pos_set:
            if -1*num in neg_set:
                results.add(tuple(sorted([-1*num, 0, num])))

    for i in range(len(positive)):
        for j in range(len(positive)):
            if not i == j:
                target = -1*(positive[i]+positive[j])
                if target in neg_set:
                    #if (i == 4):
                        #print("i: " + str(i))
                        #print("j: " + str(j))
                        #print()
                    results.add(tuple(sorted([target, positive[i], positive[j]])))

    for i in range(len(negative)):
        for j in range(len(negative)):
            if not i == j:
                target = -1*(negative[i]+negative[j])
                if target in pos_set:
                    results.add(tuple(sorted([target, negative[i], negative[j]])))

    return results

def test():
    input_1 = [-1, 0, 1, 2, -1, -4]
    res_1 = threeSum(input_1)
    print(res_1)

test()
