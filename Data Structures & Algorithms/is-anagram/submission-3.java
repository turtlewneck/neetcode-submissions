class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();
        for(Character x : s.toCharArray()) {
            if(mapS.containsKey(x)) {
                mapS.put(x, mapS.get(x)+1);
            }
            else {
                mapS.put(x, 1);
            }
        }
        for(Character x : t.toCharArray()) {
            if(mapT.containsKey(x)) {
                mapT.put(x, mapT.get(x)+1);
            }
            else {
                mapT.put(x, 1);
            }
        }
        return (mapS.equals(mapT)) ? true : false;
    }
}
