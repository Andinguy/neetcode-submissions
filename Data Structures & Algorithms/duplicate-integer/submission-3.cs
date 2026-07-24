public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> exists = new HashSet<int>();
        foreach (var n in nums){
            if (exists.Contains(n)){
                return true;
            }
            exists.Add(n);
        }
        return false;
    }
}