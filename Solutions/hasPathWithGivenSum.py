#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    path = []
    left = False
    right = False
    #empty case
    if t == None:
        return False
    
    
    s = s - t.value
    
    if t.left != None: 
        left = hasPathWithGivenSum(t.left, s)
    
    if t.right != None:
        right = hasPathWithGivenSum(t.right, s)
    
    #leaf node
    if t.left == None and t.right == None:
        if s == 0:
            return True
        else:
            return False
        
    if right == True or left == True:
        return True
    else:
        return False
