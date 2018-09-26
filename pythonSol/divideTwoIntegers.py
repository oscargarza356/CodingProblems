class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count = 0
        dividend2 = abs(dividend)
        divisor2 = abs(divisor)
        
        while dividend2 >= divisor2:
            remainder = divisor2
            i=1
            while dividend2 >= remainder:
                dividend2 -= remainder
                count += i
                remainder <<= 1
                i <<= 1
                print(count)
        
        
        if (dividend < 0) != (divisor < 0):
            count = -count
        return min(max(-2147483648, count), 2147483647)
