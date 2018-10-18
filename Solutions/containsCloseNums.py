def containsCloseNums(nums, k):
    numDictionary = {}
    for i in range(len(nums)):
        if nums[i] not in numDictionary:
            numDictionary[nums[i]] = [i]
        else:
            numDictionary[nums[i]].append(i)
    
    for key in numDictionary:
        if len(numDictionary[key]) > 1:
            for i in range(1,len(numDictionary[key])):
                if numDictionary[key][i] - numDictionary[key][i-1] <= k:
                    return True
    
    return False
