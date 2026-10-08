class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)
        hand.sort()

        for card in hand:
            if freq[card] != 0:
                for i in range(card, card + groupSize):
                    if freq[i] == 0:
                        return False
                    freq[i] -= 1
        
        return True
        

        
            





            
        