import random

print ("Willkommen zu lordy_prods Kniffel")

print ("Wieviele Mitspieler gibt es heute?(max 4)")


spieler = input()
if spieler == "exit":exit()
if int(spieler) >4 : spieler = "4"
print("also: " +spieler + " spielen heute mit.")
players = int(spieler)


class PointTable:
        
    def __init__(self,player):
        self.my_player = player
        self.all_points = 0
        self.points_teil_1 = 0
        self.points_teil_2 = 0
        self.points_einser = 0
        self.points_zweier = 0
        self.points_dreier = 0
        self.points_vierer = 0
        self.points_fünfer = 0
        self.points_sechser = 0

        self.dreier_pasch = 0
        self.vierer_pasch = 0
        self.full_house = 0
        self.kleine_strasse = 0
        self.große_strasse = 0
        self.kniffel = 0
        self.chance = 0



    def print_table(self):
        print("nur einser: " +str(self.points_einser))
        print("nur zweier: " +str(self.points_zweier))
        print("nur dreier: " +str(self.points_dreier))
        print("nur vierer: " +str(self.points_vierer))
        print("nur fünfer: " +str(self.points_fünfer))
        print("nur sechser: " + str(self.points_sechser))
        print("dreier pasch: " + str(self.dreier_pasch))
        print("vierer pasch: " + str(self.vierer_pasch))
        print("full house: " + str(self.full_house))
        print("kleine straße: " +str(self.kleine_strasse))
        print("große straße: "+str(self.große_strasse))
        print("kniffel: " +str(self.kniffel))
        print("chance: "+str(self.chance))

player_1_points = PointTable(1)
player_1_points.print_table()
player_2_points = PointTable(2)
player_2_points.print_table()
player_3_points = PointTable(3)
player_3_points.print_table()
player_4_points = PointTable(4)
player_4_points.print_table()




saved_dice = []

class Dice:
    saved = False

    def __init__(self):
        self.eyes = 0
    

    def roll_die(self):
        if Dice.saved == False: 
            eyes = random.randint(1,6)
        return eyes
    def save_die(self):
        Dice.saved = True

die_1 = Dice()
die_2 = Dice()
die_3 = Dice()
die_4 = Dice()
die_5 = Dice()

thrown_dice = {"W1":0,"W2":0,"W3":0,"W4":0,"W5":0}


def throw_dice(würfel):
        if 1 in würfel:thrown_dice["W1"] = die_1.roll_die()
        if 2 in würfel:thrown_dice["W2"] = die_2.roll_die()
        if 3 in würfel:thrown_dice["W3"] = die_3.roll_die()
        if 4 in würfel:thrown_dice["W4"] = die_4.roll_die()
        if 5 in würfel:thrown_dice["W5"] = die_5.roll_die()
        return thrown_dice



def player_turn(player):
    count = 0
    würfel = [1,2,3,4,5]
    for turn in range(0,3):
        count +=1
        inputs = input("würfeln?")
        if inputs == "exit":exit()
        throw_dice(würfel)
        print("dein wurf: "+"\n"
              "Würfel 1: "+str(thrown_dice["W1"])+"\n"+
              "Würfel 2: " +str(thrown_dice["W2"])+"\n"+
              "Würfel 3: " +str(thrown_dice["W3"])+"\n"+
              "Würfel 4: " +str(thrown_dice["W4"])+"\n"+
              "Würfel 5: " +str(thrown_dice["W5"])+"\n"
              
              )
        if count == 3:
            for wurf in würfel:
                saved_dice.append(wurf)
            break
        else:
            hold = input("welche Würfel halten?"+str(würfel)+":")
        if hold =="exit":exit()
        if "1" in hold and die_1.saved == False: 
            die_1.save_die
            saved_dice.append(thrown_dice["W1"])
            würfel.pop(würfel.index(1))

        if "2" in hold and die_2.saved == False: 
            die_2.save_die
            saved_dice.append(thrown_dice["W2"])
            würfel.pop(würfel.index(2))

        if "3" in hold and die_3.saved == False: 
            die_3.save_die
            saved_dice.append(thrown_dice["W3"])
            würfel.pop(würfel.index(3))

        if "4" in hold and die_4.saved == False:
            die_4.save_die
            saved_dice.append(thrown_dice["W4"])
            würfel.pop(würfel.index(4))

        if "5" in hold and die_5.saved == False:
            die_5.save_die
            saved_dice.append(thrown_dice["W5"])
            würfel.pop(würfel.index(5))
        if len(würfel) == 0:break   
    
    score_points(player)

