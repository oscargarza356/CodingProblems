def composeRanges(nums):
    arr = []
    while nums:
        test = erode(nums)
        print(test[0])
        arr.append(test[0])
        nums = nums[test[1]:]
    return arr
    
    
def erode(nums): 
    lastnumber= 0
    arr = []
    firstNumber =0
    index= 0
    for i in range(len(nums)):
        if i == 0:
            firstNumber= nums[i]
            arr.append(str(nums[i]))
        elif nums[i] != nums[0] + i:
            break
        lastnumber = nums[i]
        index +=1
    if lastnumber == firstNumber:
        return (arr[0], index)
    else:
        arr[0] += "->"+str(lastnumber)
        return (arr[0], index)
