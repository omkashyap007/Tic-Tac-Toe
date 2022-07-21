import numpy as n


def game():
    #The rules of the game.
    print("The tic tac toe is two player game . To enter the moves , use the numbers alloted to their respective places . \n")
    print("The moves alloted are given below.")
    print(n.array([int(i) for  i  in "123456789"]).reshape(3,3),"\n")
    print("The person who want to make the first move must write his or her name first , when asked")
    print("You are free to choose the signs you want to put.. first persons sign first and seconds at second...\n")
    
    
    #the game board of the game
    board=[int(i) for i in "000000000"]
    
    #the moves allowed for the persons
    moves_avail=[int(i) for i in "123456789"]
    
    #checking the moves to lie in these numbers
    check=[int(i) for i in "123456789"]
    
    #the ways a person can win
    win_chance=[[1,2,3] ,
                [1,3,2] ,
                [2,3,1] ,
                [2,1,3] ,
                [3,1,2] ,
                [3,2,1] ,
                
                [1,5,9] , 
                [1,9,5] ,
                [5,9,1] ,
                [5,1,9] ,
                [9,5,1] ,
                [9,1,5] ,
                
                [1,4,7] ,
                [1,7,4] ,
                [4,7,1] ,
                [4,1,7] ,
                [7,1,4] ,
                [7,4,1] ,
                
                [2,5,8] ,
                [2,8,5] ,
                [8,5,2] ,
                [8,2,5] ,
                [5,2,8] ,
                [5,8,2] ,
                
                
                [3,5,7] ,
                [3,7,5] ,
                [5,7,3] ,
                [5,3,7] ,
                [7,3,5] ,
                [7,5,3] ,
                
                [3,6,9] ,
                [3,9,6] ,
                [9,6,3] ,
                [9,3,6] ,
                [6,9,3] ,
                [6,3,9] ,
                
                [4,5,6] ,
                [4,6,5] ,
                [5,4,6] ,
                [5,6,4] ,
                [6,5,4] ,
                [6,4,5] ,
                
                [7,8,9] ,
                [7,9,8] ,
                [8,7,9] ,
                [8,9,7] ,
                [9,8,7] ,
                [9,7,8]
               ]
    
    #User entered data and constants
    p1,p2=map(str,input("Write the name of players seperated with commma-:").split(","))
    persons=[p1,p2]
    
    #the signs chosen by them.
    sign1 ,sign2= map(str,input("Tell the signs you going to use seperated with comma-:").split(","))
    signs=[sign1,sign2]
    
    #moves they make
    p1_set=[]
    p2_set=[]
    p_set=[p1_set,p2_set]
    
    #defining the move , iterating it later for another person
    i=0
    
    #defining the move that it is only allowed till the length of the board or simply 9.
    while i<len(board):
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        
        #asking for the person to make the move.
        move= int(input("Its " + str(persons[i%2]) +  " move"+ " :" ))


        #error handling1 , the move made by person is not already taken.
        if move not in moves_avail and move in check:
            print("The move is already taken")
            i-=1

        #error handling2 , the move made by the person exists . 
        if move not in moves_avail and move not in check:
            print("This is not applicable")
            i-=1
            
        if move in moves_avail and move in check:
            board[move-1]=signs[i%2]
            p_set[i%2].append(move)
            moves_avail.pop(moves_avail.index(move))
            
            print("\nThe game is going this\n",n.array(board).reshape(3,3),"\n")
            print("The moves available are",moves_avail,"\n")
                
            print("The moves done by "+ str(p1) + " are " , p_set[0])
            print("The moves done by "+ str(p2) + " are " , p_set[1])
        

                
        if len(p1_set)==3 and len(p2_set)==2:
            for k in range(0,len(win_chance)):
                if p_set[0]==win_chance[k]:
                    print("The winner is " + str(p1))
                    i=10
                    
        if len(p2_set)==3 and len(p1_set)==3:
            for k in range(0,len(win_chance)):
                if p_set[1]==win_chance[k]:
                    print("The winner is " + str(p2))
                    i=10
                    
        if len(p1_set)==4 and len(p2_set)==3:
            for k in range(0,len(win_chance)):
                if [p1_set[1] , p1_set[2] , p1_set[3]] == win_chance[k] or \
                   [p1_set[0] , p1_set[2] , p1_set[3]] == win_chance[k]:
                    print("The winner is " + str(p1))
                    i=10
                    
        if len(p1_set)==4 and len(p2_set)==4:
            for k in range(0,len(win_chance)):
                if [p2_set[1] , p2_set[2] , p2_set[3]] == win_chance[k] or \
                   [p2_set[0] , p2_set[2] , p2_set[3]] == win_chance[k] :
                    print("The winner is " +str(p2))
                    i=10
                    
        if len(p1_set)==5 and len(p2_set)==4:
            for k in range(0,len(win_chance)):
                if [p1_set[2] , p1_set[3] , p1_set[4]] == win_chance[k] or \
                   [p1_set[1] , p1_set[3] , p1_set[4]] == win_chance[k] or \
                   [p1_set[0] , p1_set[3] , p1_set[4]] == win_chance[k]:
                    print("The winner is " +str(p1))
        i+=1
game()