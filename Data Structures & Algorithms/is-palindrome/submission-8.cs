public class Solution {
    public bool IsPalindrome(string s) {
        // How can we remove all non-alphanumeric characters
        // using char.IsLetterOrDigit()
        int start = 0; 
        int end = s.Length - 1;
        while(start < end) {
            while (start < end && !char.IsLetterOrDigit(s[start])) start++;
            while (end > start && !char.IsLetterOrDigit(s[end])) end--;
            Console.WriteLine($"start:{{{start}:{s[start]}}}, end:{{{end}:{s[end]}}}");
            if (char.ToLower(s[start]) != char.ToLower(s[end])) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
