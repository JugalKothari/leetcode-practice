class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q=[]
        d_q=[]
        size=len(senate)
        for i in range(len(senate)):
            if senate[i]=='R':
                r_q.append(i)
            else:
                d_q.append(i)
        j=0
        while(r_q and d_q):
            if r_q[j]<d_q[j]:
                d_q.pop(0)
                winner=r_q.pop(0)
                r_q.append(winner+size)
            else:
                r_q.pop(0)
                winner=d_q.pop(0)
                d_q.append(winner+size)
        if r_q:
            return "Radiant"
        else:
            return "Dire"
