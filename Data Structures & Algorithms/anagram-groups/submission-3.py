class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(tuple(sorted(strs[0])))
        dict1=OrderedDict()

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            # print(key)
            if key in dict1:
                dict1[key].append(strs[i])
            else:
                dict1[key] = [strs[i]]
        return list(dict1.values())
