# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    head = 1
    tail = n
    while head < tail
        mid = Integer((head + tail) / 2) # change to integer
        if is_bad_version(mid)
            tail = mid
        else
            head = mid + 1
        end
    end
    return head
end
