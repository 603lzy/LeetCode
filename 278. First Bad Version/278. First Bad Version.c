// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

int firstBadVersion(int n) {
    int head = 1, tail = n, mid;
    while (head < tail){
        mid = head + (tail - head) / 2; // force to int = int + float
        if (isBadVersion(mid))
            tail = mid;
        else
            head = mid + 1;
    }
    return head;
}
