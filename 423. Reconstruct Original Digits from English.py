class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # construct hash table for the original string
        hs = {}
        for i in set(s):
            hs[i] = s.count(i)
        # construct output hash table
        ho = {}
        if "z" in hs: #0
            ho[0] = hs["z"]
            hs["e"] -= hs["z"] #test hs["e"] != 0 when use
            hs["r"] -= hs["z"]
            hs["o"] -= hs["z"]

        if "w" in hs: #2
            ho[2] = hs["w"]
            hs["t"] -= hs["w"]
            hs["o"] -= hs["w"]

        if "u" in hs: #4
            ho[4] = hs["u"]
            hs['f'] -= hs["u"]
            hs["o"] -= hs["u"]
            hs["r"] -= hs["u"]

        if "x" in hs: #6
            ho[6] = hs["x"]
            hs["i"] -= hs["x"]
            hs["s"] -= hs["x"]

        if "g" in hs: #8
            ho[8] = hs["g"]
            hs["e"] -= hs["g"]
            hs["i"] -= hs["g"]
            hs["h"] -= hs["g"]
            hs["t"] -= hs["g"]

        if "o" in hs and hs["o"] != 0: #1
            ho[1] = hs["o"]
            hs["n"] -= hs["o"]
            hs["e"] -= hs["o"]

        if "h" in hs and hs["h"] != 0: #3
            ho[3] = hs["h"]
            hs["t"] -= hs["h"]
            hs["r"] -= hs["h"]
            hs["e"] -= (hs["h"] * 2)

        if "s" in hs and hs["s"] != 0: #7
            ho[7] = hs["s"]
            hs["e"] -= (hs["s"] * 2)
            hs["v"] -= hs["s"]
            hs["n"] -= hs["s"]

        if "v" in hs and hs["v"] != 0: #5
            ho[5] = hs["v"]

        if "n" in hs and hs["n"] != 0: #9
            ho[9] = hs["n"] // 2

        p = ""
        for i in range(10):
            if i in ho:
                p += (str(i) * ho[i])

        return p
