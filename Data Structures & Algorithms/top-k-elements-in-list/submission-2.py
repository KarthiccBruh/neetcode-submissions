class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for c in nums:
            freq[c]=freq.get(c,0)+1
        bucket=[[] for _ in range(max(freq.values()))]
        for num,times in freq.items():
            bucket[times-1].append(num)
        res=[]
        for c in range(len(bucket)-1,-1,-1):
            for d in bucket[c]:
                res.append(d)
                if k==len(res):
                    return res