class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        sorted_pairs = sorted(count.items(),key=lambda pair: pair[1], reverse=True)
        return [num for num, freq in sorted_pairs[:k]]