public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> uniqueInts = new HashSet<int>();

        foreach (int num in nums) {
            if (uniqueInts.Contains(num))
                return true;
            uniqueInts.Add(num);
        }
        return false;
    }
}