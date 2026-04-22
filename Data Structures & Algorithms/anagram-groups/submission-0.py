class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dicts = dict()
        index = 0
        for m in strs:
            new_dict = dict()
            for n in m:
                if n in new_dict:
                    new_dict[n] += 1
                else:
                    new_dict[n] = 1
            key = tuple(sorted(new_dict.items()))
            if key in dicts:
                # write to given index
                res[dicts[key]].append(m)
            else:
                # give index for array
                dicts[key] = index
                res.append([m])
                index += 1



        
        #dictionary for each word
        print(dicts)
        print(res)
        return res