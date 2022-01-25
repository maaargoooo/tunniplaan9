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
		k,v=i.strip().split(" - ") # отделяем слова на строчке в строчке по знаку " - "
		Lessons[k.strip()]=v.strip() # добавляем в словарь

root = Tk()

Label(root,text=" ").grid(row=0,column=0)
Label(root,text="0.\n7.40-8.25",borderwidth=1,relief="solid").grid(row=0,column=2,sticky=W+E+N+S)
Label(root,text="1.\n8.30-9.15",borderwidth=1,relief="solid").grid(row=0,column=3,sticky=W+E+N+S)
Label(root,text="2.\n9.20-10.05",borderwidth=1,relief="solid").grid(row=0,column=4,sticky=W+E+N+S)
Label(root,text="3.\n10.10-10.55",borderwidth=1,relief="solid").grid(row=0,column=5,sticky=W+E+N+S)
Label(root,text="4.\n11.00-11.45",borderwidth=1,relief="solid").grid(row=0,column=6,sticky=W+E+N+S)
Label(root,text="5.\n11.50-12.35",borderwidth=1,relief="solid").grid(row=0,column=7,sticky=W+E+N+S)
Label(root,text="6.\n12.40-13.25",borderwidth=1,relief="solid").grid(row=0,column=8,sticky=W+E+N+S)
Label(root,text="7.\n13.30-14.15",borderwidth=1,relief="solid").grid(row=0,column=9,sticky=W+E+N+S)
Label(root,text="8.\n14.20-15.05",borderwidth=1,relief="solid").grid(row=0,column=10,sticky=W+E+N+S)
Label(root,text="9.\n15.10-15.55",borderwidth=1,relief="solid").grid(row=0,column=11,sticky=W+E+N+S)
Label(root,text="10.\n16.00-16.45",borderwidth=1,relief="solid").grid(row=0,column=12,sticky=W+E+N+S)

#Päevad
Label(text="Esmaspäev",borderwidth=1,relief="solid").grid(row=1, column=0,sticky=W+E+N+S)
Label(text="Teisipäev",borderwidth=1,relief="solid").grid(row=2, column=0,sticky=W+E+N+S)
Label(text="Kolmapäev",borderwidth=1,relief="solid").grid(row=3, column=0,sticky=W+E+N+S)
Label(text="Neljapäev",borderwidth=1,relief="solid").grid(row=4, column=0,sticky=W+E+N+S)
Label(text="Reede",borderwidth=1,relief="solid").grid(row=5, column=0,sticky=W+E+N+S)
#Ained

