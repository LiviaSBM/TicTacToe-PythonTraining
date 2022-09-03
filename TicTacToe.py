#!/usr/bin/env python
# coding: utf-8

# In[5]:


def parametrosdousuario():

    #Module for asking which mark the player 1 wants to use: X or O    
    #Perguntar qual marcador o usuario quer
    player1 = input("Player 1, select either X or O: ")
    while player1 not in ["X","x","o","O"]:
         player1 = input("I'm sorry, this character is not valir. Please, select either X or O: ")
    if player1=="X":
        print("Player 1 is now X and Player 2 is O")
        player2="O"
    else:
        print("Player 1 is now O and Player 2 is X")
        player2="X"
    return player1,player2

player1, player2 = parametrosdousuario()


# In[4]:

#Module for rolling the game
def jogadas(player1,player2):
    #The variable below prints the game pattern with the numbered positions for the player to choose
    pattern = "1|2|3\n-----\n4|5|6\n-----\n7|8|9"
    print(pattern)
    positionsavailable = "123456789"
    winner=True
    
    #Variables for recording each player's move
    row1=0
    row2=0
    row3=0
    column1=0
    column2=0
    column3=0
    cross1=0
    cross2=0
    lista=[row1,row2,row3,column1,column2,column3,cross1,cross2]
    
    while winner:
        markplayer1=input("\nPlayer 1, Choose one position to mark: ")
        while markplayer1 not in positionsavailable:
            markplayer1 = input("I'm sorry, this position isn't avaliable. Please choose an available position: ")
        pattern = pattern.replace(markplayer1,player1)
        positionsavailable = positionsavailable.replace(markplayer1,"")
        print(f"Here's the updated board:\n{pattern}\n")
        
        #Every move of Player 1 adds up 1 to each row/column/cross variable
        if markplayer1=="1":
            row1 += 1
            column1 += 1
            cross1 += 1
        elif markplayer1=="2":
            row1 += 1
            column2 += 1
        elif markplayer1=="3":
            row1 += 1
            column3 += 1
            cross2 += 1
        elif markplayer1=="4":
            row2 += 1
            column1 += 1
        elif markplayer1=="5":
            row2 += 1
            column2 += 1
            cross1 += 1
            cross2 += 1
        elif markplayer1=="6":
            row2 += 1
            column3 += 1
        elif markplayer1=="7":
            row3 += 1
            column1 += 1
            cross2 += 1
        elif markplayer1=="8":
            row3 += 1
            column2 += 1
        elif markplayer1=="9":
            row3 += 1
            column3 += 1
            cross1 += 1
        lista=[row1,row2,row3,column1,column2,column3,cross1,cross2]
        
        #Condition for defining P1 as winner: as soon as each variable reaches 3,
        #it means P1 is the winner
        if 3 in lista:
            return "player 1 is the winner"
            winner=False
        elif positionsavailable=="":
            return "No winners today :)"        
        
        #P2 turn
        markplayer2=input("\nPlayer 2, Choose one position to mark: ")
        while markplayer2 not in positionsavailable:
            markplayer2 = input("I'm sorry, this position isn't avaliable. Please choose an available position: ")
        pattern = pattern.replace(markplayer2,player2)
        positionsavailable = positionsavailable.replace(markplayer2,"")
        print(f"Here's the updated board:\n{pattern}\n")
        
        #Differently from P1, each P2 move adds up +5 to each variable
        #Thus, as soon as any variable reaches 15, it means P2 wins
        if markplayer2=="1":
            row1 += 5
            column1 += 5
            cross1 += 5
        elif markplayer2=="2":
            row1 += 5
            column2 += 5
        elif markplayer2=="3":
            row1 += 5
            column3 += 5
            cross2 += 5
        elif markplayer2=="4":
            row2 += 5
            column1 += 5
        elif markplayer2=="5":
            row2 += 5
            column2 += 5
            cross1 += 5
            cross2 += 5
        elif markplayer2=="6":
            row2 += 5
            column3 += 5
        elif markplayer2=="7":
            row3 += 5
            column1 += 5
            cross2 += 5
        elif markplayer2=="8":
            row3 += 5
            column2 += 5
        elif markplayer2=="9":
            row3 += 5
            column3 += 5
            cross1 += 5     
        
        lista=[row1,row2,row3,column1,column2,column3,cross1,cross2]

        if 15 in lista:
            return "player 2 is the winner"
            winner=False
        elif positionsavailable=="":
            return "No winners today :)"
    
jogadas(player1,player2)


# In[ ]:




