class Solution:
    def Fibonacci(self,n):
        a0,a1=0,1
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n+1):
            a3=a0+a1
            a0=a1
            a1=a3
        return a1