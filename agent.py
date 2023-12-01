Agent_loc=[]
Agent_view=[['0']*5 for _ in range(5)]
Environement=[]
percived=[]
mov_check=False
moves=[]
pervious_dir='up'
wumpus_loc=False
shoot=False
shoot_cod=[]
Wumpus=[]
possible_wumpus=[]
safe_loc=[]
possible_pit=[]
up_percive=1
down_percive=1
left_percive=1
right_percive=1
current_percive=1

class Agent():
    def __init__(self):
        self.matrix=[['0']*5 for _ in range(5)]

    def getpercive(row,col):
        global up_percive
        global down_percive
        global left_percive
        global right_percive
        global current_percive
        global percived
        current_percive=Environement[row][col]


        if row-1>=0 and [row-1,col] not in percived:
            up_percive=Environement[row-1][col]
            percived.append([row-1,col])
        if row+1<5 and [row+1,col] not in percived:
            down_percive=Environement[row+1][col]
            percived.append([row+1,col])
        if col-1>=0 and [row,col-1] not in percived:
            left_percive=Environement[row][col-1]
            percived.append([row,col-1])
        if col+1<5 and [row,col+1] not in percived:
            right_percive=Environement[row][col+1]
            percived.append([row,col+1])
            
    def safe(row,col):
        global Agent_view
        global safe_loc
        if row-1>=0 and Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='W' and [row-1,col] not in safe_loc:
            if Agent_view[row-1][col]=='PP':
                possible_pit.remove([row-1,col])
            Agent_view[row-1][col]='SF'
            safe_loc.append([row-1,col])
        if row+1<5 and Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row-1][col]!='W' and [row+1,col] not in safe_loc:
            if Agent_view[row+1][col]=='PP':
                possible_pit.remove([row+1,col])
            Agent_view[row+1][col]='SF'
            safe_loc.append([row+1,col])
        if col-1>=0 and Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row-1][col]!='W' and [row,col-1] not in safe_loc:
            if Agent_view[row][col-1]=='PP':
                possible_pit.remove([row,col-1])
            Agent_view[row][col-1]='SF'
            safe_loc.append([row,col-1])
        if col+1<5 and Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row-1][col]!='W' and [row,col+1] not in safe_loc:
            if Agent_view[row][col+1]=='PP':
                possible_pit.remove([row,col+1])
            Agent_view[row][col+1]='SF'
            safe_loc.append([row,col+1])


    def OnlyBreezeMarkPit(row,col):
        global possible_pit
        if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF'):
            if Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='P' or Agent_view[row-1][col]=='PPW':
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='P'
            else:
                Agent_view[row-1][col]='PP'
                possible_pit.append([row-1,col])
        if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF'):
            if Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='P' or Agent_view[row+1][col]=='PPW':
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='P'
            else:
                Agent_view[row+1][col]='PP'
                possible_pit.append([row+1,col])
        if col-1>=0 and (Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF'):
            if Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='P' or Agent_view[row][col-1]=='PPW':
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='P'
            else:
                Agent_view[row][col-1]='PP'
                possible_pit.append([row,col-1])
        if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF'):
            if Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='P' or Agent_view[row][col+1]=='PPW':
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='P'
            else:
                Agent_view[row][col+1]='PP'
                possible_pit.append([row,col+1])

    def OnlyStinkMarkWumpus(row,col):
        global wumpus_loc
        global Wumpus
        if wumpus_loc==False:
            if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF') and wumpus_loc==False:
                if Agent_view[row-1][col]=='PW' or Agent_view[row-1][col]=='W' or Agent_view[row-1][col]=='PPW':
                    Agent_view[row-1][col]='W'
                    Wumpus.append([row-1,col])
                    wumpus_loc=True
                else:
                    if Agent_view[row-1][col]=='PP':
                        possible_pit.remove([row-1,col])
                    Agent_view[row-1][col]='PW'
            if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF') and wumpus_loc==False:
                if Agent_view[row+1][col]=='PW' or Agent_view[row+1][col]=='W' or Agent_view[row+1][col]=='PPW':
                    Agent_view[row+1][col]='W'
                    Wumpus.append([row+1,col])
                    wumpus_loc=True
                else:
                    if Agent_view[row+1][col]=='PP':
                        possible_pit.remove([row+1,col])
                    Agent_view[row+1][col]='PW'
            if col-1>=0 and (Agent_view[row][col-1]!='V'and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF') and wumpus_loc==False:
                if Agent_view[row][col-1]=='PW' or Agent_view[row][col-1]=='W' or Agent_view[row][col-1]=='PPW':
                    Agent_view[row][col-1]='W'
                    Wumpus.append([row,col-1])
                    wumpus_loc=True
                else:
                    if Agent_view[row][col-1]=='PP':
                        possible_pit.remove([row,col-1])
                    Agent_view[row][col-1]='PW'
            if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF') and wumpus_loc==False:
                if Agent_view[row][col+1]=='PW' or Agent_view[row][col+1]=='W' or Agent_view[row][col+1]=='PPW':
                    Agent_view[row][col+1]='W'
                    Wumpus.append([row,col+1])
                    wumpus_loc=True
                else:
                    if Agent_view[row][col+1]=='PP':
                        possible_pit.remove([row,col+1])
                    Agent_view[row][col+1]='PW'
        else:
            if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF' and Agent_view[row-1][col]!='W'):
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='SF'
            if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF' and Agent_view[row+1][col]!='W'):
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='SF'
            if col-1>=0 and (Agent_view[row][col-1]!='V'and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF' and Agent_view[row][col-1]!='W'):
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='SF'
            if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF' and Agent_view[row][col+1]!='W'):
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='SF'
    
    def BreezeStink(row,col):
        global wumpus_loc
        global possible_pit
        global Wumpus
        if row-1>=0 and (Agent_view[row-1][col]!='V' and Agent_view[row-1][col]!='A' and Agent_view[row-1][col]!='SF'):
            if Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='P':
                if Agent_view[row-1][col]=='PP':
                    possible_pit.remove([row-1,col])
                Agent_view[row-1][col]='P'
            elif Agent_view[row-1][col]=='PW' or Agent_view[row-1][col]=='W' or Agent_view[row-1][col]=='PPW' and wumpus_loc==False:
                Agent_view[row-1][col]='W'
                wumpus_loc=True
                Wumpus.append([row-1,col])
            elif wumpus_loc==False:
                Agent_view[row-1][col]='PPW'
            elif Agent_view[row-1][col]!='W':
                Agent_view[row-1][col]='PP'
                possible_pit.append([row-1,col])
        if row+1<5 and (Agent_view[row+1][col]!='V' and Agent_view[row+1][col]!='A' and Agent_view[row+1][col]!='SF'):
            if Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='P':
                if Agent_view[row+1][col]=='PP':
                    possible_pit.remove([row+1,col])
                Agent_view[row+1][col]='P'
            elif Agent_view[row+1][col]=='PW' or Agent_view[row+1][col]=='W' or Agent_view[row+1][col]=='PPW' and wumpus_loc==False:
                Agent_view[row+1][col]='W'
                wumpus_loc=True
                Wumpus.append([row+1,col])
            elif wumpus_loc==False:
                Agent_view[row+1][col]='PPW'
            elif Agent_view[row+1][col]!='W':
                Agent_view[row+1][col]='PP'
                possible_pit.append([row+1,col])
        if col-1>=0 and (Agent_view[row][col-1]!='V' and Agent_view[row][col-1]!='A' and Agent_view[row][col-1]!='SF'):
            if Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='P':
                if Agent_view[row][col-1]=='PP':
                    possible_pit.remove([row,col-1])
                Agent_view[row][col-1]='P'
            elif Agent_view[row][col-1]=='PW' or Agent_view[row][col-1]=='W' or Agent_view[row][col-1]=='PPW' and wumpus_loc==False:
                Agent_view[row][col-1]='W'
                wumpus_loc=True
                Wumpus.append([row,col-1])
            elif wumpus_loc==False:
                Agent_view[row][col-1]='PPW'
            elif Agent_view[row][col-1]!='W':
                Agent_view[row][col-1]='PP'
                possible_pit.append([row,col-1])
        if col+1<5 and (Agent_view[row][col+1]!='V' and Agent_view[row][col+1]!='A' and Agent_view[row][col+1]!='SF'):
            if Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='P':
                if Agent_view[row][col+1]=='PP':
                    possible_pit.remove([row,col+1])
                Agent_view[row][col+1]='P'
            elif Agent_view[row][col+1]=='PW' or Agent_view[row][col+1]=='W' or Agent_view[row][col+1]=='PPW' and wumpus_loc==False:
                Agent_view[row][col+1]='W'
                wumpus_loc=True
                Wumpus.append([row,col+1])
            elif wumpus_loc==False:
                Agent_view[row][col+1]='PPW'
            elif Agent_view[row][col+1]!='W':
                Agent_view[row][col+1]='PP'
                possible_pit.append([row,col+1])

    def travel_to_safe(row,col,temp_row,temp_col):
        global Agent_view
        global pervious_dir

        if(row>=temp_row):
            while(row>temp_row):
                row-=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='up'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_up')
                pervious_dir='up'
                Agent_view[row][col]=state
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='left'):
                        print("Move - forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right and Move Forward")
                    moves.append('move_left')
                    pervious_dir='left'
                    
                    Agent_view[row][col]=state
            else:
                while(col<temp_col):
                    col+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='right'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Left and Move Forward")
                    moves.append('move_right')
                    pervious_dir='right'
                    
                    Agent_view[row][col]=state

        else:
            while(row<temp_row):
                row+=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='down'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Left and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_down')
                pervious_dir='down'
                
                Agent_view[row][col]=state
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='left'):
                        print("Move - forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right and Move Forward")
                    moves.append('move_left')
                    pervious_dir='left'
                    
                    Agent_view[row][col]=state
            else:
                while(col<temp_col):
                    col+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='right'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right twice and Move Forward")
                    elif(pervious_dir=='up'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Left and Move Forward")
                    moves.append('move_right')
                    pervious_dir='right'
                    
                    Agent_view[row][col]=state

    def travel_to_safe_col(row,col,temp_row,temp_col):
        global Agent_view
        global pervious_dir

        if(col>=temp_col):
            while(col>temp_col):
                col-=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='left'):
                    print("Move - forward")
                elif(pervious_dir=='right'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right and Move Forward")
                moves.append('move_left')
                pervious_dir='left'

                
                Agent_view[row][col]=state
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='up'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_up')
                    pervious_dir='up'
                    
                    Agent_view[row][col]=state
            else:
                while(row<temp_row):
                    row+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='down'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Left and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_down')
                    pervious_dir='down'
                    
                    Agent_view[row][col]=state

        else:
            while(col<temp_col):
                col+=1
                state=Agent_view[row][col]
                Agent_view[row][col]='A'
                if(pervious_dir=='right'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Left and Move Forward")
                moves.append('move_right')
                pervious_dir='right'
                
                Agent_view[row][col]=state
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='up'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Right and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Left and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_up')
                    pervious_dir='up'
                    
                    Agent_view[row][col]=state
            else:
                while(row<temp_row):
                    row+=1
                    state=Agent_view[row][col]
                    Agent_view[row][col]='A'
                    if(pervious_dir=='down'):
                        print("Move - forward")
                    elif(pervious_dir=='left'):
                        print("Turn Left and Move Forward")
                    elif(pervious_dir=='right'):
                        print("Turn Right and Move Forward")
                    else:
                        print("Turn Right twice and Move Forward")
                    moves.append('move_down')
                    pervious_dir='down'
                    
                    Agent_view[row][col]=state

    def checkpath(row,col,temp_row,temp_col):
        global Agent_view
        correct=True
        if(row>=temp_row):
            while(row>temp_row):
                row-=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct=False
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(col<temp_col):
                    col+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        else:
            while(row<temp_row):
                row+=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct= False
            if(col>=temp_col):
                while(col>temp_col):
                    col-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(col<temp_col):
                    col+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        
    def colcheckpath(row,col,temp_row,temp_col):
        #check if there is a clear path from to a safe cell in the safe_loc array but travelling first to column and then to row
        global Agent_view
        correct=True
        if(col>=temp_col):
            while(col>temp_col):
                col-=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct=False
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(row<temp_row):
                    row+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        else:
            while(col<temp_col):
                col+=1
                if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                    correct= False
            if(row>=temp_row):
                while(row>temp_row):
                    row-=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            else:
                while(row<temp_row):
                    row+=1
                    if(Agent_view[row][col]=='W' or Agent_view[row][col]=='P' or Agent_view[row][col]=='PW' or Agent_view[row][col]=='PP' or Agent_view[row][col]=='PPW'):
                        correct= False
            return correct
        
    def unsafe(row,col):
        global pervious_dir
        global Agent_view
        if row-1>=0 and (Agent_view[row-1][col]=='PP' or Agent_view[row-1][col]=='PW'):
            row=row-1
            col=col
            print(row,col)
            if(pervious_dir=='up'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Right and Move Forward")
            elif(pervious_dir=='right'):
                print("Turn Left and Move Forward")
            else:
                print("Turn Right twice and Move Forward")
            moves.append('move_up')
            pervious_dir='up'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif col+1<5 and (Agent_view[row][col+1]=='PP' or Agent_view[row][col+1]=='PW'):
            col=col+1
            row=row
            print(row,col)
            if(pervious_dir=='right'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Right twice and Move Forward")
            elif(pervious_dir=='up'):
                print("Turn Right and Move Forward")
            else:
                print("Turn Left and Move Forward")
            moves.append('move_right')
            pervious_dir='right'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif row+1<5 and (Agent_view[row+1][col]=='PP' or Agent_view[row+1][col]=='PW'):
            row=row+1
            col=col
            print(row,col)
            if(pervious_dir=='down'):
                print("Move - forward")
            elif(pervious_dir=='left'):
                print("Turn Left and Move Forward")
            elif(pervious_dir=='right'):
                print("Turn Right and Move Forward")
            else:
                print("Turn Right twice and Move Forward")
            moves.append('move_down')
            pervious_dir='down'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]
        elif col-1>=0 and (Agent_view[row][col-1]=='PP' or Agent_view[row][col-1]=='PW'):
            row=row
            col=col-1
            print(row,col)
            if(pervious_dir=='left'):
                print("Move - forward")
            elif(pervious_dir=='right'):
                print("Turn Right twice and Move Forward")
            elif(pervious_dir=='up'):
                print("Turn Left and Move Forward")
            else:
                print("Turn Right and Move Forward")
            moves.append('move_left')
            pervious_dir='left'
            if Agent_view[row][col]=='PP':
                possible_pit.remove([row,col])
            return [row,col]

    def agentStart(self):
        counter=0
        temp_row=5
        temp_col=5
        crash_cou=0
        global possible_pit
        global safe_loc
        global pervious_dir
        global Agent_view
        global wumpus_loc
        global moves
        global mov_check
        global shoot
        global shoot_cod
        global up_percive,down_percive,left_percive,right_percive
        row=Agent_loc[0]
        col=Agent_loc[1]
        percived.append([row,col])
        Agent.getpercive(row,col)
        if(current_percive=='A'):
            Agent.safe(row,col)
        elif(current_percive=='AB'):
            Agent.OnlyBreezeMarkPit(row,col)
        elif(current_percive=='AS') and wumpus_loc==False:
            Agent.OnlyStinkMarkWumpus(row,col)
        elif(current_percive=='ASB'):
            Agent.BreezeStink(row,col)
        while(current_percive!='G' and current_percive!='GB' and current_percive!='GS' and current_percive!='PG' and current_percive!='GSB'
        and current_percive!='PGB' and current_percive!='GPS' and current_percive!='GPSB' and counter!=30):#if glod is found exit loop
            counter+=1
            Agent_view[row][col]='A'
            if(Environement[row][col]=='P' or Environement[row][col]=='PS' or Environement[row][col]=='PB' or Environement[row][col]=='PSB'):
                print("FELL IN TO A PIT ! GAME OVER")
                moves.append("game_over_pit")
                break
            if(Environement[row][col]=='W' and shoot==False):
                print("ATTACKED BY WUMPUS ! GAME OVER")
                moves.append("game_over_wumpus")
                break
            elif Environement[row][col]=='W' and [row,col] not in shoot_cod:
                print("ATTACKED BY WUMPUS ! GAME OVER")
                moves.append("game_over_wumpus")
                break
            if(up_percive!=1):
                if(up_percive=='B' or up_percive=='PB' or up_percive=='WB' or up_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row-1,col)
                elif(up_percive=='S' or up_percive=='PS' or up_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row-1,col)
                elif(up_percive=='SB' or up_percive=='PSB' or up_percive=='GSB'):
                    Agent.BreezeStink(row-1,col)
                else:
                    Agent.safe(row-1,col)
            if(down_percive!=1):
                if(down_percive=='B' or down_percive=='PB' or down_percive=='WB' or down_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row+1,col)
                elif(down_percive=='S' or down_percive=='PS' or down_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row+1,col)
                elif(down_percive=='SB' or down_percive=='PSB' or down_percive=='GSB'):
                    Agent.BreezeStink(row+1,col)
                else:
                    Agent.safe(row+1,col)
            if(left_percive!=1):
                if(left_percive=='B' or left_percive=='PB' or left_percive=='WB' or left_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row,col-1)
                elif(left_percive=='S' or left_percive=='PS' or left_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row,col-1)
                elif(left_percive=='SB' or left_percive=='PSB' or left_percive=='GSB'):
                    Agent.BreezeStink(row,col-1)
                else:
                    Agent.safe(row,col-1)
            if(right_percive!=1):
                if(right_percive=='B' or right_percive=='PB' or right_percive=='WB' or right_percive=='GB'):
                    Agent.OnlyBreezeMarkPit(row,col+1)
                elif(right_percive=='S' or right_percive=='PS' or right_percive=='GS') and wumpus_loc==False:
                    Agent.OnlyStinkMarkWumpus(row,col+1)
                elif(right_percive=='SB' or right_percive=='PSB' or right_percive=='GSB'):
                    Agent.BreezeStink(row,col+1)
                else:
                    Agent.safe(row,col+1)
            

            if(wumpus_loc):
                for i in range(5):
                    for j in range(5):
                        if Agent_view[i][j]=='PW':
                            Agent_view[i][j]='SF'
                            safe_loc.append([i,j])
                        elif Agent_view[i][j]=='PPW':
                            Agent_view[i][j]='PP'
                            possible_pit.append([i,j])
            else:
                wump_count=0
                for i in range(5):
                    for j in range(5):
                        if Agent_view[i][j]=='PW' or Agent_view[i][j]=='PPW':
                            wump_count+=1
                if(wump_count==1):
                    for i in range(5):
                        for j in range(5):
                            if Agent_view[i][j]=='PW' or Agent_view[i][j]=='PPW':
                                Agent_view[i][j]='W'
                                wumpus_loc=True
                                Wumpus.append([i,j])


            if(row-1>=0 and Agent_view[row-1][col]=='W' and shoot==False):
                shoot=True
                shoot_cod.append([row-1,col])
                print("SHOOT THE WUMPUS IN ",(row-1,col)," CELL")
                Agent_view[row-1][col]='SF'
                
                moves.append("shoot_up")
                safe_loc.append([row-1,col])
            elif(col+1<5 and Agent_view[row][col+1]=='W' and shoot==False):
                shoot=True
                shoot_cod.append([row,col+1])
                print("SHOOT THE WUMPUS IN ",(row,col+1)," CELL")
                Agent_view[row][col+1]='SF'
                
                moves.append("shoot_right")
                safe_loc.append([row,col+1])
            elif(row+1<5 and Agent_view[row+1][col]=='W' and shoot==False):
                shoot=True
                shoot_cod.append([row+1,col])
                print("SHOOT THE WUMPUS IN ",(row+1,col)," CELL")
                Agent_view[row+1][col]='SF'
                
                moves.append("shoot_down")
                safe_loc.append([row+1,col])
            elif(col-1>=0 and Agent_view[row][col-1]=='W'):
                shoot=True
                shoot_cod.append([row,col-1])
                print("SHOOT THE WUMPUS IN ",(row,col-1)," CELL")
                Agent_view[row][col-1]='SF'
                
                moves.append("shoot_left")
                safe_loc.append([row,col-1])
            Agent_view[row][col]='V'
            if(row-1>=0 and Agent_view[row-1][col]=='SF'):
                row=row-1
                col=col
                print(row,col)
                if(pervious_dir=='up'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_up')
                pervious_dir='up'
                mov_check=True
                safe_loc.remove([row,col])
            elif(col+1<5 and Agent_view[row][col+1]=='SF'):
                col=col+1
                row=row
                print(row,col)
                if(pervious_dir=='right'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Left and Move Forward")
                moves.append('move_right')
                pervious_dir='right'
                mov_check=True
                safe_loc.remove([row,col])
            elif(row+1<5 and Agent_view[row+1][col]=='SF'):
                row=row+1
                col=col
                print(row,col)
                if(pervious_dir=='down'):
                    print("Move - forward")
                elif(pervious_dir=='left'):
                    print("Turn Left and Move Forward")
                elif(pervious_dir=='right'):
                    print("Turn Right and Move Forward")
                else:
                    print("Turn Right twice and Move Forward")
                moves.append('move_down')
                pervious_dir='down'
                mov_check=True
                safe_loc.remove([row,col])
            elif(col-1>=0 and Agent_view[row][col-1]=='SF'):
                row=row
                col=col-1
                print(row,col)
                if(pervious_dir=='left'):
                    print("Move - forward")
                elif(pervious_dir=='right'):
                    print("Turn Right twice and Move Forward")
                elif(pervious_dir=='up'):
                    print("Turn Left and Move Forward")
                else:
                    print("Turn Right and Move Forward")
                moves.append('move_left')
                pervious_dir='left'
                safe_loc.remove([row,col])
                mov_check=True
            elif len(safe_loc)!=0:
                i=0
                while i<len(safe_loc):
                    temp_row=safe_loc[i][0]
                    temp_col=safe_loc[i][1]
                    clearpath=Agent.checkpath(row,col,temp_row, temp_col)
                    if(clearpath):
                        Agent.travel_to_safe(row,col,temp_row,temp_col)
                        row=temp_row
                        col=temp_col
                        safe_loc.remove([row,col])
                        mov_check=True
                        break
                    elif i==len(safe_loc)-1:
                        j=0
                        while j<len(safe_loc):
                            temp_row=safe_loc[j][0]
                            temp_col=safe_loc[j][1]
                            clearpath1=Agent.colcheckpath(row,col,temp_row,temp_col)
                            if(clearpath1):
                                Agent.travel_to_safe_col(row,col,temp_row,temp_col)
                                row=temp_row
                                col=temp_col
                                safe_loc.remove([row,col])
                                mov_check=True
                                break
                            elif j==len(safe_loc)-1:
                                break
                            else:
                                temp_col=5
                                temp_row=5
                                j+=1
                        break
                    else:
                        temp_col=5
                        temp_row=5
                        i+=1
            if (mov_check==False and len(possible_pit)!=0):
                new_loc=Agent.unsafe(row,col)
                if new_loc:
                    row=new_loc[0]
                    col=new_loc[1]
                else:
                    k=0
                    while k<len(possible_pit):
                        temp_row=possible_pit[k][0]
                        temp_col=possible_pit[k][1]
                        clearpath=Agent.colcheckpath(row,col,temp_row,temp_col)
                        if(clearpath):
                            Agent.travel_to_safe(row,col,temp_row,temp_col)
                            row=temp_row
                            col=temp_col
                            print("here row bn",temp_row,temp_col)
                            possible_pit.remove([row,col])
                            break
                        elif k==len(possible_pit)-1:
                            h=0
                            while h<len(possible_pit):
                                temp_row=possible_pit[h][0]
                                temp_col=possible_pit[h][1]
                                clearpath1=Agent.colcheckpath(row,col,temp_row,temp_col)
                                if(clearpath1):#similar
                                    Agent.travel_to_safe_col(row,col,temp_row,temp_col)
                                    row=temp_row
                                    col=temp_col
                                    print("here col bn",temp_row,temp_col)
                                    possible_pit.remove([row,col])
                                    break
                                elif h==len(possible_pit)-1:
                                    if(crash_cou==4):
                                        print(" Agent unable to locate next move")
                                        moves.append("crash")
                                        counter=30
                                    else:
                                        crash_cou+=1
                                        if(row-1>=0 and Agent_view[row-1][col]=='V'):
                                            row=row-1
                                            col=col
                                            print(row,col)
                                            if(pervious_dir=='up'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Right and Move Forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Left and Move Forward")
                                            else:
                                                print("Turn Right twice and Move Forward")
                                            moves.append('move_up')
                                            pervious_dir='up'
                                            mov_check=True
                                        elif(col+1<5 and Agent_view[row][col+1]=='V'):
                                            col=col+1
                                            row=row
                                            print(row,col)
                                            if(pervious_dir=='right'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Right twice and Move Forward")
                                            elif(pervious_dir=='up'):
                                                print("Turn Right and Move Forward")
                                            else:
                                                print("Turn Left and Move Forward")
                                            moves.append('move_right')
                                            pervious_dir='right'
                                            mov_check=True
                                        elif(row+1<5 and Agent_view[row+1][col]=='V'):
                                            row=row+1
                                            col=col
                                            print(row,col)
                                            if(pervious_dir=='down'):
                                                print("Move - forward")
                                            elif(pervious_dir=='left'):
                                                print("Turn Left and Move Forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Right and Move Forward")
                                            else:
                                                print("Turn Right twice and Move Forward")
                                            moves.append('move_down')
                                            pervious_dir='down'
                                            mov_check=True
                                        elif(col-1>=0 and Agent_view[row][col-1]=='V'):
                                            row=row
                                            col=col-1
                                            print(row,col)
                                            if(pervious_dir=='left'):
                                                print("Move - forward")
                                            elif(pervious_dir=='right'):
                                                print("Turn Right twice and Move Forward")
                                            elif(pervious_dir=='up'):
                                                print("Turn Left and Move Forward")
                                            else:
                                                print("Turn Right and Move Forward")
                                            moves.append('move_left')
                                            pervious_dir='left'
                                            mov_check=True

                                    break
                                else:
                                    temp_col=5
                                    temp_row=5
                                    h+=1
                            break
                        else:
                            temp_col=5
                            temp_row=5
                            k+=1
            elif mov_check==False:
                print("Agent unable to locate next move")
                moves.append("crash")
                counter=30

            mov_check=False
            up_percive=1
            down_percive=1
            right_percive=1
            left_percive=1
            Agent.getpercive(row,col)

        if(Environement[row][col]=="G" or Environement[row][col]=="GS" or Environement[row][col]=="GB" or Environement[row][col]=="GSB"):
            print("GOLD FOUND!!! AGENT WINS")
            moves.append("gold")
        else:
            print("AGENT LOSE :-[")
        return moves

    def agent_loc(agent_loc,original):
        global Agent_loc
        Agent_loc=agent_loc
        row=Agent_loc[0]
        col=Agent_loc[1]
        Agent_view[row][col]='A'
        global Environement
        Environement=original





