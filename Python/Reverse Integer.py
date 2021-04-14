class Solution:
    def reverse(self, x: int) -> int:
        s= str(abs(x))
        
        s1= int(s[::-1])
    
        if(s1 >=2** 31 -1 or s1<= -2** 31):
            return 0
        elif x<0:
            return (-1 * s1)
        else:
            return s1
