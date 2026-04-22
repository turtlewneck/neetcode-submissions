class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # last index will always be 0
        res = [0] * len(temperatures)

        for i in range(len(temperatures)): #0 -> 6
            
            if len(stack) > 0:
                while stack[len(stack)-1][0] < temperatures[i]:
                    top = stack.pop()
                    print('stack:',stack,'top:',top,'top[0]:',top[0],'top[1]:',top[1] ,'i:',i)
                    res[top[1]] = i - top[1]
                    if not stack:
                        break
            stack.append((temperatures[i], i))
        
        print(temperatures,'\n',stack,'\n', res)
        return res