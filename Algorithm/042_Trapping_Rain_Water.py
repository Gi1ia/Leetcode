class Solution:
    def trap_two_pointers(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        # The idea is calculating water of each column
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max < right_max:
                # on index i, this column of water should be min(left_max, right_max) - height[i]
                res += left_max - height[i]
                i += 1
            else:
                res += right_max - height[j]
                j -= 1
        
        return res
