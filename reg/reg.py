from tkinter import *
raam = Tk()
raam.title("Gmail")
tahvel = Canvas(raam, width=1360, height=920, background="grey")
tahvel.grid()

#poland
tahvel.create_rectangle(30,200, 300,300,fill="red")
tahvel.create_rectangle(30,300, 300,400,fill="white")
#estonia
tahvel.create_rectangle(650,50, 300,150,fill="blue")
tahvel.create_rectangle(650,100, 300,150,fill="black")
tahvel.create_rectangle(650,200, 300,150,fill="white")
#bahama

tahvel.create_rectangle(30,50, 300,150,fill="cyan")
tahvel.create_rectangle(30,100, 300,150,fill="yellow")
tahvel.create_rectangle(30,200, 300,150,fill="cyan")
tahvel.create_polygon(30,50,100,125,30,200, fill="black")

raam.mainloop()
