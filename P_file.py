from tkinter import *
from PIL import Image, ImageTk
from random import randint 

#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background = "#63dcf7")


#picture
rock_img = ImageTk.PhotoImage(Image.open("rockimg.png"))
paper_img = ImageTk.PhotoImage(Image.open("paperimg.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissorimg.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#insert picture 
user_label = Label(root, image=scissor_img, bg="#63dcf7")
comp_label = Label(root, image=scissor_img_comp, bg="#63dcf7")
comp_label.grid(row=3,column=0)
user_label.grid(row=3,column=4)

#scores
playerscore = Label(root,text=0,font=100,bg="#63dcf7",fg="white")
computerscore = Label(root,text=0,font=100,bg="#63dcf7",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",fg="white",bg="#63dcf7")
comp_indicator = Label(root,font=50,text="COMPUTER",fg="white",bg="#63dcf7")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50, bg="#63dcf7", fg="white")
msg.grid(row=3, column=2) 

#update message
def updatemessage(x):
    msg["text"] = x 

#update user score 
def updateuserscore():
    score = int(playerscore["text"])
    score = score + 1
    playerscore["text"] = str(score)

#update computer score
def updatecompscore():
    score = int(computerscore["text"])
    score = score + 1
    computerscore["text"] = str(score)

#check winner
def checkwinner(player, computer):
    if player == computer:
        updatemessage("It's a tie!!!")

    elif player == "rock":
        if computer == "paper":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore()

    elif player == "paper":
        if computer == "scissor":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")
            updateuserscore()

    elif player == "scissor":
        if computer == "rock":
            updatemessage("You Loose")
            updatecompscore()
        else:
            updatemessage("You Win")    
            updateuserscore()

    else:
        pass        

#update choices
choices = ["rock", "paper", "scissor"]

def updatechoices(x):

#for computer
    compchoice = choices[randint(0, 2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x ==  "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwinner(x,compchoice)


#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#b8bab9",fg="#000000",command =lambda:updatechoices("rock")).grid(row=12,column=1) 
paper = Button(root,width=20,height=2,text="PAPER",bg="#e6f2ef",fg="#152324",command =lambda:updatechoices("paper")).grid(row=12,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#f25a76",fg="#0e0f0e",command =lambda:updatechoices("scissor")).grid(row=12,column=3)


root.mainloop() 

