public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        Array.Sort(nums);
        IList<int> disnum = new List<int>();  //using IList to get a list for there is in the function
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                disnum.Add(nums[i]);
            }
        }
        return disnum;
    }
}
