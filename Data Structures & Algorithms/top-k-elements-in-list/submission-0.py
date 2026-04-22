class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = dict()
        for i in nums:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
        print('occ - ', occ)
        sort_occ = sorted(occ.items(), key=lambda item: item[1], reverse=True)
        print('soirted occ - ', sort_occ)
        res = []
        for i in range(k):
            res.append(sort_occ[i][0])

        return res