import random

#print ("Willkommen zu lordy_prods Kniffel")

#print ("Wieviele Mitspieler gibt es heute?(max 4)")


#spieler = input()
#if int(spieler) >4 : spieler = "4"
#print("also: " +spieler + " spielen heute mit.")
#players = int(spieler)


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
        self.kleine_straße = 0
        self.große_straße = 0
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
        print("kleine straße: " +str(self.kleine_straße))
        print("große straße: "+str(self.große_straße))
        print("kniffel: " +str(self.kniffel))
        print("chance: "+str(self.chance))

player_1_points = PointTable(1)
player_1_points.print_table()


saved_dice = []

class Dice:
    saved = False

    def __init__(self):
        pass
    

    def roll_die(self):
        if not Dice.saved: return random.randint(1,6)
    
    def save_die(self):
        Dice.saved = True

die_1 = Dice()
die_2 = Dice()
die_3 = Dice()
die_4 = Dice()
die_5 = Dice()

thrown_dice = {"W1":0,"W2":0,"W3":0,"W4":0,"W5":0}


def throw_dice():
        if thrown_dice["W1"] == 0:thrown_dice["W1"] = die_1.roll_die()
        if thrown_dice["W2"] == 0:thrown_dice["W2"] = die_2.roll_die()
        if thrown_dice["W3"] == 0:thrown_dice["W3"] = die_3.roll_die()
        if thrown_dice["W4"] == 0:thrown_dice["W4"] = die_4.roll_die()
        if thrown_dice["W5"] == 0:thrown_dice["W5"] = die_5.roll_die()
        return thrown_dice


def player_turn():
    count = 0
    for turn in range(0,3):
        count +=1
        inputs = input("würfeln?")
        print(throw_dice())
        hold = input("welche Würfel halten?(1,2,3,4 oder 5):")
        for number in hold:
            if number =="1": 
                die_1.save_die
                saved_dice.append(thrown_dice["W1"])
            else:thrown_dice ["W1"] = 0

            if number =="2": 
                die_2.save_die
                saved_dice.append(thrown_dice["W2"])
            else:thrown_dice ["W2"] = 0

            if number =="3": 
                die_3.save_die
                saved_dice.append(thrown_dice["W3"])
            else:thrown_dice ["W3"] = 0

            if number =="4":
                die_4.save_die
                saved_dice.append(thrown_dice["W4"])
            else:thrown_dice ["W4"] = 0

            if number =="5":
                die_5.save_die
                saved_dice.append(thrown_dice["W5"])
            else:thrown_dice ["W5"] = 0

    print(saved_dice)
player_turn()
