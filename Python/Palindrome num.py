class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        z= str(x)
        
        rev = z[::-1]
        
        flag =0
        if(z == rev):
            flag=1
        
        if(flag==1):
            return True
        else:
            return False
