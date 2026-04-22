class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0 || nums.length == 1)
            return false;
        Map<Integer, Integer> numMap  = new HashMap<>();
        for(int number : nums) {
            if(numMap.containsKey(number))
                return true;
            numMap.put(number, 0);
        }
        return false;
    }
}
