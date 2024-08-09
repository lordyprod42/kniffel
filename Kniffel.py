import random

print ("willkommen zu lordy_prods kniffel")




spieler = input("wieviele mitspieler gibt es heute?(max 4):")
if spieler == "exit":exit()
if int(spieler) >4 : spieler = "4"
print("also: " +spieler + " spielen heute mit.")
players = int(spieler)

class pointtable:
        
    def __init__(self,player):
        self.my_player = player
        self.all_points = 0
        self.points_teil_1 = 0
        self.points_teil_2 = 0
        self.points_einser = -1
        self.points_zweier = -1
        self.points_dreier = -1
        self.points_vierer = -1
        self.points_fünfer = -1
        self.points_sechser = -1

        self.dreier_pasch = -1
        self.vierer_pasch = -1
        self.full_house = -1
        self.kleine_strasse = -1
        self.grosse_strasse = -1
        self.kniffel = -1
        self.chance = -1
        


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
        print("große straße: "+str(self.grosse_strasse))
        print("kniffel: " +str(self.kniffel))
        print("chance: "+str(self.chance))

    def add_teil_1(self):
        self.points_teil_1=self.points_einser+self.points_zweier+self.points_dreier+self.points_vierer+self.points_fünfer+self.points_sechser

    def give_bonus(self):
        if self.points_teil_1  >=63:
            self.points_teil_1 += 35
    def add_teil_2(self):
        self.points_teil_2=self.dreier_pasch+self.vierer_pasch+self.full_house+self.kleine_strasse+self.grosse_strasse+self.kniffel+self.chance
    def return_gesamt(self):
        self.all_points = self.points_teil_1+self.points_teil_2
        return self.all_points
    def reset_self(self):
        self.all_points = 0
        self.points_teil_1 = 0
        self.points_teil_2 = 0
        self.points_einser = -1
        self.points_zweier = -1
        self.points_dreier = -1
        self.points_vierer = -1
        self.points_fünfer = -1
        self.points_sechser = -1

        self.dreier_pasch = -1
        self.vierer_pasch = -1
        self.full_house = -1
        self.kleine_strasse = -1
        self.grosse_strasse = -1
        self.kniffel = -1
        self.chance = -1 

player_1_points = pointtable(1)
player_1_points.print_table()
player_2_points = pointtable(2)
player_3_points = pointtable(3)
player_4_points = pointtable(4)




saved_dice = []

class dice:

    def __init__(self):
        self.saved = False
        self.eyes = 0
    

    def roll_die(self):
        if self.saved == False: 
            self.eyes = random.randint(1,6)
        return self.eyes
    def save_die(self):
        self.saved = True
    def unsave_die(self):
        self.saved = False

die_1 = dice()
die_2 = dice()
die_3 = dice()
die_4 = dice()
die_5 = dice()


thrown_dice = {"w1":0,"w2":0,"w3":0,"w4":0,"w5":0}

  

