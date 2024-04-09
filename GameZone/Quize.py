class Quize:
    def main(self):
        def give_options(a,b,c,d):
            print("A):", a)
            print("B):", b)
            print("C):", c)
            print("D):", d)
            
        print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
        ans = input("Are you ready to play (yes/no): ")
        a ="Note: Wrtie Only Option."
        score = 0
        total_questions = 4

        correct_ans =["United States", "Emmanuel Macron", "1912", "1914","Brahma","Vishnu","120m","9 cm/s","175 Gayle From RCB","Rohit Sharma"]

        if ans.lower() == "yes":

            print(a)
            print("Question 1- Which country won the most gold medals in the Tokyo 2020 Olympics? ")
            give_options("United States", "China", "Japan","Britain" )
            ans=input("==========>")
            if ans.lower() == 'a':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")

            
            print()
            print("Question 2- Who is the current President of France as of 2024?")
            give_options("Marine Le Pen", "Emmanuel Macron", "François Hollande","Nicolas Sarkozy")
            ans = input("==========>")
            if ans.lower() == 'b':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")

            
            print()
            print("Question 3- In which year did the Titanic sink ? ")
            give_options("1910", "1912", "1915" ,"1917")
            ans = input("==========>")
            if ans.lower() == 'b':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")

            
            print()
            print("Question 4- In which year did World War I begin?")
            give_options("1914", "1916", "1918" ,"1920")
            ans = input("==========>")
            if ans.lower() == 'a':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")

                
            print()
            print("Question 5-In Hindu mythology, who is considered the creator god, responsible for the creation of the universe?")
            give_options("Vishnu", "Shiva", "Brahma" ,"Ganesh")
            ans = input("==========>")
            if ans.lower() == 'c':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")
            
            print()
            print("Question 6- Who is the preserver god in Hindu mythology, responsible for maintaining the balance of the universe?")
            give_options("Shiva", "Brahma", "Indra" ,"Vishnu")
            ans = input("==========>")
            if ans.lower() == 'd':
                score=score+1
                print("Correct !!")
            else: 
                print("Incorrect !!")
                               
            
                               
            
            print()
            print("Question 7- The angle of elevation of the top of a tower from a point 60 meters from its base is 30 degree What is the height of the tower?")
            give_options("30m", "60m", "90m" ,"120m")
            ans = input("==========>")
            if ans.lower() == 'd':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")
                               
            
            print()
            print("Question 8- The radius of a circle is increasing at a rate of 3 cm/s. What is the rate of increase of its circumference when the radius is 5 cm?")
            give_options("3 cm/s", "6 cm/s", "9 cm/s" ,"15 cm/s")
            ans = input("==========>")
            if ans.lower() == 'c':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")
                               
            
            print()
            print("Question 9- What is the highest ipl score by a player and from which team ?")
            give_options("158 Mccullum From KKR", "180 Warner From DC", "175 Gayle From RCB" ,"168 Rohit MI")
            ans = input("==========>")
            if ans.lower() == 'c':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")
                               
            
            print()
            print("Question 5- which player has win most ipl trophy as player?")
            give_options("Rohit Sharma", "Virat Kholi", "MS Dhoni" ,"Ab de villiers")
            ans = input("==========>")
            if ans.lower() == 'a':
                score=score+1
                print("Correct !!")
            else:
                print("Incorrect !!")



        i = score*10
        if i<30:
            print("Ouch, your score is ",i,"/ 100 improve your self.")
        elif 31 <i <75:
            print("Nice! you scored ",i,"/ 100 you are quiet smart.")
        else:
            print("Congratulations! it's a perfect ",i,"/ 100 you are Intelligent.")
