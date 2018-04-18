suitToSym={"h":"♥","d":"♦","c":"♣","s":"♠"}
Rankindex = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
def getSuitToSym():
    return suitToSym
def getRankindex():
    return Rankindex
class card:
    def __init__(self,rank,suit):
        if isinstance(rank,str):
            rank = rank.upper()
        if rank in Rankindex:
            self.rank = rank
        else:
            raise ValueError("rank not availible")
        if suit[0] in suitToSym.keys():
            self.suit = suit[0].lower()
        else:
            raise ValueError("suit not availible")
    def getSuit(self):
        return self.suit[0]
    def getRank(self):
        return self.rank
    def setSuit(self,suit):
        self.suit = suit[0]
    def setRank(self,rank):
        self.rank = rank
    def __lt__(self,other):
        return Rankindex.index(self.rank)<Rankindex.index(other.rank)
    def __gt__(self,other):
        return Rankindex.index(self.rank)>Rankindex.index(other.rank)
    def __eq__(self,other):
        return self.rank==other.rank
    def __str__(self):
        return(str(self.rank)+" of "+suitToSym[self.suit[0].lower()])