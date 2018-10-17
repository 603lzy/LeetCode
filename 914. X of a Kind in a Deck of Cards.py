class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deck.sort()
        deckDict = {}
        deckSet = set(deck)
        for n in deckSet:
            deckDict[n] = deck.count(n)
        X = 2
        while X <= max(deckDict.values()):
            if all(x % X == 0 for x in deckDict.values()):
                return True
            X = X + 1
        return False
                
            
        
