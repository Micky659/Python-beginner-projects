import random
import tkinter


def winner(call): 
	if random.random() <= (1 / 5):
		throw = "rock" 
	elif (1 / 5) < random.random() <= (2 / 5):
		throw = "paper"
	elif (2 / 5) < random.random() <= (3 / 5):
		throw = "scissor"
	elif (3 / 5) < random.random() <= (4 / 5): 		throw = "lizard"
	else:
		throw = "spock"
     

	if(throw == "rock" and call == "paper") or  (throw == "paper" and call == "scissor"):
		result = "You won"
	elif(throw == "scissor" and call == "rock") or (throw == "lizard" and call == "rock"):
		result = "You won"
	elif(throw == "spock" and call == "lizard") or (throw == "scissor" and call == "spock"):
		result = "You won"
	elif(throw == "lizard" and call == "scissor") or (throw == "paper" and call == "lizard"):
		result = "You won"
	elif(throw == "spock" and call == "paper") or (throw == "rock" and call == "spock"):
		result = "You won!"
	elif throw == call:
		result = "It's a draw"
	else:
		result = "You lost!"

	global output
	output.config(text="Computer did: " + throw + "\n" + "You did: " + call + "\n" + result)

def pass_s():
	winner("scissor")
def pass_r():
	winner("rock")
def pass_p():
	winner("paper")
def pass_l():
	winner("lizard")
def pass_o():
	winner("spock") 

window = tkinter.Tk()

output=tkinter.Label(window, width=20, fg="red", text="What's your call?")
rock=tkinter.Button(window, text="Rock", bg="#eb96aa", padx =10, pady = 5, command = pass_r, width = 15)
paper=tkinter.Button(window, text="Paper", bg="#43b581", padx =10, pady = 5, command = pass_p, width = 15)
scissor=tkinter.Button(window, text="Scissor", bg="#5a4aa5", padx =10, pady = 5, command = pass_s , width = 15)
lizard=tkinter.Button(window, text="Lizard", bg="#f3c366", padx =10, pady = 5, command = pass_l, width = 15)
spock=tkinter.Button(window, text="Spock", bg="#ff6100", padx =10, pady = 5, command = pass_o, width = 15)

rock.pack(side="left")
paper.pack(side="left")
scissor.pack(side="left")
lizard.pack(side="left")
spock.pack(side="left")
output.place(anchor = "nw")
window.mainloop()