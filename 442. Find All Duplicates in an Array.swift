class Solution {
    func findDuplicates(_ nums: [Int]) -> [Int] {
        var rep: [Int] = []
        var num = nums
        num.sort()
        var i = 0
        while i < num.count - 1 {
            if num[i] == num[i + 1]{
                rep.append(num[i])
            }
            i += 1
        }
        return rep
    }
}
