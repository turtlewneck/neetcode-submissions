class Solution {
    public boolean isAnagram(String s, String t) {
        char[] ss = s.toCharArray();
        char[] ts = t.toCharArray();

        Arrays.sort(ss);
        Arrays.sort(ts);

        if(Arrays.equals(ss, ts)) 
            return true;
        return false;
    }
}
