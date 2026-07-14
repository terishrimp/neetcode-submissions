public class Solution {
    public bool IsAnagram(string s, string t) {
        // Brute Force
        if (s.Length != t.Length)
            return false;

        var sortS = string.Concat(s.OrderBy(s => s));
        var sortT = string.Concat(t.OrderBy(t => t));
        return sortS == sortT;
    }
}
