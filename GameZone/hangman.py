from tkinter import *
import random
class Hangman:
    def __init__(self):
        self.root=Tk()
        self.height=400
        self.width=500
        self.x1=self.root.winfo_screenwidth()
        self.y1=self.root.winfo_screenheight()
        self.x=(self.x1/2)-(self.width/2)
        self.y=(self.y1/2)-(self.height/2)
        #set screen at center
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y)) 
        self.root.attributes("-topmost", True)   
    def main(self):
        self.catagory = {
        "ANIMAL": ["LION", "ELEPHANT", "GIRAFFE", "TIGER", "MONKEY", "KANGAROO", "ZEBRA", "PENGUIN", "PANDA", "KOALA"],
        "FRUIT": ["APPLE", "BANANA", "ORANGE", "GRAPES", "WATERMELON", "STRAWBERRY", "PINEAPPLE", "MANGO", "KIWI", "PEACH"],
        "COLOR": ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "ORANGE", "PINK", "BROWN", "BLACK", "WHITE"],
        "COUNTRY": ["USA", "CANADA", "INDIA", "AUSTRALIA", "BRAZIL", "CHINA", "GERMANY", "FRANCE", "JAPAN", "MEXICO"],
        "VEHICLE": ["CAR", "BUS", "BICYCLE", "MOTORCYCLE", "TRUCK", "TRAIN", "BOAT", "HELICOPTER", "AIRPLANE", "SCOOTER"],
        "INSTRUMENT": ["PIANO", "GUITAR", "VIOLIN", "TRUMPET", "FLUTE", "DRUMS", "SAXOPHONE", "CLARINET", "CELLO", "HARP"]
        }
        self.catagory_list=['ANIMAL', 'FRUIT', 'COLOR', 'COUNTRY', 'VEHICLE', 'INSTRUMENT']
        self.computer_choice1=random.choice(self.catagory_list)
        self.computer_choice2=random.choice(self.catagory[self.computer_choice1])
        print(self.computer_choice1)
        print(self.computer_choice2)
        self.hint_label=Label(self.root,text=self.computer_choice1)
        self.hint_label.pack()
        self.temp1=list("_"*len(self.computer_choice2))
        self.guess_label=Label(self.root,text=self.temp1)
        self.guess_label.pack()
        self.i=Entry(self.root,text="Guess")
        self.temp2=self.temp1
        self.i.pack()
        self.guess_btn=Button(self.root,text="Guess",command=self.isGuessCorrect)
        self.guess_btn.pack()
        self.c=0
        self.l1=Label(self.root,text="+------------++",font=("Arial",15))
        self.l2=Label(self.root,text="+------------++",font=("Arial",15))
        self.l3=Label(self.root,text="                ++",font=("Arial",15))
        self.l4=Label(self.root,text="                ++",font=("Arial",15))
        self.l5=Label(self.root,text="                ++",font=("Arial",15))
        self.l6=Label(self.root,text="                ++",font=("Arial",15))
        self.l7=Label(self.root,text="                ++",font=("Arial",15))
        self.l8=Label(self.root,text="                ++",font=("Arial",15))
        self.l9=Label(self.root,text="+++++++++++++++",font=("Arial",15))  
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()
        self.l4.pack()
        self.l5.pack()
        self.l6.pack()
        self.l7.pack()
        self.l8.pack()
        self.l9.pack()



        self.root.mainloop()
    def isGuessCorrect(self):
        self.j=self.i.get().upper()
        if (self.j) in self.computer_choice2:
            for i1 in range (len(self.computer_choice2)):
                if self.computer_choice2[i1]==self.j and self.j!="_":
                    self.temp2[i1]=self.j
            self.guess_label.config(text="".join(self.temp2))
            self.i.delete(0,END)
            if "_" not in self.temp2:
                self.l3.config(text="                ++")
                self.l4.config(text="                ++",font=("Arial",15))
                self.l5.config(text="                ++")
                self.l6.config(text="\\😀/      ++",font=("Arial",20))
                self.l7.config(text="   |            ++")
                self.l8.config(text="  / \\           ++")
                self.i.destroy()
                self.guess_btn.config(text="YOU WON! YOU GUESSED IT RIGHT",command=self.root.destroy)
        else:
            self.hanger()
    def hanger(self):
        global c
        print(self.c)
        self.c=self.c+1
        if self.c==1:
            self.l3.config(text="   |            ++")
            self.i.delete(0,END)
        elif self.c==2:
            self.l4.config(text=" 😭       ++",font=("Arial",20))
            self.i.delete(0,END)
        elif self.c==3:
            self.l5.config(text="   |            ++")
            self.i.delete(0,END)
        elif self.c==4:
            self.l5.config(text="  /|            ++")
            self.i.delete(0,END)
        elif self.c==5:
            self.l5.config(text="  /|\\           ++")
            self.i.delete(0,END)
        elif self.c==6:
            self.l6.config(text="  /             ++")
            self.i.delete(0,END)
        elif self.c==7:
            self.l6.config(text="  / \\           ++")
            self.i.destroy()
            self.guess_btn.config(text="GAME OVER!YOU HANGED" ,command=self.root.destroy)
