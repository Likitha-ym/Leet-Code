public class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> charCount = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        int palindromeLength = 0;
        int oddCount = 0;
        
        for (int count : charCount.values()) {
            if (count % 2 == 0) {
                palindromeLength += count;
            } else {
                palindromeLength += count - 1;
                oddCount = 1;
            }
        }
        
        return palindromeLength + oddCount;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String s1 = "abccccdd";
        String s2 = "a";

        System.out.println(solution.longestPalindrome(s1)); 
        System.out.println(solution.longestPalindrome(s2));  
    }
}
