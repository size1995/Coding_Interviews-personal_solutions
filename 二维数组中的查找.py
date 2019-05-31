class Solution:
    def Find(self, target, array):
        raw = len(array)
        col = len(array[0])
        if raw == 0 or col == 0:
            return False
        if target > array[raw - 1][col - 1] or target < array[0][0]:
            return False
        i = 0
        j = col - 1

        while True:
            if i > row - 1 or j < 0:
                return False
            elif array[i][j] == target:
                return True
            elif array[i][j] > target:
                j = j - 1
            elif array[i][j] < target:
                i = i + 1

