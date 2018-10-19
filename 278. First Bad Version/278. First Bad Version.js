/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        var head = 1, tail = n;
        while (head < tail){
            var mid = parseInt((tail + head) / 2);
            /**
             * same with python use parseInt cut the int part
             */
            if (isBadVersion(mid))
                tail = mid;
            else
                head = mid + 1;
        }
        return head;
    };
};
