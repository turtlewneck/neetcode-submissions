class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        Map<String, Integer> map1 = new HashMap<String, Integer>();
        Map<String, Integer> map2 = new HashMap<String, Integer>();

        for (char c : s.toCharArray()) {
            String letter = String.valueOf(c);
            if (map1.containsKey(letter)) {
                map1.put(letter, map1.get(letter) + 1);
            }
            else {
                map1.put(String.valueOf(c), 1);
            }
        }
        for (char d : t.toCharArray()) {
            String letter = String.valueOf(d);
            if (map2.containsKey(letter)) {
                map2.put(letter, map2.get(letter) + 1);
            }
            else {
                map2.put(String.valueOf(d), 1);
            }
        }

        return map1.equals(map2);
    }
}
