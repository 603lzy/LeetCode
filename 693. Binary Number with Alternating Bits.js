/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    var nStr = n.toString(2);
    for (var i = 1; i < nStr.length; i++) {
        if (nStr[i] === nStr[i - 1]) {
            return false;
        };  
    };
    return true;
};
