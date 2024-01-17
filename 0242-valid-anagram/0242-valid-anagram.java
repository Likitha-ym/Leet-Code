class Solution {
    public boolean isAnagram(String s, String t) {
        int length1 = s.length();
        int length2 = t.length();
        if(length1 != length2)
        {
            return false;
        }
        int [] count=new int[26];
        for (char ch : s.toCharArray())
        {
            count[ch - 'a']++;
        }
        for (char ch : t.toCharArray())
        {
            count[ch - 'a']--;
        }
        for(int i=0; i<26; i++)
        {
            if(count[i] != 0)
            {
                return false;
            }
        }
        return true;
    }
}