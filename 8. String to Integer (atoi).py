class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        a = list(str)
        while len(a) >= 1:
            if a[0] == " ":
                del a[0]
            else:
                break
        if a == " ":
            return 0
        if len(a) == 0:
            return 0
        elif len(a) == 1:
            if (ord(a[0]) <= ord('9')) and (ord(a[0]) >= ord('0')):
                return int(a[0])
            else:
                return 0
        elif len(a) == 2:
            if (a[0] == "-") and (ord(a[1]) <= ord('9')) and (ord(a[1]) >= ord('0')):
                return int(str)
            elif (a[0] == "+") and (ord(a[1]) <= ord('9')) and (ord(a[1]) >= ord('0')):
                return int(a[1])
            elif (ord(a[0]) <= ord('9')) and (ord(a[0]) >= ord('0')):
                if (ord(a[1]) <= ord('9')) and (ord(a[1]) >= ord('0')):
                    return int(str)
                else:
                    return int(a[0])
            else:
                return 0
        else:
            b = []
            strb = ""
            if (a[0] == "-") and (ord(a[1]) <= ord('9')) and (ord(a[1]) >= ord('0')):
                for i in range(1, len(a)):
                    if (ord(a[i]) <= ord('9')) and (ord(a[i]) >= ord('0')):
                        b.append(a[i])
                        strb = "".join(b)
                    else:
                        break
                if -(int(strb)) <= -2147483648:
                    return -2147483648
                else:
                    return -(int(strb))
            elif (a[0] == "+") and (ord(a[1]) <= ord('9')) and (ord(a[1]) >= ord('0')):
                for i in range(1, len(a)):
                    if (ord(a[i]) <= ord('9')) and (ord(a[i]) >= ord('0')):
                        b.append(a[i])
                        strb = "".join(b)
                    else:
                        break
                if int(strb) >= 2147483647:
                    return 2147483647
                else:
                    return (int(strb))
            elif (ord(a[0]) <= ord('9')) and (ord(a[0]) >= ord('0')):
                for i in range(0, len(a)):
                    if (ord(a[i]) <= ord('9')) and (ord(a[i]) >= ord('0')):
                        b.append(a[i])
                        strb = "".join(b)
                    else:
                        break
                if int(strb) >= 2147483647:
                    return 2147483647
                else:
                    return (int(strb))
            else:
                return 0
