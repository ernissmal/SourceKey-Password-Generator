
from ast import List
from msilib.schema import File

import string
import random
from tkinter import Tk
from msilib.schema import CheckBox
from tkinter import *
import tkinter
from tkinter import Menu
import random
print("App started")

root = Tk("SourceKey Password Generator V.1.0")
root.geometry("500x400")

#Label
label = Label(root)
label.config(text = "Select characters and specify the password's length!")
label.pack()

#Characters list
characters=[]

#Password generator function
def clicked():
	#statements
	if (var1.get() == 1):
		characters.append('q');characters.append('w');characters.append('e');characters.append('r')
		characters.append('t');characters.append('y');characters.append('u');characters.append('i')
		characters.append('o');characters.append('p');characters.append('a');characters.append('s')
		characters.append('d');characters.append('f');characters.append('g');characters.append('h')
		characters.append('j');characters.append('k');characters.append('l');characters.append('z')
		characters.append('x');characters.append('c');characters.append('v');characters.append('b')
		characters.append('n');characters.append('m')
	else:
		pass

	if (var2.get() == 1):
		characters.append('Q');characters.append('W');characters.append('E');characters.append('R')
		characters.append('T');characters.append('Y');characters.append('U');characters.append('I')
		characters.append('O');characters.append('P');characters.append('A');characters.append('S')
		characters.append('D');characters.append('F');characters.append('G');characters.append('H')
		characters.append('J');characters.append('K');characters.append('L');characters.append('Z')
		characters.append('X');characters.append('C');characters.append('V');characters.append('B')
		characters.append('N');characters.append('M')
		print(characters)
	else:
		pass

	if (var3.get() == 1):
		characters.append('!');characters.append('@');characters.append('%');characters.append('(')
		characters.append(')');characters.append('*');characters.append('^');characters.append('/')
	else:
		pass

	if (var4.get() == 1):
		characters.append('0');characters.append('5')
		characters.append('1');characters.append('6')
		characters.append('2');characters.append('7')
		characters.append('3');characters.append('8')
		characters.append('4');characters.append('9')
		
		
	else:
		pass
	
   #Password generator process
	## shuffling the characters
	random.shuffle(characters)
	
	password = []
	f = open("password_file.txt","a")


	for i in range(var.get()):
		password.append(random.choice(characters))
	f.write("\nPassword:\n"+("".join(password)))
	f.read
	f.close
	label.config(text = "File saved as password_file.txt!")
	print("Passed")



###Checkboxes

#Letters checkbox
var1=IntVar()
checkbox1=Checkbutton(root,text="letters", variable=var1, onvalue=1, offvalue=0)
checkbox1.pack(anchor=CENTER)

#Capital letters checkbox
var2=IntVar()
checkbox2=Checkbutton(root,text="capital letters", variable=var2, onvalue=1, offvalue=0)
checkbox2.pack(anchor=CENTER)

#Special characters checkbox
var3=IntVar()
checkbox3=Checkbutton(root,text="special characters", variable=var3, onvalue=1, offvalue=0)
checkbox3.pack(anchor=CENTER)

#Digits checkbox
var4=IntVar()
checkbox4=Checkbutton(root,text="digits", variable=var4, onvalue=1, offvalue=0)
checkbox4.pack(anchor=CENTER)

#Password length input
var = IntVar()
scale = Scale( root, variable = var,orient=HORIZONTAL)
scale.pack(anchor=CENTER)



#Submit button
btn=Button(root,text="Submit parameters and generate password",command=clicked)
btn.pack()

#Mainloop
root.mainloop()
print("App finished and closed successfully!")