###Esmaspäev
Button(text="Tugiope Eesti keel 2 grupp",font="Arial,50",bg="#8D757F",borderwidth=1,relief=RIDGE,command=lambda a="Tugiope Eesti keel 2 grupp":newroot(a)).grid(row=1,column=3,sticky=W+E+N+S)
Button(text="Logistikateenused ",font="Arial,50",width=20,height=3,bg="green",relief=RIDGE,command=lambda a="Logistikateenused ja varude juhtimine":newroot(a)).grid(row=1, column=4,columnspan=2,sticky=N+S+W+E)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Matemaatika":newroot(a)).grid(row=1, column=6,sticky=N+S+W+E)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Matemaatika":newroot(a)).grid(row=1, column=7,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=1, column=7,sticky=N+S+W+E)
Button(text="Keel ja\n Kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Keel ja kirjandus":newroot(a)).grid(row=1, column=8,sticky=N+S+W+E)
Button(text="Keel ja\n Kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Keel ja kirjandus":newroot(a)).grid(row=1, column=9,sticky=N+S+W+E)
Button(text="Tugiõpe\n(Matemaatika) ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=lambda a="Tugiope Matemaatika":newroot(a)).grid(row=1, column=10,sticky=N+S+W+E)
###Teisipäev
Button(text="Tugiõpe(Keemia) ",font="Arial,50",width=10,height=3,bg="#D178DA",relief=RIDGE,command=lambda a="Tugiope Keemia":newroot(a)).grid(row=2, column=3,sticky=N+S+W+E)
Button(text="Programmeerimise alused ",font="Arial,50",width=30,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=2, column=4,columnspan=3,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=2, column=7,sticky=N+S+W+E)
Button(text="Füüsika ",font="Arial,50",width=20,height=3,bg="lightpink",relief=RIDGE,command=lambda a="Fuusika":newroot(a)).grid(row=2, column=8,columnspan=2,sticky=N+S+W+E)
Label(text=" ").grid(row=3, column=1,sticky=N+S+W+E)
###Kolmapäev
Button(text="Tugiõpe(Eesti keel \n 1 grupp) ",font="Arial,50",width=10,height=3,bg="#D178DA",relief=RIDGE,command=lambda a="Tugiope Eesti keel 1 grupp":newroot(a)).grid(row=3, column=3,sticky=N+S+W+E)
Button(text="Kunstiained ",font="Arial,50",width=20,height=3,bg="#9E54A6",relief=RIDGE,command=lambda a="Kunstiained":newroot(a)).grid(row=3, column=4,columnspan=2,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=3, column=6,sticky=N+S+W+E)
Button(text="Kehaline kasvatus ",font="Arial,50",width=20,height=3,bg="#9E54A6",relief=RIDGE,command=lambda a="Kehaline Kasvatus":newroot(a)).grid(row=3, column=7,columnspan=2,sticky=N+S+W+E)
Label(text=" ").grid(row=3, column=9,sticky=N+S+W+E)
Label(text=" ").grid(row=3, column=10,sticky=N+S+W+E)
###Neljapäev
Button(text="Logistikateenused ",font="Arial,50",width=20,height=3,bg="lightgreen",relief=RIDGE,command=lambda a="Logistikateenused ja varude juhtimine":newroot(a)).grid(row=4, column=3,columnspan=2,sticky=N+S+W+E)
Label(text="Puhkemine",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=4, column=5,sticky=N+S+W+E)
Button(text="Programmerimise\nalused ",font="Arial,50",width=20,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=4, column=6,columnspan=2,sticky=N+S+W+E)
Button(text="Rakendustarkvara \nja arenduskeskkonna \nloomine",font="Arial,50",width=20,height=3,bg="#F77BAE",relief=RIDGE,command=lambda a="Rakendustarkvara ja arenduskeskkonna loomine":newroot(a)).grid(row=4, column=8,columnspan=2,sticky=N+S+W+E)
Button(text="Eesti keel ",font="Arial,50",width=20,height=3,bg="#8D757F",relief=RIDGE,command=lambda a="Eesti keel 2 grupp":newroot(a)).grid(row=4, column=10,columnspan=2,sticky=N+S+W+E)
Button(text="Rühmajuhataja \n tund",font="Arial,50",borderwidth=1,relief=RIDGE,bg="#F335F6",command=lambda a="Ruhmajuhataja tund":newroot(a)).grid(row=4,column=12,sticky=W+E+N+S)

###Reede
Button(text="Rakendustarkvara \nja arenduskeskkonna \nloomine",font="Arial,50",width=40,height=3,bg="#F77BAE",relief=RIDGE,command=lambda a="Rakendustarkvara ja arenduskeskkonna loomine":newroot(a)).grid(row=5, column=3,columnspan=2,sticky=N+S+W+E)
Button(text="Programmerimise alused(eesti keeles) ",font="Arial,50",width=65,height=3,bg="lightblue",relief=RIDGE,command=lambda a="Programmeerimise alused":newroot(a)).grid(row=5, column=5,columnspan=5,sticky=N+S+W+E)
Button(text="Inglise keel",font="Arial,50",width=20,height=3,bg="#42ED85",relief=RIDGE,command=lambda a="Inglise keel 2 grupp":newroot(a)).grid(row=5, column=10,columnspan=2,sticky=N+S+W+E)




root.mainloop()