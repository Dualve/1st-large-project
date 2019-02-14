class food(object):
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

    def give_money(self):
        return self.cost

    def __str__(self):
        rep = "Name - " + self.name + ".\n Cost - " + str(self.cost) + ".\n"
        return rep


class buyer(object):
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def buy_a_food(self,fooder):
        
        if self.money > fooder.cost :
            self.money = self.money - fooder.cost 
        else:
            print("Мало денег.\n")
    
    def __str__(self):
        rep = "Name - " + self.name + ".\n Money - " + str(self.money) + ".\n"
        return rep

a = buyer("Киря",1000)
b = food("Бутер",50)
print(a)
print("\n")
print(b)
print("\n")
while True:
    n = int(input("1 - buy , 2 -exit\n"))
    if n == 1:
        a.buy_a_food(b)
        print(a)
    if n == 2:
        break
            
