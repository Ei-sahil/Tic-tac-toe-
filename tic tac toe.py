from tkinter import *
import random

global HC_player 
global l1
global b1
global b2

def next_turn(row,column):
 global HC_player
 if mode=="HH":
     global player
     if buttons[row][column]['text']=="" and check_winner() is False:
         if player==players[0]:
             buttons[row][column]['text']=player
             if check_winner() is False:
              player=players[1]
              status_label.config(text=f"{player}'s Turn")
             elif check_winner() is True:
                 status_label.config(text=(players[0]+" wins"))
             elif check_winner()=="Tie":
                 status_label.config(text="Tie!")
         else:
             buttons[row][column]['text']=player
             if check_winner() is False:
              player=players[0]
              status_label.config(text=f"{player}'s Turn")
             elif check_winner() is True:
                 status_label.config(text=(players[1]+" wins"))
             elif check_winner()=="Tie":
                 status_label.config(text="Tie!")
 else:
     if buttons[row][column]['text']=="" and check_winner() is False:
          buttons[row][column]['text']=HC_player
          if check_winner() is False:
              HC_player=players[1] #move computer will move 
              empty_cells = []
              for row in range(3):
                 for column in range(3):
                     if buttons[row][column]['text'] == "":
                         empty_cells.append((row, column))
              if len(empty_cells)>0:
                  win_move = None
                  for win_row,win_column in empty_cells:
                      
                     buttons[win_row][win_column]['text']=HC_player
                     
                     if check_winner() is True:
                         win_move=(win_row,win_column)
                         buttons[win_row][win_column]['text']=""
                         break
                     else:
                         buttons[win_row][win_column]['text']=""
                  if win_move:
                     win_row,win_column=win_move
                  else:
                     win_row,win_column=random.choice(empty_cells)

                  buttons[win_row][win_column]['text']=HC_player
                  if check_winner() is True:
                     status_label.config(text="Wanna play again!")
                     return 
                  HC_player=players[0]
                  status_label.config(text="Your Turn bro")
          elif check_winner() is True:
             status_label.config(text="Nice bro")
          elif check_winner()=="Tie":
             status_label.config(text="Tie!")   
                        
             
     
 

def check_winner():
  for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

  for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

  if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

  elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

  elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
  else:
      return False

       


def empty_spaces():
 spaces=9
 for row in range(3):
     for column in range(3):
         if buttons[row][column]['text']!="":
             spaces-=1
 if spaces==0:
     return False
 else:
     return True



def new_game():
    status_label.pack_forget()
    reset_button.pack_forget()
    frame.pack_forget()
    for row in range(3):
        for column in range(3):
            buttons[row][column].grid_forget()
    l1.pack()
    b1.pack()
    b2.pack()


def set_mode(value):
    global mode
    global frame
    global HC_player
    mode = value
    l1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    #print("mode=",mode)
    if mode == "HH":
        status_label.config(text=f"{player}'s Turn")
        status_label.pack(side=TOP)
        reset_button.pack(side=TOP)
        frame = Frame(window)
        frame.pack()
        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
                buttons[row][column].grid(row=row,column=column)
    else:
        
        HC_player=players[0]
        status_label.config(text="Your Turn->"+HC_player)
        status_label.pack(side=TOP)
        reset_button.pack(side=TOP)
        frame = Frame(window)
        frame.pack()
        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
                buttons[row][column].grid(row=row,column=column)
    status_label.pack()

window=Tk()
window.title("tic-tac-toe")
players=["x","o"]
mode = None
player=random.choice(players)
status_label = Label(window,
                     font=('consolas',40),
                     fg="black",
                     bg="red")
buttons: list[list[any]]=[[0,0,0],
         [0,0,0],
         [0,0,0]]
reset_button=Button(window,text="Restart",font=('consolas',20),fg="red",bg="black",command=new_game)

l1=Label(window,text="Please select the Mode of game",font=("cambria",20,'underline'),fg="red",bg="black")
l1.pack()
b1=Button(window,text="Human VS Human",font=("Arial",10,'bold'),fg="white",bg="black",command= lambda: set_mode("HH"))
b1.pack()
b2=Button(window,text="Human VS Computer",font=("Arial",10,'bold'),fg="white",bg="black",command= lambda: set_mode("HC"))
b2.pack()

window.mainloop()
