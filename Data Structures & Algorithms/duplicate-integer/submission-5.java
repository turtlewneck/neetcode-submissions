class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        Map<Integer, Integer> numMap  = new HashMap<>();
        for(int number : nums) {
            if(numMap.containsKey(number))
                return true;
            numMap.put(number, 0);
        }
        return false;
    }
}
