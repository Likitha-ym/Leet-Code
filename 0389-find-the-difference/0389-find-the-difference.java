public class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character, Integer> charCount = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()) {
            if (charCount.containsKey(c)) {
                int count = charCount.get(c);
                if (count == 1) {
                    charCount.remove(c);
                } else {
                    charCount.put(c, count - 1);
                }
            } else {
                return c; 
            }
        }
        
        return '\0'; 
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String s1 = "abcd", t1 = "abcde";
        String s2 = "", t2 = "y";

        System.out.println(solution.findTheDifference(s1, t1));  
        System.out.println(solution.findTheDifference(s2, t2));  
    }
}
