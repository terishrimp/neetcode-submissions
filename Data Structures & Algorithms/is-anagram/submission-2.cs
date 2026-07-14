public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sCharCount = new Dictionary<char, int>();
        Dictionary<char, int> tCharCount = new Dictionary<char, int>();
        if(s.Length != t.Length) return false;
        
        foreach (char c in s) {
            if (!sCharCount.ContainsKey(c))
                sCharCount.Add(c, 1);
            else
                sCharCount[c]++;
        }

        foreach (char c in t) {
            if (!tCharCount.ContainsKey(c))
                tCharCount.Add(c, 1);
            else
                tCharCount[c]++;
        }

        foreach (char key in sCharCount.Keys) {
            if (!tCharCount.ContainsKey(key))
                return false;
            else if (tCharCount[key] != sCharCount[key])
                return false;
        }

        return true;
    }
}
