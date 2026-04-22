class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0 || nums.length ==1) {
            return false;
        }
        Set<Integer> set = new HashSet<Integer>();
        for (int n : nums) {
            if(set.contains(n)) {
                return true;
            }
            set.add(n);
        }
        return false;
    }
}
