from random import randint
from os import system

Player = "😎"
Final_Boss = "💀"
Boss1 = "🤩"
Boss2 = "😤"
Shop = "💰"
Shop1 = "💰"
Shop2 = "💰"
Master_Roshi = "🥸 "
Monster = "😡"
y = 19
x = 14
monstery = 9
monsterx = 10

#---------------------------------------------------------------------
def Monster_Movement(monstery,monsterx):
    Index1 = randint(1,3)
    Index2 = randint(1,3)
    if Index1 == 1:
        if monstery < 12:
            monstery+=1
        else:
            pass
    if Index1 == 2:
        if monstery > 7:
            monstery-=1
        else: 
            pass 
    if Index2 == 1: 
        if monsterx < 13:
            monsterx+=1
        else:
            pass 
    if Index2 == 2:
        if monsterx > 0:
            monsterx-=1
        else:
            pass 
    return monstery,monsterx

#---------------------------------------------------------------------
def Monster_Encounter():
    Monster_Chance = randint(0,50)
    return Monster_Chance

#---------------------------------------------------------------------
def Player_Movement(Move,y,x):
    Move = Move.strip()
    system("clear")
    if Move == "haut":
        if y != 0:       
            y -= 1  
        else:
            print("Vous ne pouvez pas aller en haut")
            pass        

    if Move == "bas":
        if y < 19:            
            y += 1    
        else:
            print("Vous ne pouvez pas aller en bas")        
            pass

    if Move == "gauche":
        if x != 0:            
            x -= 1     
        else:
            print("Vous ne pouvez pas aller a gauche")
            pass

    if Move == "droite":
        if x <14:            
            x += 1        
        else:
            print("Vous ne pouvez pas aller a droite")
            pass    
    return y,x 

#---------------------------------------------------------------------
def world_map(y,x):
    i = 0
    p = 0
    World_Map = []
    Map = []
    for i in range (18):
        L = []
        L1 = []
        for p in range (15):
            L.append("|__|")
            p += 1 
        i += 1
        Map.append(L)
        if i == 13 or i == 6:
            Map.append(L1)
    Map[y][x] = f"|{Player}|"
    Map[16][13] = f"|{Shop}|"
    Map[13][3] = f"|{Shop1}|"
    Map[3][10] = f"|{Shop2}|"
    Map[15][0] = f"|{Boss1}|"
    Map[7][14] = f"|{Boss2}|"
    Map[0][0] = f"|{Final_Boss}|" 
    Map[2][6] = f"|{Master_Roshi}|" 
    Map[monstery][monsterx] = f"|{Monster}|"
    a = 0
    for a in range (len(Map)):
        World_Map.append(Map[a])
        print(*World_Map[a])
        a += 1
    return Map


monstery,monsterx = Monster_Movement(monstery,monsterx)
Map = world_map(y,x)