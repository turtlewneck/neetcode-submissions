class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0 || nums.length == 1)
            return false;
        Set<Integer> numSet  = new HashSet<>();
        for(int number : nums) {
            if(numSet.contains(number))
                return true;
            numSet.add(number);
        }
        return false;
    }
}
