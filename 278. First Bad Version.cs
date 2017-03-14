/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        int head = 1, mid, tail = n;
        while (head < tail){
            mid = head + (tail - head) / 2; /*force to int = int + float*/
            if (IsBadVersion(mid)){
                tail = mid;
            } else {
                head = mid + 1;
            }
        }
        return head;
    }
}
