class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        if len(s)%2 != 0 or s[0] not in ['{','(','[']:
            return False 
        accepted = {'{':['}','{','[','('],'(':[')','{','[','('],'[':[']','{','[','(']}
        pastLetters = []
        for letter in s:
            if letter in ['{','(','[']:
                pastLetters.append(letter)
                continue
            
            if letter not in accepted[pastLetters[len(pastLetters)-1]]:
                return False
            elif letter == accepted[pastLetters[len(pastLetters)-1]][0]:
                pastLetters.pop()
        if pastLetters != []:
            return False
        return True
