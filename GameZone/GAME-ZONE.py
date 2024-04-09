from tkinter import *
from hangman import Hangman
from cricket import Cricket
from tic_tac_toe import TicTacToe
from stone_paper_scissor import SPS
from eggcatcher import EggCatcher
from Quize import Quize
from Number_Guessing import number

while True:
    try:
        print("\n\n\n      +"+"-"*40+"+")
        print("      |"+" "*10+"     GAMEZONE"+" "*17+"|")
        print("      +"+"-"*40+"+")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"1. HANGMAN"+" "*18+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"2. EGG CATCHER"+" "*14+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"3. TIC-TAC-TOE"+" "*14+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"4. CRICKET"+" "*18+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"5. STONE-PAPER-SCISSORS"+" "*5+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"6. QUIZ GAME"+" "*16+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"7. GUESS THE NUMBER"+" "*9+"|")
        print("      |"+" "*40+"|")
        print("      |"+" "*12+"8. EXIT"+" "*21+"|")
        print("      |"+" "*40+"|")
        print("      +"+"-"*40+"+")
        choice=int(input("\n      ENTER YOUR CHOICE: "))
        if choice==1:
            game1=Hangman()
            game1.main()
        elif choice==2:
            game2=EggCatcher()
            game2.main()
        elif choice==3:
            game3=TicTacToe()
            game3.main()
        elif choice==4:
            game4=Cricket()
            game4.printRules()
            game4.matchStart()
        elif choice==5:
            game5=SPS()
            game5.main()
        elif choice==6:
            game6=Quize()
            game6.main()
        elif choice==7:
            game7=number()
            number.start_game()
        elif choice==8:
            print("\n\n      +"+"-"*40+"+")
            print("      |"+" "*11+"EXITING THE SYSTEM"+" "*11+"|")
            print("      +"+"-"*40+"+\n")
            break
        else:
            print("\n\n      +"+"-"*40+"+")
            print("      |"+" "*7+"!! SELECT A VALID CHOICE !!"+" "*6+"|")
            print("      +"+"-"*40+"+\n")
    except Exception as e:
        print("Exception Occured! ", e)
