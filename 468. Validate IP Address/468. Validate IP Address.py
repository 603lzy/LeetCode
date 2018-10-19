class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            A = IP.split('.')
            if len(A) != 4:
                return "Neither"
            for i in A:
                if i.isdigit() == False: # not a number
                    return "Neither"
                elif int(i) > 255 or (i[0] == '0' and len(i) > 1):
                    return "Neither"
            return "IPv4"
        else:
            letter = set("abcdefABCDEF")
            B = IP.split(':')
            if len(B) != 8:
                return "Neither"
            for j in B:
                if len(j) > 4 or len(j) == 0:
                    return "Neither"
                for k in j:
                    if k.isdigit() == False and (k not in letter):
                        return "Neither"
            return "IPv6"
