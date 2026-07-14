public class Solution {
    public bool IsPalindrome(string s) {
        // How can we remove all non-alphanumeric characters
        // using char.IsLetterOrDigit()
        int start, end;
        end = s.Length - 1;
        s = s.ToLower();
        for (start = 0, end = s.Length - 1; start < s.Length && end >= 0; start++, end--) {
            while (start < s.Length && !char.IsLetterOrDigit(s[start])) start++;
            while (end >= 0 && !char.IsLetterOrDigit(s[end])) end--;
            if (end < 0 || start >= s.Length)
                break;
            Console.WriteLine($"start:{{{start}:{s[start]}}}, end:{{{end}:{s[end]}}}");
            if (s[start] != s[end]) {
                return false;
            }
        }
        return true;
    }
}