def player_turn(player):
    count = 0
    würfel = [1,2,3,4,5]
    würfel_out = []
    for turn in range(0,3):
        count +=1
        input12 = input("spieler "+str(player)+" würfeln?")
        if input12 == "exit":exit()
        throw_dice(würfel)
        print("dein wurf: "+"\n"
              "würfel 1: "+str(thrown_dice["w1"])+"\n"+
              "würfel 2: " +str(thrown_dice["w2"])+"\n"+
              "würfel 3: " +str(thrown_dice["w3"])+"\n"+
              "würfel 4: " +str(thrown_dice["w4"])+"\n"+
              "würfel 5: " +str(thrown_dice["w5"])+"\n"
              
              )
        if count == 3:
            for wurf in würfel:
                if wurf == 1:saved_dice.append(thrown_dice["w1"])
                if wurf == 2:saved_dice.append(thrown_dice["w2"])
                if wurf == 3:saved_dice.append(thrown_dice["w3"])
                if wurf == 4:saved_dice.append(thrown_dice["w4"])
                if wurf == 5:saved_dice.append(thrown_dice["w5"])
        else:
            hold = input("welche würfel halten?"+str(würfel)+":")
        if hold =="exit":exit()
        print("debug "+str(hold))
        for number in hold:
            if number =="1":
                die_1.save_die()
                saved_dice.append(thrown_dice["w1"])
                würfel.pop(würfel.index(1))
                würfel_out.append(1)

            if number =="2":
                die_2.save_die
                saved_dice.append(thrown_dice["w2"])
                würfel.pop(würfel.index(2))
                würfel_out.append(2)

            if number =="3":
                die_3.save_die()
                saved_dice.append(thrown_dice["w3"])
                würfel.pop(würfel.index(3))
                würfel_out.append(3)
            if number =="4":
                die_4.save_die()
                saved_dice.append(thrown_dice["w4"])
                würfel.pop(würfel.index(4))
                würfel_out.append(4)
            if number =="5":
                die_5.save_die()
                saved_dice.append(thrown_dice["w5"])
                würfel.pop(würfel.index(5))
                würfel_out.append(5)
        if len(würfel) == 0:break
        if count == 2:
            input24 = input("weiter?")
            back=input("welche würfel wieder würfeln?"+str(würfel_out)+":")
            if back =="exit":exit()
            for number in back:
                if number =="1" and 1 in würfel_out:
                    die_1.unsave_die()
                    würfel_out.pop(würfel_out.index(1))
                    würfel.append(1)
                    saved_dice.pop(saved_dice.index(die_1.eyes))
                if number =="2" and 2 in würfel_out:
                    die_2.unsave_die()
                    würfel_out.pop(würfel_out.index(2))
                    würfel.append(2)
                    saved_dice.pop(saved_dice.index(die_2.eyes))
                if number =="3" and 3 in würfel_out:
                    die_3.unsave_die()
                    würfel_out.pop(würfel_out.index(1))
                    würfel.append(3)
                    saved_dice.pop(saved_dice.index(die_3.eyes))
                if number =="4" and 4 in würfel_out:
                    die_4.unsave_die()
                    würfel_out.pop(würfel_out.index(4))
                    würfel.append(4)
                    saved_dice.pop(saved_dice.index(die_4.eyes))
                if number =="5" and 5 in würfel_out:
                    die_5.unsave_die()
                    würfel_out.pop(würfel_out.index(5))
                    würfel.append(5)
                    print(die_5.saved,würfel)
                    saved_dice.pop(saved_dice.index(die_5.eyes))
            print("debug: "+str(saved_dice))



    input23=input("weiter?")
    score_points(player)

