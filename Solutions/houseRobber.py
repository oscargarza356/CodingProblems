def houseRobber(nums):
    if not nums:
        return 0
    optimalPath = []
    optimalPath.append(0)
    optimalPath.append(nums[0])
    
    for i in range(2,len(nums)+1):
        if optimalPath[i-1] > optimalPath[i-2] + nums[i-1]:
            optimalPath.append(optimalPath[i-1])
        else:
            optimalPath.append(optimalPath[i-2] + nums[i-1])
    return optimalPath[-1]
