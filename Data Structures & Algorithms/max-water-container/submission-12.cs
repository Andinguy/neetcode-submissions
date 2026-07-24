public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0;
        int r = heights.Length -1;
        int maxA = 0;
        while (l < r){
            var area = (r-l) * Math.Min(heights[r],heights[l]);
            maxA = Math.Max(area,maxA);
            if (heights[r] < heights[l]) {
                r--;
            }
            else l++;
        }
        return maxA;
    }
}
