class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            delta = target - numbers[i]
            print("target: ",target, ", number[",i,"]: ",numbers[i], ", delta: ", delta)
            try:
                if numbers.index(delta) > i:
                    return [i+1, numbers.index(delta)+1]
            except:
                continue
        