def score_points(player):
    if player == 1:
        player_1_points.print_table()
    elif player == 2:
        player_2_points.print_table()
    elif player == 3:
        player_3_points.print_table()
    elif player == 4:
        player_4_points.print_table()
    
    print("dein gewerteter wurf: "+"\n"
          "Würfel 1: "+str(saved_dice[0])+"\n"+
          "Würfel 2: " +str(saved_dice[1])+"\n"+
          "Würfel 3: " +str(saved_dice[2])+"\n"+
          "Würfel 4: " +str(saved_dice[3])+"\n"+
          "Würfel 5: " +str(saved_dice[4])+"\n"
          )
    score_input = input("wo möchtest du dein Punkte eintragen: ")
    if score_input == "exit":exit()
    elif score_input =="einser":get_points(player,1)        
    elif score_input =="zweier":get_points(player,2)
    elif score_input =="dreier":get_points(player,3)
    elif score_input =="vierer":get_points(player,4)
    elif score_input =="fünfer":get_points(player,5)
    elif score_input =="sechser":get_points(player,6)
    elif score_input =="dreier pasch":get_points(player,33)
    elif score_input =="vierer pasch":get_points(player,44)
    elif score_input =="full house":get_points(player,25)
    elif score_input =="kleine straße":get_points(player,30)
    elif score_input =="große straße":get_points(player,40)
    elif score_input =="kniffel":get_points(player,50)    
    elif score_input == "chance":get_points(77)
    else:
        score_points(player)

def get_points(player,wich):
    table = player_1_points
    if player == 1:
        table = player_1_points
    elif player == 2:
        table =  player_2_points
    elif player == 3:
        table = player_3_points
    elif player == 4:
        table = player_4_points

    if wich == 1:
        if table.points_einser != 0: score_points(player)
        else : 
            x = saved_dice.count(1)
            table.points_einser = x
    elif wich == 2:
        if table.points_zweier != 0: score_points(player)
        else:
            x = saved_dice.count(2)
            table.points_zweier = x*2
    elif wich == 3:
        if table.points_dreier != 0: score_points(player)
        else:
            x = saved_dice.count(3)
            table.points_dreier = x*3
    elif wich == 4:
        if table.points_vierer != 0: score_points(player)
        else:
            x = saved_dice.count(4)
            table.points_vierer = x*4
    elif wich == 5:
        if table.points_fünfer != 0: score_points(player)
        else:
            x = saved_dice.count(5)
            table.points_fünfer = x*5
    elif wich == 6:
        if table.points_sechser != 0: score_points(player)
        else:
            x = saved_dice.count(6)
            table.points_sechser = x*6
    elif wich == 33:
        if table.dreier_pasch != 0: score_points(player)
        else:
            x = 0
            for point in saved_dice:
                x += point
            table.dreier_pasch = x
    elif wich == 44:
        if table.vierer_pasch != 0: score_points(player)
        else:
            x = 0
            for point in saved_dice:
                x += point
            table.vierer_pasch = x
    elif wich == 25:
        if table.full_house != 0: score_points(player)
        else:
            table.full_house = 25
    elif wich == 30:
        if table.kleine_strasse != 0: score_points(player)
        else:
            table.kleine_strasse = 30
    elif wich == 40:
        if table.große_strasse != 0: score_points(player)
        else:
            table.große_strasse = 30
    elif wich == 50:
        if table.kniffel != 0: score_points(player)
        else:
            table.kniffel = 50
    elif wich == 77:
        if table.chance != 0: score_points(player)
        else:
            x = 0
            for point in saved_dice:
                x += point
            table.chance = x
    table.print_table()        
for round in range (0,13,1):
    for player in range(0,players,1):
        player_turn(player)
        






