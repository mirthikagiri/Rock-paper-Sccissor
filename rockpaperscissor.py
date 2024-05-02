from tkinter import *
import random
from tkinter.font import Font

root = Tk()


root.geometry("5000x6000")
root.config(bg="#eeb8ae" )
root.iconbitmap("favicon.ico")


root.title("Rock Paper Scissor Game")


computer_value = {
	"0": "Rock",
	"1": "Paper",
	"2": "Scissor"
}



def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player ")
	l3.config(text="Computer")
	l4.config(text="")



def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"




def isrock():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "Match Draw"
	elif c_v == "Scissor":
		match_result = "Player Win"
	else:
		match_result = "Computer Win"
	l4.config(text=match_result)
	l1.config(text="Rock")
	l3.config(text=c_v)
	button_disable()




def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "Match Draw"
	elif c_v == "Scissor":
		match_result = "Computer Win"
	else:
		match_result = "Player Win"
	l4.config(text=match_result)
	l1.config(text="Paper")
	l3.config(text=c_v)
	button_disable()




def isscissor():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "Computer Win"
	elif c_v == "Scissor":
		match_result = "Match Draw"
	else:
		match_result = "Player Win"
	l4.config(text=match_result)
	l1.config(text="Scissor")
	l3.config(text=c_v)
	button_disable()

myfont=Font(family="Times", size=40,slant="italic", weight="bold")

Label(root,
	text="Rock Paper Scissor",
	font=myfont,
	fg="BLACK",bg="white").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text="Player ",
		font=myfont,bg="white")

l2 = Label(frame,
		text="VS ",
		font=myfont,bg="white")

l3 = Label(frame, text="Computer", font=myfont,bg="white")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
		text="",
		font=myfont,
		bg="white",fg="red",
		width=15,
		borderwidth=2,
		relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
			font=myfont, width=7,fg="white",bg="black",
			command=isrock)

b2 = Button(frame1, text="Paper ",
			font=myfont, width=7,fg="white",bg="black",
			command=ispaper)

b3 = Button(frame1, text="Scissor",
			font=myfont, width=7,fg="white",bg="black",
			command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game",
	font=myfont, fg="black",
	bg="white", command=reset_game).pack(pady=20)

root.mainloop()
