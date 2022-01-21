from tkinter import *
from tkinter.messagebox import *

def newroot(a:str):
	newwd=Toplevel() #tk()
	abc=Label(newwd,text=Lessons.get(a),font="Calibri 23",fg="black",justify=CENTER)
	newwd.geometry("500x90")
	abc.pack()

Lessons={}
with open("TextFile1.txt","r") as f:
	for i in f: # создаем цикл по количеству строк
		k,v=i.strip().split(" -") # отделяем слова на строчке в строчке по знаку " - "
		Lessons[k.strip()]=v.strip() # добавляем в словарь

root = Tk()

Label(text=" ").grid(row=0, column=0)
Label(text="0.").grid(row=0, column=1)
Label(text="1.").grid(row=0, column=2)
Label(text="2.").grid(row=0, column=3)
Label(text="3.").grid(row=0, column=4)
Label(text="4.").grid(row=0, column=5)
Label(text="5.").grid(row=0, column=6)
Label(text="6.").grid(row=0, column=7)
Label(text="7.").grid(row=0, column=8)
Label(text="8.").grid(row=0, column=9)
Label(text="9.").grid(row=0, column=10)
Label(text="10.").grid(row=0, column=11)
Label(text=" ").grid(row=0, column=0)
#Päevad
Label(text="Esmaspäev").grid(row=1, column=0)
Label(text="Teisipäev").grid(row=2, column=0)
Label(text="Kolmapäev").grid(row=3, column=0)
Label(text="Neljapäev").grid(row=4, column=0)
Label(text="Reede").grid(row=5, column=0)
#Ained
###Esmaspäev
Button(text="Tugiõpe",font="Arial,50",width=10,height=3,bg="#8D757F",relief=RIDGE,command=lambda a="Tugiope Eesti keel 2 grupp":newroot(a)).grid(row=1, column=2,sticky=N+S+W+E)
Button(text="Logistikateenused ",font="Arial,50",width=20,height=3,bg="green",relief=RIDGE,command=lambda a="Logistikateenused ja varude juhtimine":newroot(a)).grid(row=1, column=3,columnspan=2,sticky=N+S+W+E)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Matemaatika":newroot(a)).grid(row=1, column=5)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Matemaatika":newroot(a)).grid(row=1, column=6)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=1, column=7)
Button(text="Keel ja\n Kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Keel ja kirjandus":newroot(a)).grid(row=1, column=8)
Button(text="Keel ja\n Kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Keel ja kirjandus":newroot(a)).grid(row=1, column=9)
Button(text="Tugiõpe\n(Matemaatika) ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Tugiope Matemaatika":newroot(a)).grid(row=1, column=10)
###Teisipäev
Button(text="Tugiõpe ",font="Arial,50",width=10,height=3,bg="#D178DA",relief=RIDGE,command=lambda a="Tugiope Keemia":newroot(a)).grid(row=2, column=2,sticky=N+S+W+E)
Button(text="Programmeerimise alused ",font="Arial,50",width=30,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=2, column=3,columnspan=2,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=2, column=5)
Button(text="Füüsika ",font="Arial,50",width=20,height=3,bg="lightpink",relief=RIDGE,command=lambda a="Fuusika":newroot(a)).grid(row=2, column=6,columnspan=2)
Label(text=" ").grid(row=3, column=1)
###Kolmapäev
Button(text="Tugiõpe ",font="Arial,50",width=10,height=3,bg="#D178DA",relief=RIDGE,command=lambda a="Tugiõpe Eesti keel 1 grupp":newroot(a)).grid(row=3, column=2,sticky=N+S+W+E)
Button(text="Kunstiained ",font="Arial,50",width=20,height=3,bg="#9E54A6",relief=RIDGE,command=lambda a="Kunstiained":newroot(a)).grid(row=3, column=3,columnspan=2,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=3, column=5)
Button(text="Kehaline kasvatus ",font="Arial,50",width=20,height=3,bg="#9E54A6",relief=RIDGE,command=lambda a="Kehaline Kasvatus":newroot(a)).grid(row=3, column=6,columnspan=2)
Label(text=" ").grid(row=3, column=8)
Label(text=" ").grid(row=3, column=9)
Label(text=" ").grid(row=3, column=10)
###Neljapäev
Button(text="Logistikateenused ",font="Arial,50",width=20,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Logistikateenused ja varude juhtimine":newroot(a)).grid(row=4, column=2,columnspan=1,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=4, column=3,sticky=N+S+W+E)
Button(text="Programmerimise\nalused ",font="Arial,50",width=20,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=4, column=4,columnspan=2)
Button(text="Rakendustarkvara \nja arenduskeskkonna \nloomine",font="Arial,50",width=20,height=3,bg="#F77BAE",relief=RIDGE,command=lambda a="Rakendustarkvara ja arenduskeskkonna loomine":newroot(a)).grid(row=4, column=6,columnspan=2,sticky=N+S+W+E)
Button(text="Eesti keel ",font="Arial,50",width=20,height=3,bg="#8D757F",relief=RIDGE,command=lambda a="Eesti keel 2 grupp":newroot(a)).grid(row=4, column=8,columnspan=2,sticky=N+S+W+E)

###Reede
Button(text="Rakendustarkvara \nja arenduskeskkonna \nloomine",font="Arial,50",width=40,height=3,bg="#F77BAE",relief=RIDGE,command=lambda a="Rakendustarkvara ja arenduskeskkonna loomine":newroot(a)).grid(row=5, column=2,columnspan=2,sticky=N+S+W+E)
Button(text="Programmerimise alused(eesti keeles) ",font="Arial,50",width=65,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=5, column=3,columnspan=7)
Button(text="Inglise keel",font="Arial,50",width=20,height=3,bg="#42ED85",relief=RIDGE,command=lambda a="Inglise keel 2 grupp":newroot(a)).grid(row=5, column=9,columnspan=2)




root.mainloop()