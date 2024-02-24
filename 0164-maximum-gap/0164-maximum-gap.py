class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n < 2:
            return 0
        
        max_num = max(nums)
        min_num = min(nums)
        
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        num_buckets = (max_num - min_num) // bucket_size + 1
        
        buckets = [[float('inf'), -float('inf')] for _ in range(num_buckets)]
        
        for num in nums:
            index = (num - min_num) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
        
        max_gap = 0
        prev_max = min_num
        for bucket in buckets:
            if bucket[0] != float('inf'):
                max_gap = max(max_gap, bucket[0] - prev_max)
                prev_max = bucket[1]
        
        return max_gap
