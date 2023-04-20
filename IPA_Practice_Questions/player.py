class Player:
    def __init__(self,name,country, age, runs, wickets):
        self.name=name
        self.country=country
        self.age=age
        self.runs=runs
        self.wickets=wickets

class Team:
    def __init__(self, playerlist):
        self.playerlist=playerlist
    
    def minruns(self):
        min=self.playerlist[3]
        for i in self.playerlist:
            if i.runs < min:
                min=i.runs
                ob=i
        return ob

    def maxwickets(self):
        max=self.playerlist[4]
        for i in self.playerlist:
            if i.wickets > max:
                max=i.wickets
                ob=i
        return ob

n=int(input())
playerlist=[]
for i in range(n):
    name=input()
    country=input()
    age=int(input())
    runs=int(input())
    wickets=int(input()) 
    playerlist.append(Player(name, country, age, runs, wickets))
print(playerlist)
ob=Team(playerlist)
ob1=ob.minruns()
print(ob1.name)
print(ob1.runs)
print(ob1.country)
ob2=ob.maxwickets()
print(ob2.name)
print(ob2.wickets)
print(ob2.country)