public class Solution {
    public bool IsPalindrome(string s) {
        // How can we remove all non-alphanumeric characters
        // using char.IsLetterOrDigit()
        int start, end;
        end = s.Length - 1;
        s = s.ToLower();
        string trimmedS = "";
        for (int i = 0; i < s.Length; i++)
            if (char.IsLetterOrDigit(s[i]))
                trimmedS += s[i];
        Console.WriteLine(trimmedS);
        for (start = 0, end = trimmedS.Length - 1; start < trimmedS.Length && end >= 0;
             start++, end--) {
            if (end < 0 || start >= trimmedS.Length)
                break;
            if (trimmedS[start] != trimmedS[end]) {
                return false;
            }
        }
        return true;
    }
}
