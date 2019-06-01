class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        for i in range(len(rotateArray)):
            if i == 0:
                continue
            if rotateArray[i] < rotateArray[i - 1]:
                return rotateArray[i]
