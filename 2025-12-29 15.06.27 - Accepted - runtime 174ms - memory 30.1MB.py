class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        import bisect
        
        def longestNonDecreasing(nums):
            # LIS with non-decreasing (allow equal)
            tails = []
            for num in nums:
                pos = bisect.bisect_right(tails, num)
                if pos == len(tails):
                    tails.append(num)
                else:
                    tails[pos] = num
            return len(tails)
        
        total = 0
        for i in range(k):
            # Extract every k-th element starting from i
            subarray = [arr[j] for j in range(i, len(arr), k)]
            # Operations needed = length - longest non-decreasing subsequence
            total += len(subarray) - longestNonDecreasing(subarray)
        
        return total