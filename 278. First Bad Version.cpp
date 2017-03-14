// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int head = 1, tail = n;
        int mid;
        while (head < tail){
            mid = head + (tail - head) / 2; // can not be mid = (tail + head) / 2, this can force transform it to int
            if (isBadVersion(mid))
                tail = mid;
            else{
                head = mid + 1;
            }
        }
        return head;
    }
};
