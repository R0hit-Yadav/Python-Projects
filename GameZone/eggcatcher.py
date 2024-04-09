from tkinter import *
import random
class EggCatcher:
    def __init__(self):
        self.root = Tk()
        self.root.title("Egg Catcher")
        self.height=600
        self.width=500

        #returns available screen's width and height
        self.x1=self.root.winfo_screenwidth()
        self.y1=self.root.winfo_screenheight()
        x=(self.x1/2)-(self.width/2)
        y=(self.y1/2)-(self.height/2)

        #set screen at center
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        self.canvas=Canvas(self.root,width=500,height=600)
        self.catcher=self.canvas.create_rectangle(10, 570, 90, 590,outline = "black", fill = "blue",width = 2)
        self.egg=self.canvas.create_oval(20, 10, 60, 70,outline = "red", fill = "Yellow",width = 2)
        self.score=0
        self.score_text = self.canvas.create_text(50, 20, text="Score: " + str(self.score),anchor="n")
        self.canvas.coords(self.score_text, 400, 10)
        self.root.attributes("-topmost", True) 
    def move_left(self):
        if self.canvas.coords(self.catcher)[0]>=80:
            self.canvas.move(self.catcher, -60, 0)
    def move_right(self):
        if self.canvas.coords(self.catcher)[2]<=800:
            self.canvas.move(self.catcher, 60, 0)
        
    def moveEgg(self,egg,score):
        self.canvas.move(self.egg,0,3)
        self.catchercoords=self.canvas.coords(self.catcher)
        self.eggcoords=self.canvas.coords(egg)
        if self.catchercoords[0]<=(self.eggcoords[0]+20) and self.catchercoords[2]>=(self.eggcoords[0]+20) and self.catchercoords[1]<self.eggcoords[3] and self.catchercoords[3]>self.eggcoords[3]:
            self.score+=1
            self.canvas.itemconfig(self.score_text, text="Score: " + str(self.score)) 
            self.canvas.delete(egg)
            x1=random.randrange(20,440)
            self.egg=self.canvas.create_oval(x1, 10, (x1+40), 70,outline = "red", fill = "Yellow",width = 2)
            self.moveEgg(self.egg,self.score)
            return True,
        elif self.catchercoords[1]<self.eggcoords[3] and (self.catchercoords[0]>(self.eggcoords[0]+20) or self.catchercoords[2]<(self.eggcoords[0]+20)) :
            print("Egg Not Caught ! Your Final Score is : ",self.score)
            self.canvas.delete(egg)
            self.root.destroy()
            return False
        self.canvas.after(10, self.moveEgg,egg,score)
    def main(self):
        self.left_button = Button(self.root, text="<-", command=self.move_left, width=5, height=1,bg="red", fg="white")
        self.left_button.place(x=10, y=0)

        self.right_button = Button(self.root, text="->", command=self.move_right, width=5, height=1 ,bg="red", fg="white")
        self.right_button.place(x=50, y=0)
        self.moveEgg(self.egg,self.score)
        self.canvas.pack()
        self.root.mainloop()
 
# game2=EggCatcher()
# game2.main()
