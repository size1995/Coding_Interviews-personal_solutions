#把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少次这样的操作
#1100 ->1011 -> 1100&1011=1000 ... ...
class Solution:
    def NumberOf1(self, n):
        counter=0
        n=n&0xffffffff
        while n:
            counter+=1
            n=n&(n-1)
        return counter
# class Solution:
#     def NumberOf1(self, n):
#         return sum([(n>>i) for i in range(32)])

