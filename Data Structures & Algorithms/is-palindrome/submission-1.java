class Solution {
    public boolean isPalindrome(String s) {
       String stripped = s.replaceAll("[^A-Za-z0-9]", "");
       stripped = stripped.toLowerCase();
       for (int i=0, j = stripped.length() - 1; i < j; i++, j--) {
            if(stripped.charAt(i) != stripped.charAt(j)) 
            return false;
       }
       return true;
    }
}
