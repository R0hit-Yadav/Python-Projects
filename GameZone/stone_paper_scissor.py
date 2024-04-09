from tkinter import * 
import random
from functools import partial
class SPS:
    def __init__(self):
        self.root=Tk()
        self.height1=400
        self.width1=600
        self.w=(self.root.winfo_screenwidth())
        self.h=(self.root.winfo_screenheight())
        self.x=(self.w/2)-(self.width1/2)
        self.y=(self.h/2)-(self.height1/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width1, self.height1, self.x, self.y))
        self.root.attributes("-topmost", True)
    def getUserChoice(self,a):
        self.user_choice=a.lower()
        self.num=random.choice(["stone","paper","scissor"])
        print(" Computer's choice: ",self.num)
        if (self.user_choice== "stone" and self.num=="paper") or (self.user_choice== "paper" and self.num=="scissor") or (self.user_choice== "scissor" and self.num=="stone"):
            self.c=Label(text="User's Choice: "+self.user_choice,font=("Arial",20))
            self.b=Label(text="Computer's Choice: "+self.num,font=("Arial",20))
            self.a=Label(text="Computer Won",font=("Arial",20))
        elif (self.user_choice==self.num):
            self.c=Label(text="User's Choice: "+self.user_choice,font=("Arial",20))
            self.b=Label(text="Computer's Choice: "+self.num,font=("Arial",20))
            self.a=Label(text="Draw",font=("Arial",20))
        else: 
            self.c=Label(text="User's Choice: "+self.user_choice,font=("Arial",20))
            self.b=Label(text="Computer's Choice: "+self.num,font=("Arial",20))
            self.a=Label(text="User Won",font=("Arial",20))
        self.b.pack()
        self.c.pack()
        self.a.pack()
        self.stone_btn.destroy()
        self.paper_btn.destroy()
        self.scissor_btn.destroy()


    def main(self):
        self.stone_photo=PhotoImage(file="rock.png")
        self.stone_photo_image=self.stone_photo.subsample(2,2)
        self.stone_btn = Button(self.root, text="Button-1",image=self.stone_photo_image,height=100,width=140,command=partial(self.getUserChoice,"stone"))
        self.paper_photo=PhotoImage(file="paper.png")
        self.paper_photo_image=self.paper_photo.subsample(2,2)
        self.paper_btn = Button(self.root, text="Button-2",image=self.paper_photo_image,height=100,width=140,command=partial(self.getUserChoice,"paper"))
        self.scissor_photo=PhotoImage(file="scissor.png")
        self.scissor_photo_image=self.scissor_photo.subsample(3,3)
        self.scissor_btn = Button(self.root, text="Button-3",image=self.scissor_photo_image,height=100,width=140,command=partial(self.getUserChoice,"scissor"))
        self.stone_btn.pack()
        self.paper_btn.pack()
        self.scissor_btn.pack()
        self.root.mainloop() 

