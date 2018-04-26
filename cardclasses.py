suitToSym={"h":"♥","d":"♦","c":"♣","s":"♠"}
Rankindex = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
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
        return(str(self.rank)+str(suitToSym[self.suit[0].lower()]))
    
class hand():
    def __init__(self,cards = None):
        self.cards = [cards]
        try:
            if cards == None:
                self.cards=[]
        except:
            pass
        if isinstance(cards,list):
            self.cards = cards
        
    def suits(self):
        end ={}
        for i in self.cards:
            suit=i.getSuit()
            if suit in end.keys():
                end[suit]+=1
            else:
                end[suit]=1
        return end
    def ranks(self):
        end =[]
        for i in self.cards:
            end.append(i.getRank())
        return end
    def sort(self,by="rank"):
        if by == "rank":
            self.cards.sort()
        elif by == "suit":
            sorter = {}
            for i in self.cards:
                if i.getSuit() in sorter.keys():
                    sorter[i.getSuit()].append(i)
                else:
                    sorter[i.getSuit()]=[i]
            tempcards = []
            for key,value in sorter.items():
                value.sort()
                tempcards=tempcards+value
            self.cards=tempcards
    
    def __add__(self,other):
        return hand(self.cards+other.cards)
    def remove(self,card):
        if isinstance(card,int):
            return self-hand(self.cards[card])
        else:
            return self-hand(card)
    def __sub__(self,other):
        end = []
        for i in self.cards:
            if i not in other.cards:
                end.append(i)
        return hand(end)
        
    def __str__(self):
        end = []
        for i in self.cards:
            end.append(str(i))
        return ",".join(end)
#war turn
def turn(p1,p2,pe):
    card1 =p1.pop(0)
    card2 =p2.pop(0)
    pe.append(card1)
    pe.append(card2)
    if card1>card2:
        print("p1 win")
        for i in pe:
            p1.append(i)
        pe = []
    elif card1<card2:
        print("p2 win")
        for i in pe:
            p2.append(i)
        pe = []
    elif card1==card2:
        print("war")
        for i in range(0,3):
            pe.append(p1.pop(0))
            pe.append(p2.pop(0))
        result = turn(p1,p2,pe)
        p1=result[0]
        p2=result[1]
        pe=result[2]
    print(len(pe))
    return(p1,p2,pe)