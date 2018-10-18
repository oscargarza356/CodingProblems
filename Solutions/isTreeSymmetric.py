#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    rightArr = [] 
    leftArr = []
    
    if t == None:
        return True
    counter = 0
    if t.right != None:
        rightSideTraversal(t.right, rightArr, counter)
    if t.left != None:
        leftSideTraversal(t.left, leftArr, counter)
    
    return rightArr == leftArr    

def checkBalance(t):
    if t.left == None and t.right == None:
        return True
    elif t.left != None and t.right != None:
        return checkBalance(t.left) and checkBalance(t.right)
    else:
        return False
        
        
        
def rightSideTraversal(t, rightArr,counter):
    rightArr.append([t.value, counter])
    counter += 1
    if(t.left != None):
        rightSideTraversal(t.left, rightArr,counter)
    counter += 1
    if(t.right != None):
        rightSideTraversal(t.right, rightArr, counter)
    
def leftSideTraversal(t, leftArr,counter):   
    leftArr.append([t.value, counter])
    counter +=1
    if(t.right != None):
        leftSideTraversal(t.right, leftArr,counter)
    counter +=1
    if(t.left != None):
        leftSideTraversal(t.left, leftArr,counter)
    
        

        
    
    
