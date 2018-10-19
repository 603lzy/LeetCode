/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int head = 1, tail = n, mid;
        while (head < tail){
            mid = head + (tail - head) / 2; /* force to int = int + float*/
            if (isBadVersion(mid)){
                tail = mid;
            } else{
                head = mid + 1;
            }
        }
        return head;
    }
}
