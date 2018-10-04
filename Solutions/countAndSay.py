class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
      
            
        sequence = '1'
        subsequence = ''
        pastchar = 1
        for i in range(n-1):
            counter = 1
            for j in range(len(sequence)):
                if j == 0:
                    pastchar = sequence[j]
                    continue
                if pastchar == sequence[j]:
                    counter += 1
                else:
                    subsequence += str(counter)+pastchar
                    counter = 1
                pastchar = sequence[j]
                
            subsequence += str(counter)+pastchar
            sequence = subsequence
            subsequence = ''
        return sequence
