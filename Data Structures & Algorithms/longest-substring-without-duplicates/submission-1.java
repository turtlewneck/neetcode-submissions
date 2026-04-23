class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int l, r, max;
        l = r = max = 0;
        Set<Character> set = new HashSet<>();
        while(r<s.length()) {
            if(set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l += 1;
            }
            else {
                set.add(s.charAt(r));
                r += 1;
            }
            max = Math.max(max, set.size());
        }
        return max;
    }
}