def score_points(player):
    table = player_1_points
    if player == 1:
        table = player_1_points
    elif player == 2:
        table =  player_2_points
    elif player == 3:
        table = player_3_points
    elif player == 4:
        table = player_4_points
    table.print_table()
    print("dein gewerteter wurf: "+"\n"
          "würfel 1: "+str(saved_dice[0])+"\n"+
          "würfel 2: " +str(saved_dice[1])+"\n"+
          "würfel 3: " +str(saved_dice[2])+"\n"+
          "würfel 4: " +str(saved_dice[3])+"\n"+
          "würfel 5: " +str(saved_dice[4])+"\n"
          )
    score_input = input("wo möchtest du dein punkte eintragen: ")
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
    elif score_input == "chance":get_points(player,77)
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
        if table.points_einser !=-1 : score_points(player)
        else : 
            x = saved_dice.count(1)
            table.points_einser = x
    elif wich == 2:
        if table.points_zweier != -1: score_points(player)
        else:
            x = saved_dice.count(2)
            table.points_zweier = x*2
    elif wich == 3:
        if table.points_dreier != -1: score_points(player)
        else:
            x = saved_dice.count(3)
            table.points_dreier = x*3
    elif wich == 4:
        if table.points_vierer != -1: score_points(player)
        else:
            x = saved_dice.count(4)
            table.points_vierer = x*4
    elif wich == 5:
        if table.points_fünfer != -1: score_points(player)
        else:
            x = saved_dice.count(5)
            table.points_fünfer = x*5
    elif wich == 6:
        if table.points_sechser != -1: score_points(player)
        else:
            x = saved_dice.count(6)
            table.points_sechser = x*6
    elif wich == 33:
        if table.dreier_pasch != -1: score_points(player)
        else:
            tempbool = false
            for dice in saved_dice:
             if saved_dice.count(dice) >=3:
                tempbool = true
                x = 0
                for point in saved_dice:
                    x += point
                table.dreier_pasch = x
            if tempbool == false:
                input7 = input("du hast kein dreier pasch, willst du 0 punkte, schreib 0:")
                if input7 == "0": table.dreier_pasch =0
                else:score_points(player)
            else: tempbool = false
    elif wich == 44:
        if table.vierer_pasch != -1: score_points(player)
        else:
            tempbool = false
            for dice in saved_dice:
             if saved_dice.count(dice) >=4:
                tempbool = true
                x = 0
                for point in saved_dice:
                    x += point
                table.vierer_pasch = x
            if tempbool == false:
                input7 = input("du hast kein vierer pasch, willst du 0 punkte, schreib 0:")
                if input7 == "0": table.vierer_pasch =0
                else:score_points(player)
            else: tempbool = false
    elif wich == 25:
        if table.full_house != -1: score_points(player)
        else:
            temp1=0
            temp2=0
            for dice in saved_dice:
                if saved_dice.count(dice) == 3:
                    temp1 = 3
                if saved_dice.count(dice) == 2:
                    temp2 = 2
            if temp1==3 and temp2==2: table.full_house=25
            else:
                input3 = input("du hast kein full house willst du 0 punkte, schreib 0:")
                if input3 =="0": table.full_house=0
                else:score_points(player)
    elif wich == 30:
        if table.kleine_strasse != -1: score_points(player)
        else:
            if 1 in saved_dice and 2 in saved_dice and 3 in saved_dice and 4 in saved_dice and 5 in saved_dice:
                table.kleine_strasse = 30
            else:
                input8 = input("du hast keine kleine straße willst du 0 punkte, schreib 0:")
                if input8 == 0: table.kleine_strasse =0
                else: score_points(player)
    elif wich == 40:
        if table.grosse_strasse != -1: score_points(player)
        else:
            if 6 in saved_dice and 2 in saved_dice and 3 in saved_dice and 4 in saved_dice and 5 in saved_dice:
                table.grosse_strasse = 30
            else:
                input9 = input("du hast keine große straße willst du 0 punkte, schreib 0:")
                if input9 == 0: table.grosse_strasse =0
                else: score_points(player)
    elif wich == 50:
        if table.kniffel != -1: score_points(player)
        else:
            x = 0
            nose = true
            for dice in saved_dice:
                if x == 0:
                    x=dice
                if x != dice:
                    nose = false
                    break
            if nose:
                table.kniffel = 50
            else:
                nose = true
                input10 = input("du hast kein kniffel willst du 0 punkte, schreib 0:")
                if input10 == 0: table.kniffel = 0
                else:score_points(player)
                        
    elif wich == 77:
        if table.chance != -1: score_points(player)
        else:
            x = 0
            for point in saved_dice:
                x += point
            table.chance = x
    table.print_table()
    sanother_input = input("weiter?")
    saved_dice.clear()
    thrown_dice = {"w1":0,"w2":0,"w3":0,"w4":0,"w5":0}

def throw_dice(würfel):
        if 1 in würfel:thrown_dice["w1"] = die_1.roll_die()
        if 2 in würfel:thrown_dice["w2"] = die_2.roll_die()
        if 3 in würfel:thrown_dice["w3"] = die_3.roll_die()
        if 4 in würfel:thrown_dice["w4"] = die_4.roll_die()
        if 5 in würfel:thrown_dice["w5"] = die_5.roll_die()
        return thrown_dice

def start_game():

    rounds = 1
    for round in range (0,rounds,1):
        for player in range(1,players+1,1):
            player_turn(player)
    end_game()
    
def end_game():
    points_pl_1=0
    points_pl_2=0
    points_pl_3=0
    points_pl_4=0

    table = player_1_points
    for player in range(1,players+1,1):
        if player == 1:
            table = player_1_points
        elif player == 2:
            table =  player_2_points
        elif player == 3:
            table = player_3_points
        elif player == 4:
            table = player_4_points
        table.add_teil_1()
        table.give_bonus()
        table.add_teil_2()
        points = table.return_gesamt()
        table.print_table()
        if player == 1:
            points_pl_1= points
        elif player == 2:
            points_pl_2= points
        elif player == 3:
            points_pl_3 = points
        elif player == 4:
            points_pl_4= points
        table.reset_self()

    print("player 1: "+str(points_pl_1))
    print("player 2: "+str(points_pl_2))
    print("player 3: "+str(points_pl_3))   
    print("player 4: "+str(points_pl_4))
    input25 = input("neue runde?(ja/nein)")
    if input25 =="ja":start_game()
    else: exit()






start_game()
